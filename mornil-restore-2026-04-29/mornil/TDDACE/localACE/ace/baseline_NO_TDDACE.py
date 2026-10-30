# !pip install jedi
# #!pip install protobuf==5.29.3
# #!pip install vllm==0.7.0
# !pip install transformers==4.57.6
# !pip install vllm==0.11.0
# #!pip install vllm

#################################
## LLM PART ##
#################################

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
    elif (mode == "no_tddace"):
      print("Using only FInal Answer json.")
      json_schema = onlyFinalAnswer.model_json_schema()
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

class onlyFinalAnswer(BaseModel):
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

  print("This is prompt: -->", prompt, "<--")

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
        elif (prompt.startswith("Complete")):
          print("NO TDDACE DETECTED")
          sampling_params = setup(mode="no_tddace")
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
  print("\n\n-----------------------HALF OF ENTIRE RESPONSE-----------------------")
  print(response[int(-len(response)/2):])
  print("\n\n-----------------------      END    -----------------------")
  # try:
  #   response = response.split("---", 1)[1] # mostly for normistral i believe.
  # except:
  #   print("Not able to split on ---, returning full result")
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


def start():
  if __name__ == "__main__":
    print("Loading...")
    llm = load("gpt_oss_20b" ,"auto", "full", 32768, "0.96")
    samplingparams = setup(mode="no_tddace")
  print("Generating...")
  question = '''
  def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
  '''
  prompt = "Complete this function:" + question
  response = callvLLM(prompt, llm, samplingparams)
  print("Final response: ", response)

# start()
# exit()
# Samples:
list_of_samples = []
list_of_samples.append(["def can_arrange(arr):\n    \"\"\"Create a function which returns the largest index of an element which\n    is not greater than or equal to the element immediately preceding it. If\n    no such element exists then return -1. The given array will not contain\n    duplicate values.\n\n    Examples:\n    can_arrange([1,2,4,3,5]) = 3\n    can_arrange([1,2,3]) = -1\n    \"\"\"\n", "def test_check():\n\n    # Check some simple cases\n    assert can_arrange([1,2,4,3,5])==3\n    assert can_arrange([1,2,4,5])==-1\n    assert can_arrange([1,4,2,5,6,7,8,9,10])==2\n    assert can_arrange([4,8,5,7,3])==4\n\n    # Check some edge cases that are easy to work out by hand.\n    assert can_arrange([])==-1\n\n"])
list_of_samples.append(["def max_fill(grid, capacity):\n    import math\n    \"\"\"\n    You are given a rectangular grid of wells. Each row represents a single well,\n    and each 1 in a row represents a single unit of water.\n    Each well has a corresponding bucket that can be used to extract water from it, \n    and all buckets have the same capacity.\n    Your task is to use the buckets to empty the wells.\n    Output the number of times you need to lower the buckets.\n\n    Example 1:\n        Input: \n            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]\n            bucket_capacity : 1\n        Output: 6\n\n    Example 2:\n        Input: \n            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]\n            bucket_capacity : 2\n        Output: 5\n    \n    Example 3:\n        Input: \n            grid : [[0,0,0], [0,0,0]]\n            bucket_capacity : 5\n        Output: 0\n\n    Constraints:\n        * all wells have the same length\n        * 1 <= grid.length <= 10^2\n        * 1 <= grid[:,1].length <= 10^2\n        * grid[i][j] -> 0 | 1\n        * 1 <= capacity <= 10\n    \"\"\"\n", "def test_check():\n\n\n    # Check some simple cases\n    assert True, \"This prints if this assert fails 1 (good for debugging!)\"\n    assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6, \"Error\"\n    assert max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5, \"Error\"\n    assert max_fill([[0,0,0], [0,0,0]], 5) == 0, \"Error\"\n\n    # Check some edge cases that are easy to work out by hand.\n    assert True, \"This prints if this assert fails 2 (also good for debugging!)\"\n    assert max_fill([[1,1,1,1], [1,1,1,1]], 2) == 4, \"Error\"\n    assert max_fill([[1,1,1,1], [1,1,1,1]], 9) == 2, \"Error\"\n\n"])
list_of_samples.append(["def digits(n):\n    \"\"\"Given a positive integer n, return the product of the odd digits.\n    Return 0 if all digits are even.\n    For example:\n    digits(1)  == 1\n    digits(4)  == 0\n    digits(235) == 15\n    \"\"\"\n", "def test_check():\n\n    # Check some simple cases\n    assert digits(5) == 5\n    assert digits(54) == 5\n    assert digits(120) ==1\n    assert digits(5014) == 5\n    assert digits(98765) == 315\n    assert digits(5576543) == 2625\n\n    # Check some edge cases that are easy to work out by hand.\n    assert digits(2468) == 0\n\n"])
list_of_samples.append(["def fib(n: int):\n    \"\"\"Return n-th Fibonacci number.\n    >>> fib(10)\n    55\n    >>> fib(1)\n    1\n    >>> fib(8)\n    21\n    \"\"\"\n", "\n\nMETADATA = {}\n\n\ndef test_check():\n    assert fib(10) == 55\n    assert fib(1) == 1\n    assert fib(8) == 21\n    assert fib(11) == 89\n    assert fib(12) == 144\n\n"])
list_of_samples.append(["def check_dict_case(dict):\n    \"\"\"\n    Given a dictionary, return True if all keys are strings in lower \n    case or all keys are strings in upper case, else return False.\n    The function should return False is the given dictionary is empty.\n    Examples:\n    check_dict_case({\"a\":\"apple\", \"b\":\"banana\"}) should return True.\n    check_dict_case({\"a\":\"apple\", \"A\":\"banana\", \"B\":\"banana\"}) should return False.\n    check_dict_case({\"a\":\"apple\", 8:\"banana\", \"a\":\"apple\"}) should return False.\n    check_dict_case({\"Name\":\"John\", \"Age\":\"36\", \"City\":\"Houston\"}) should return False.\n    check_dict_case({\"STATE\":\"NC\", \"ZIP\":\"12345\" }) should return True.\n    \"\"\"\n", "def test_check():\n\n    # Check some simple cases\n    assert check_dict_case({\"p\":\"pineapple\", \"b\":\"banana\"}) == True, \"First test error: \" + str(check_dict_case({\"p\":\"pineapple\", \"b\":\"banana\"}))\n    assert check_dict_case({\"p\":\"pineapple\", \"A\":\"banana\", \"B\":\"banana\"}) == False, \"Second test error: \" + str(check_dict_case({\"p\":\"pineapple\", \"A\":\"banana\", \"B\":\"banana\"}))\n    assert check_dict_case({\"p\":\"pineapple\", 5:\"banana\", \"a\":\"apple\"}) == False, \"Third test error: \" + str(check_dict_case({\"p\":\"pineapple\", 5:\"banana\", \"a\":\"apple\"}))\n    assert check_dict_case({\"Name\":\"John\", \"Age\":\"36\", \"City\":\"Houston\"}) == False, \"Fourth test error: \" + str(check_dict_case({\"Name\":\"John\", \"Age\":\"36\", \"City\":\"Houston\"}))\n    assert check_dict_case({\"STATE\":\"NC\", \"ZIP\":\"12345\" }) == True, \"Fifth test error: \" + str(check_dict_case({\"STATE\":\"NC\", \"ZIP\":\"12345\" }))      \n    assert check_dict_case({\"fruit\":\"Orange\", \"taste\":\"Sweet\" }) == True, \"Fourth test error: \" + str(check_dict_case({\"fruit\":\"Orange\", \"taste\":\"Sweet\" }))      \n\n\n    # Check some edge cases that are easy to work out by hand.\n    assert check_dict_case({}) == False, \"1st edge test error: \" + str(check_dict_case({}))\n\n"])
list_of_samples.append(["from typing import List \ndef filter_by_prefix(strings: List[str], prefix: str) -> List[str]:\n    \"\"\" Filter an input list of strings only for ones that start with a given prefix.\n    >>> filter_by_prefix([], 'a')\n    []\n    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')\n    ['abc', 'array']\n    \"\"\"\n", "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef test_check():\n    assert filter_by_prefix([], 'john') == []\n    assert filter_by_prefix(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']\n"])
list_of_samples.append(["def right_angle_triangle(a, b, c):\n    '''\n    Given the lengths of the three sides of a triangle. Return True if the three\n    sides form a right-angled triangle, False otherwise.\n    A right-angled triangle is a triangle in which one angle is right angle or \n    90 degree.\n    Example:\n    right_angle_triangle(3, 4, 5) == True\n    right_angle_triangle(1, 2, 3) == False\n    '''\n", "def test_check():\n\n    # Check some simple cases\n    assert right_angle_triangle(3, 4, 5) == True, \"This prints if this assert fails 1 (good for debugging!)\"\n    assert right_angle_triangle(1, 2, 3) == False\n    assert right_angle_triangle(10, 6, 8) == True\n    assert right_angle_triangle(2, 2, 2) == False\n    assert right_angle_triangle(7, 24, 25) == True\n    assert right_angle_triangle(10, 5, 7) == False\n    assert right_angle_triangle(5, 12, 13) == True\n    assert right_angle_triangle(15, 8, 17) == True\n    assert right_angle_triangle(48, 55, 73) == True\n\n    # Check some edge cases that are easy to work out by hand.\n    assert right_angle_triangle(1, 1, 1) == False, \"This prints if this assert fails 2 (also good for debugging!)\"\n    assert right_angle_triangle(2, 2, 10) == False\n\n"])
list_of_samples.append(["def remove_vowels(text):\n    \"\"\"\n    remove_vowels is a function that takes string and returns string without vowels.\n    >>> remove_vowels('')\n    ''\n    >>> remove_vowels(\"abcdef\\nghijklm\")\n    'bcdf\\nghjklm'\n    >>> remove_vowels('abcdef')\n    'bcdf'\n    >>> remove_vowels('aaaaa')\n    ''\n    >>> remove_vowels('aaBAA')\n    'B'\n    >>> remove_vowels('zbcd')\n    'zbcd'\n    \"\"\"\n", "\n\nMETADATA = {}\n\n\ndef test_check():\n    assert remove_vowels('') == ''\n    assert remove_vowels(\"abcdefghijklm\") == 'bcdfghjklm'\n    assert remove_vowels('fedcba') == 'fdcb'\n    assert remove_vowels('eeeee') == ''\n    assert remove_vowels('acBAA') == 'cB'\n    assert remove_vowels('EcBOO') == 'cB'\n    assert remove_vowels('ybcd') == 'ybcd'\n\n"])
list_of_samples.append(["def words_string(s):\n    \"\"\"\n    You will be given a string of words separated by commas or spaces. Your task is\n    to split the string into words and return an array of the words.\n    \n    For example:\n    words_string(\"Hi, my name is John\") == [\"Hi\", \"my\", \"name\", \"is\", \"John\"]\n    words_string(\"One, two, three, four, five, six\") == [\"One\", \"two\", \"three\", \"four\", \"five\", \"six\"]\n    \"\"\"\n", "def test_check():\n\n    # Check some simple cases\n    assert True, \"This prints if this assert fails 1 (good for debugging!)\"\n    assert words_string(\"Hi, my name is John\") == [\"Hi\", \"my\", \"name\", \"is\", \"John\"]\n    assert words_string(\"One, two, three, four, five, six\") == [\"One\", \"two\", \"three\", \"four\", \"five\", \"six\"]\n    assert words_string(\"Hi, my name\") == [\"Hi\", \"my\", \"name\"]\n    assert words_string(\"One,, two, three, four, five, six,\") == [\"One\", \"two\", \"three\", \"four\", \"five\", \"six\"]\n\n    # Check some edge cases that are easy to work out by hand.\n    assert True, \"This prints if this assert fails 2 (also good for debugging!)\"\n    assert words_string(\"\") == []\n    assert words_string(\"ahmed     , gamal\") == [\"ahmed\", \"gamal\"]\n\n"])
list_of_samples.append(["def order_by_points(nums):\n    \"\"\"\n    Write a function which sorts the given list of integers\n    in ascending order according to the sum of their digits.\n    Note: if there are several items with similar sum of their digits,\n    order them based on their index in original list.\n\n    For example:\n    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]\n    >>> order_by_points([]) == []\n    \"\"\"\n", "def test_check():\n\n    # Check some simple cases\n    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]\n    assert order_by_points([1234,423,463,145,2,423,423,53,6,37,3457,3,56,0,46]) == [0, 2, 3, 6, 53, 423, 423, 423, 1234, 145, 37, 46, 56, 463, 3457]\n    assert order_by_points([]) == []\n    assert order_by_points([1, -11, -32, 43, 54, -98, 2, -3]) == [-3, -32, -98, -11, 1, 2, 43, 54]\n    assert order_by_points([1,2,3,4,5,6,7,8,9,10,11]) == [1, 10, 2, 11, 3, 4, 5, 6, 7, 8, 9]\n    assert order_by_points([0,6,6,-76,-21,23,4]) == [-76, -21, 0, 4, 23, 6, 6]\n\n    # Check some edge cases that are easy to work out by hand.\n    assert True, \"This prints if this assert fails 2 (also good for debugging!)\"\n\n"])

# Pytest + Pylint
def check_code_quality(filename):
        print("Checking code quality for: ", filename)
        import subprocess

        result = subprocess.run(
            [
                "pylint",
                filename,
                "-v"
            ],
            capture_output=True,
            text=True,
            timeout=30
        )

        print("=========== CODE QUALITY ==========")
        print(result)
        print("=========== END ==========")

        # print("Exit code:", result.returncode)
        # print("STDOUT:")
        # print(result.stdout)
        # print("STDERR:")
        # print(result.stderr)

        import re
        match = re.findall(r'Your code has been rated at (\d+(?:\.\d+)?/\d+)', str(result))
        resultcode = "error"
        # print("--->", result.split("=========================")[-2], "<---")
        resultscore = "Not found"
        if len(match)!=0:
            print("->", match)
            print("->", match[-1])
            resultscore = match[-1]
        return resultscore, result


def _humaneval_answer_is_correct(filename: str) -> bool:

        test = False
        # if (predicted.startswith("THISISTEST")):
        #     print("IN THE TEST PHASE")
        #     predicted = predicted.split("THISISTEST")[1]
        #     test = True
        print("RUNNING CODECHECKER")
        import subprocess

        result = subprocess.run(
                    [
                "python",
                "./containers/codechecker.py",
            ],
            capture_output=True,
            text=True,
            timeout=30
        )
        result = str(result)
        print("DONE, WE SHOULD GET OUTPUT HERE: ", result)
        import re
        match = re.findall(r'==*\s*(.*?)\s*==\s*', result.strip())
        resultcode = "error"
        # print("--->", result.split("=========================")[-2], "<---")
        if len(match)!=0:
            print("->", match)
            index = -1
            for i in range(len(match)-1, 0, -1):
                print(match[i])
                if (match[i]!=""):
                    index = i
                    break
            print("-->", match[index])
            resultcode = match[index]
        print("--->", resultcode, "<---")
        # if ("failed" in result.split("=========================")[-2]):
        if test:
            if ("failed" in resultcode):
                print("FAIL")
                return False, ""
            else: # NEED OPTION FOR IF ERROR IN RESULT.
                print("PASS")
                return True, result
        else:
            if (any(x in resultcode for x in ["failed", "errors", "error"])):
                print("FAIL")
                return False, result
            else: # NEED OPTION FOR IF ERROR IN RESULT.
                print("PASS")
                return True, ""

def extract_filename(file):
  question = file
  print("Received Question: ", question)
  question_name = ""
  import re
  matches = re.findall(r'def\s*([^(]*)', question) 
  if matches:
      question_name = matches[0]
      question_name = question_name.split(" ")[-1]
  question_name_pure = question_name
  question_name_with_param = question_name + question.split(question_name)[1].split("):")[0] + "):"
  # question_name = "test_"+question_name + "ACEFILENAME"
  question_name = "test_"+question_name
  print("ACEFILENAME: ", question_name, question_name_pure, question_name_with_param)
  return question_name, question_name_pure, question_name_with_param

def save_file(content, filename):
  predicted = content
  print("Saving file: ", filename)
  # predicted = predicted.strip("\n").strip("}")
  predicted = predicted.strip("}").strip("\\n").strip("}")
  print("THIS IS FUNCTION: -->", predicted, "<--")
  # import re
  # matches = re.findall(r'def\s*([^(]*)', predicted) 
  # filename = "./workspace/tests/test_15.py"
  # if matches:
  #     filename = matches[-1]
  #     filename = "./workspace/tests/" + filename.split(" ")[-1] + ".py"
  # filename = "./workspace/tests/" + predicted.split("ACEFILENAME")[0]  + ".py"
  filename = "./workspace/tests/" + filename  + ".py"
  # predicted = predicted.split("ACEFILENAME")[1]
  print("SAVING TEST TO .PY FILE: ", filename)
  predicted = content
  predicted+="\n\n"
  # First save predicted answer/test in a folder workspace/test.py
  predicted = bytes(predicted, "utf-8").decode("unicode_escape")
  mode = "test"
  if (mode == "test"):
      with open(filename, "w", encoding="utf-8") as file:
          file.write(predicted)
  elif (mode == "function"):
      with open(filename, "a", encoding="utf-8") as file:
          file.write(predicted)
  
  return filename

def add_reference_test(content, file):
  print("Adding reference test")
  full_file = file + "\n\n" + content
  return full_file

def move_file(filename):
  print("Moving file: ", filename)
  print("Moving files:")
  basepath = "./workspace/tests/"
  newpath = "./workspace/done/"+filename
  print(basepath, newpath)
  from shutil import move
  import os
  if not os.path.exists(newpath):
      os.makedirs(newpath)
  file_names = os.listdir(basepath)
      
  for file_name in file_names:
      if (file_name.endswith(".py")):
          print(file_name)
          move(basepath+file_name, newpath+"/"+file_name)

def save_results(question_name_pure, code_quality_score, is_correct):
  print("Saving results")
  with open("./baseline_results.txt", "a", encoding="utf-8") as file:
          file.write(f"\n=== {question_name_pure} ===\n")
          file.write(f"Code quality score: {code_quality_score}\n")
          file.write(f"Function passed tests: {is_correct}\n")

def extract_json_part(text):
  if text.startswith("_answer"):
    print("_answer yes")
    text = '{"final_answer":' + text.split("_answer", 1)[-1].split(":", 1)[-1]
    # text = text.replace("_answer", '{"final_answer')
  if text.__contains__("assistantfinal_answer"):
    print("assistantfinal_answer yes")
    text = '{"final_answer":' + text.split("assistantfinal_answer", 1)[-1].split(":", 1)[-1]
  import json
  if ("{" in text):
    text = "{"+text.split("{", 1)[-1]
    try:
        # First try JSON parsing
        parsed = json.loads(text)
        answer = str(parsed.get("final_answer", "No final answer found"))
        print("FINAL ANSWER 1")
        return answer  
            
    except (json.JSONDecodeError, KeyError, AttributeError) as e:
      print("Json parsing failed...", e)
  if text.startswith("code"):
    print("Begins with code yes.")
    text = text[4:]
    return text
  return text


def run():
  # Setup
  if __name__ == "__main__":
    print("Loading...")
    llm = load("gpt_oss_20b" ,"auto", "full", 32768, "0.96")
    samplingparams = setup(mode="no_tddace")

  with open("./baseline_results.txt", "w", encoding="utf-8") as file:
        file.write("\n========= RESULTS =========\n")
  # Loop
  for item in list_of_samples:
    # Parse question
    question = item[0]
    tests = item[1]
    print("Question: ", question)
    print("Tests: ", tests)

    # Run LLM
    response = callvLLM("Complete this function and output only the working function implementation (No main function, no tests, just the function code): \n" + question + '\n\n **Answer only in this exact JSON format:** {"final_answer": "[Your concise final function/method here]"}', llm, samplingparams)
    print("Final response: ", response)
    response = extract_json_part(response.strip())
    print("Code: ", response)
    
    # Get filename
    question_name, question_name_pure, question_name_with_param = extract_filename(file=question)
    
    # Inject reference tests
    full_file = add_reference_test(content=tests, file=response)
    
    # Save file
    filename = save_file(content=full_file, filename=question_name)

    # Pylint
    code_quality_score, code_quality_report = check_code_quality(filename=filename)

    # Pytest
    is_correct, pytestreport = _humaneval_answer_is_correct(filename=filename)

    # Move files
    move_file(filename=question_name_pure)

    save_results(question_name_pure=question_name_pure, code_quality_score=code_quality_score, is_correct=is_correct)

run()
