#!pip install --upgrade torch
#!pip install git+https://github.com/huggingface/transformers triton==3.4 kernels
#!pip uninstall torchvision torchaudio -y

import transformers
import torch

from transformers import AutoModelForCausalLM, AutoTokenizer

import time
import datetime

def setupLLM(model="openai/gpt-oss-20b"):
    print("Setting up local LLM:", model)

    model_id = "openai/"+model.replace("_", "-")

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype="auto", # was auto
        device_map="cuda", # was cuda, could be auto.
    )
    return tokenizer, model


def askLLM(tokenizer, model, prompt):
    # print(model.hf_device_map)
    messages = [
        {"role": "user", "content": prompt},
    ]

    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt",
        return_dict=True,
    ).to(model.device)

    # Can add "reasoning_effort="high"" after return_dict.

    generated = model.generate(**inputs, max_new_tokens=2000)
    result = tokenizer.decode(generated[0][inputs["input_ids"].shape[-1]:])
    # print(tokenizer.decode(generated[0][inputs["input_ids"].shape[-1]:]))
    return result

def makeRequest():
    print("Starting request.")

    start = time.perf_counter()
    starttime = str(datetime.datetime.now())
    result = askLLM(tokenizer, model, prompt)
    endtime = str(datetime.datetime.now())
    end = time.perf_counter()


    print("\n\nTime taken for comparisons: ", str(end - start), " seconds.\nStarttime: ", starttime, " Endtime: ", endtime)
    print("\n\nResponse: ", result, "\n")

# tokenizer, model = setupLLM()
# print("Asking LLM ...")
# makeRequest()
