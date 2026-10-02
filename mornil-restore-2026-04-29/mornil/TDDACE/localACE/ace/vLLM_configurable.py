# !pip install jedi
# #!pip install protobuf==5.29.3
# #!pip install vllm==0.7.0
# !pip install transformers==4.57.6
# !pip install vllm==0.11.0
# #!pip install vllm


from vllm import LLM, SamplingParams
from vllm.sampling_params import StructuredOutputsParams
import torch
import time
import datetime

from pydantic import BaseModel
from enum import Enum

json_mode = True
MAX_TOKENS = 6000
print("NB: JSON MODE TRUE")

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

def setup(mode="generator"):
  print("Setting up sampling parameters...")
  # set up sampling parameters (equivalent to the generate() parameters)
  if (json_mode):
    if (mode == "generator"):
      json_schema = ACEgeneratorResponse.model_json_schema()
    elif (mode == "reflector"):
      json_schema = ACEreflectorResponse.model_json_schema()
    elif (mode == "curator"):
      json_schema = ACEcuratorResponse.model_json_schema()
    else:
      print("WRONG USE AAAA")
      json_schema = ACEgeneratorResponse.model_json_schema()
    structured_outputs_params_json = StructuredOutputsParams(json=json_schema)
    sampling_params = SamplingParams(
        max_tokens=MAX_TOKENS,  # limit max number of generated tokens
        structured_outputs=structured_outputs_params_json,
        # max_tokens=MAX_TOKENS
    )
  else:
    sampling_params = SamplingParams(
        max_tokens=2048,  # limit max number of generated tokens
        top_k=64,  # top-k sampling
        top_p=0.9,  # nucleus sampling
        temperature=0.3,  # a low temperature to make the outputs less chaotic
        repetition_penalty=1.0,  # turn the repetition penalty off
    )
  print("setup done")
  return sampling_params

class ACEgeneratorResponse(BaseModel):
    reasoning: str
    bullet_ids: str
    final_answer: str

class ACEreflectorResponse(BaseModel):
    reasoning: str
    error_identification: str
    root_cause_analysis: str
    correct_approach: str
    key_insight: str
    bullet_tags: str

class ACEcuratorResponse(BaseModel):
    reasoning: str
    operations: str

def callvLLM(prompt, llm, sampling_params):
  messages = [
      {"role": "user", "content": prompt}
  ]

  prompt_json = prompt

  accepted_answer_length = False
  while accepted_answer_length is False:
      print("->Attempting to generate answer.")
      # run the generation using the chat interface (applies chat template automatically)
      if (json_mode):
        if (prompt.startswith("You are an expert analyst")):
          print("REFLECTION DETECTED")
          sampling_params = setup(mode="reflector")
        elif (prompt.startswith("You are a Test Driven Development")):
          print("GENERATION DETECTED")
          sampling_params = setup(mode="generator")
        elif (prompt.startswith("You are a master curator")):
          print("CURATION DETECTED")
          sampling_params = setup(mode="curator")
        outputs = llm.generate(prompt_json, sampling_params=sampling_params)
      else:
        outputs = llm.chat(messages, sampling_params=sampling_params)

      # print("\n\n-----------------------FULL RESPONSE-----------------------")
      # print(outputs)
      # print("\n\n-----------------------      END    -----------------------")

      generated_tokens = len(outputs[0].outputs[0].token_ids)

      print(f"Generated tokens: {generated_tokens}")
      print(f"Hit max_tokens: {generated_tokens >= MAX_TOKENS}")
      if (generated_tokens >= MAX_TOKENS):
          accepted_answer_length = False
      else:
          accepted_answer_length = True
  print("->Generated answer length accepted...")

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
  print("\n\n-----------------------RETURNED RESPONSE-----------------------")
  print(response)
  print("\n\n-----------------------      END    -----------------------")
  return response


def makeSimultaneousvLLMRequest(prompts, llm, sampling_params):
    outputs = llm.generate(prompts, sampling_params)
    return outputs


