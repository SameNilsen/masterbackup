# !pip install jedi
# #!pip install protobuf==5.29.3
# #!pip install vllm==0.7.0
# !pip install transformers==4.57.6
# !pip install vllm==0.11.0
# #!pip install vllm


from vllm import LLM, SamplingParams
import torch
import time
import datetime


def load():
  print("Loading NorMistral model with vLLM...")
  # load the NorMistral model
#   global llm
  llm = LLM(
      model="norallm/normistral-11b-thinking",
      dtype=torch.bfloat16,
      trust_remote_code=True,
    #   quantization="bitsandbytes",
      #load_format="bitsandbytes",
      #dtype="half", # prev bfloat16.
      #tensor_parallel_size=1,
      gpu_memory_utilization=0.8,
      max_model_len=32768 # 16384 funka, 32768 er kanskje bedre.
  )

  print("load done")
  return llm

def setup():
  print("Setting up sampling parameters...")
  # set up sampling parameters (equivalent to the generate() parameters)
#   global sampling_params
  sampling_params = SamplingParams(
      max_tokens=2048,  # limit max number of generated tokens
      top_k=64,  # top-k sampling
      top_p=0.9,  # nucleus sampling
      temperature=0.3,  # a low temperature to make the outputs less chaotic
      repetition_penalty=1.0,  # turn the repetition penalty off
  )
  print("setup done")
  return sampling_params



def callvLLM(prompt, llm, sampling_params):
  print("Received prompt: ", prompt)
  #prompt = "Which city is the Eiffel Tower located in?"
  messages = [
      {"role": "user", "content": prompt}
  ]
  # run the generation using the chat interface (applies chat template automatically)
  outputs = llm.chat(messages, sampling_params=sampling_params)

  # get the generated text
  output_str = outputs[0].outputs[0].text.strip()

  # separate the reasoning trace that's enclosed in the special <think> ... </think> tokens
  reasoning_trace = output_str.split("</think>")[0].lstrip("<think>").strip()

  # separate the actual response that follows after the </think> token
  response = output_str.split("</think>")[-1].rstrip("</s>").strip()

  #print("\nReasoning trace:\n", reasoning_trace)
  #print("Generated response:\n", response)

  return response


def makeSimultaneousvLLMRequest(prompts, llm, sampling_params):
    outputs = llm.generate(prompts, sampling_params)
    return outputs


