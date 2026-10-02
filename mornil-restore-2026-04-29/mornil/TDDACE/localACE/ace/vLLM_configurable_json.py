# !pip install jedi
# #!pip install protobuf==5.29.3
# #!pip install vllm==0.7.0
# !pip install transformers==4.57.6
# !pip install vllm==0.11.0
# kernels 0.5.0 ?
# #!pip install vllm

"""
import vLLM_configurable
llm = vLLM_configurable.load(model_name=args.generator_model ,dtype=args.dtype, quantization=args.quantization, model_length=args.model_length, gpu_memory_utilization=args.gpu_usage)
samplingparams = vLLM_configurable.setup()


import vLLM_configurable
response = vLLM_configurable.callvLLM(prompt, llm, samplingparams)
"""


from vllm import LLM, SamplingParams
from vllm.sampling_params import StructuredOutputsParams
import torch
import time
import datetime

from pydantic import BaseModel
from enum import Enum


def load(model_name="norallm/normistral-11b-thinking", dtype="bfloat16", quantization="full", model_length=32768, gpu_memory_utilization=0.8):
  print("Loading NorMistral model with vLLM and paramaters:", dtype, quantization, model_length, gpu_memory_utilization)
  if (model_name == "normistral11b_thinking"):
      model_name = "norallm/normistral-11b-thinking"
  elif (model_name == "gpt_oss_20b" or model_name == "gpt_oss_120b"):
      model_name = "openai/"+model_name.replace("_", "-")
  if (dtype == "bfloat16"):
     torch_dtype = torch.bfloat16
  elif (dtype == "half"):
     torch_dtype = "half"
  elif (dtype == "auto"):
     torch_dtype = "auto"
  if (quantization == "full"):
     quant = None
  elif (quantization == "4bit"):
     if (model_name == "gpt_oss_20b" or model_name == "gpt_oss_120b"):
         quant = None
     else:
         quant = "bitsandbytes"
  # load the NorMistral model
  llm = LLM(
      model=model_name,
      dtype=torch_dtype,
      trust_remote_code=True,
      quantization=quant,
      gpu_memory_utilization=gpu_memory_utilization,
      max_model_len=model_length # 16384 funka, 32768 er kanskje bedre.
  )

  print("load done")
  return llm

def setup():
  print("Setting up sampling parameters...")
  # set up sampling parameters (equivalent to the generate() parameters)

  # json_schema = CarDescription.model_json_schema()
  json_schema = ACEgeneratorResponse.model_json_schema()
  structured_outputs_params_json = StructuredOutputsParams(json=json_schema)

  sampling_params = SamplingParams(
      max_tokens=4000,  # limit max number of generated tokens
      # top_k=64,  # top-k sampling
      # top_p=0.9,  # nucleus sampling
      # temperature=0.3,  # a low temperature to make the outputs less chaotic
      # repetition_penalty=1.0,  # turn the repetition penalty off
      structured_outputs=structured_outputs_params_json,
      # max_tokens=MAX_TOKENS
  )
  print("setup done")
  return sampling_params

class CarDescription(BaseModel):
    brand: str
    model: str
    car_type: str

class ACEgeneratorResponse(BaseModel):
    reasoning: str
    bullet_ids: str
    final_answer: str

def callvLLM(prompt, llm, sampling_params):
  messages = [
      {"role": "user", "content": prompt}
  ]

  prompt_json = (
    "Generate a JSON with the brand, model and car_type of "
    "the most iconic car from the 90's"
  )

  prompt_json = (
    '''
    You are a Test Driven Development (TDD) expert programmer tasked with implementing functions and tests using your knowledge, a curated playbook of strategies and insights and a reflection that goes over the diagnosis of all previous mistakes made during development.

In this first iteration your only task is to generate tests that will later be asserted using PyTest. Analyze the function requirements and create the neccessary tests. Do not include import statements for the function that the tests shall test, they will be included later.

**Instructions:**
- Read the playbook carefully and apply relevant strategies, formulas, and insights
- Pay attention to common mistakes listed in the playbook and avoid them
- Show your reasoning step-by-step
- Be concise but thorough in your analysis
- If the playbook contains relevant code snippets or formulas, use them appropriately
- Double-check your calculations and logic before providing the final answer

Your output should be a json object, which contains the following fields:
- reasoning: your chain of thought / reasoning / thinking process, detailed analysis and calculations
- bullet_ids: each line in the playbook has a bullet_id. All bulletpoints in the playbook that's relevant, helpful for you to answer this question, you should include their bullet_id in this list
- final_answer: your concise final implementation that should start with "def test_..."


**Playbook:**
## STRATEGIES & INSIGHTS

## FORMULAS & CALCULATIONS

## CODE SNIPPETS & TEMPLATES

## COMMON MISTAKES TO AVOID

## PROBLEM-SOLVING HEURISTICS

## CONTEXT CLUES & INDICATORS

## OTHERS

**Reflection:**
(empty)

**Question:**



def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries.

    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
. Entry point: sum_squares

**Context:**

    '''
  )
  prompt_json = prompt

  # # run the generation using the chat interface (applies chat template automatically)
  # outputs = llm.chat(messages, sampling_params=sampling_params)
  # outputs = llm.chat(prompt_json, sampling_params=sampling_params)
  outputs = llm.generate(prompt_json, sampling_params=sampling_params)

  print("-----------------------FULL RESPONSE-----------------------")
  print(outputs)
  print("-----------------------      END    -----------------------")

  # get the generated text
  output_str = outputs[0].outputs[0].text.strip()

  # separate the reasoning trace that's enclosed in the special <think> ... </think> tokens
  reasoning_trace = output_str.split("</think>")[0].lstrip("<think>").strip()

  # separate the actual response that follows after the </think> token
  response = output_str.split("</think>")[-1].rstrip("</s>").strip()

  try:
    response = response.split("---", 1)[1]
  except:
    print("Not able to split on ---, returning full result")
  # Return only JSON part of the response:
  try:
    if (response.find("assistantfinal") != -1):
      response = response.split("assistantfinal", 1)[1]
      print("Detected gpt_oss-style output, extracting JSON part")
    else:
      # response = response.split("**Answer in JSON format**", 1)[1]
      # Regex pattern to match the required formats of anything like "answer" inside of "** **"
      import re
      # pattern = r"\*\*.*?answer.*?\*\*"
      pattern = r"\*\*.*?JSON.*?\*\*"
      response = response.split(re.findall(pattern, response, re.IGNORECASE)[-1])[1]
      print("Detected normistral-style output, extracting JSON part")
  except:
    print("Not able to split on **Answer in JSON format** or assistantfinal, returning full result")
  return response


def makeSimultaneousvLLMRequest(prompts, llm, sampling_params):
    outputs = llm.generate(prompts, sampling_params)
    return outputs



def start():
  if __name__ == "__main__":
    print("Loading...")
    llm = load("gpt_oss_20b" ,"auto", "full", 32768, "0.96")
    samplingparams = setup()
  print("Generating...")
  prompt = "Hello."
  response = callvLLM(prompt, llm, samplingparams)
  print("Final response: ", response)

start()