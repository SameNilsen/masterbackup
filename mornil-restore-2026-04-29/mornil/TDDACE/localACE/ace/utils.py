#!/usr/bin/env python3
import os
import re
import json
#import openai
import tiktoken
from dotenv import load_dotenv
from typing import List, Dict, Any, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
#from localLLM import setupLLM
# from localLLMqwen import setupLLM

# Load environment variables from .env file
load_dotenv()

def initialize_clients(api_provider, generator_model, args):

    ## FOR API, WE DONT WANT THAT, WE WANT LOCAL MODELS.
    
    # """Initialize separate clients for generator, reflector, and curator"""
    # if api_provider == "sambanova":
    #     # Use SambaNova API
    #     base_url = "https://api.sambanova.ai/v1"
    #     api_key = os.getenv('SAMBANOVA_API_KEY', '')
    #     if not api_key:
    #         raise ValueError("SambaNova api key not found in environment variables")
    # elif api_provider == "together":
    #     # Use Together API
    #     base_url = "https://api.together.xyz/v1"
    #     api_key = os.getenv('TOGETHER_API_KEY', '')
    #     if not api_key:
    #         raise ValueError("Together api key not found in environment variables")
    # elif api_provider == "openai":
    #     # Use OpenAI API
    #     base_url = "https://api.openai.com/v1"
    #     api_key = os.getenv('OPENAI_API_KEY', '')
    #     if not api_key:
    #         raise ValueError("OpenAI api key not found in environment variables")
    # else:
    #     raise ValueError((f"Invalid api_provider name: {api_provider}. Must be 'sambanova', 'together', or 'openai'"))
        
    # generator_client = openai.OpenAI(api_key=api_key, base_url=base_url)
    # reflector_client = openai.OpenAI(api_key=api_key, base_url=base_url)
    # curator_client = openai.OpenAI(api_key=api_key, base_url=base_url)
    
    #print("Using Together API for all models")

    print("Setup LLM...")
    samplingparams = None
    tokenizer = None
    model = None
    llm = None
    if (args.inference_provider == "vllm"):
        # global vLLM_configurable, llm, samplingparams
        print("starting setup of vllm")
        import vLLM_configurable
        # if __name__ == "__main__":
        print("Soon there...")
        llm = vLLM_configurable.load(model_name=args.generator_model ,dtype=args.dtype, quantization=args.quantization, model_length=args.model_length, gpu_memory_utilization=args.gpu_usage)
        samplingparams = vLLM_configurable.setup()
        print("yey")
    elif (args.generator_model == "normistral11b_thinking" and args.inference_provider == "transformers"):
        if (args.inference_provider == "transformers"):
            # global normistral11b_configurable
            import normistral11b_configurable
            normistral11b_configurable.setupLLM(quantization=args.quantization, model_length=args.model_length, dtype=args.dtype)
    elif ((args.generator_model == "gpt_oss_20b" or args.generator_model == "gpt_oss_120b") and args.inference_provider == "transformers"):
        # global gpt_oss_configurable, tokenizer, generator_model
        import gpt_oss_configurable
        tokenizer, model = gpt_oss_configurable.setupLLM(model=args.generator_model)
    else:
        print(f"Model {generator_model} not recognized for local setup. Defaulting to Qwen3-8B.")
        from localLLMqwen import setupLLM
        setupLLM()
    print("LLM finished setting up.")

    # print("utils.py: USING LOCAL MODELS: ", generator_model)
    # if (generator_model == "Qwen3-8B"):
    #     from localLLMqwen import setupLLM
    # elif (generator_model == "normistral-11b-thinking"):
    #     from localLLM import setupLLM
    # else:
    #     print(f"Model {generator_model} not recognized for local setup. Defaulting to Qwen3-8B.")
    #     from localLLMqwen import setupLLM
    # setupLLM()

    # model_name='norallm/normistral-7b-warm-instruct'
    model_name = generator_model
    generator_client, reflector_client, curator_client = model_name, model_name, model_name
    return generator_client, reflector_client, curator_client, samplingparams, tokenizer, model, llm

def get_section_slug(section_name):
    """Convert section name to slug format (3-5 chars)"""
    # Common section mappings - updated to match original sections
    slug_map = {
        "financial_strategies_and_insights": "fin",
        "formulas_and_calculations": "calc",
        "code_snippets_and_templates": "code",
        "common_mistakes_to_avoid": "err",
        "problem_solving_heuristics": "prob",
        "context_clues_and_indicators": "ctx",
        "others": "misc",
        "meta_strategies": "meta"
    }
    
    # Clean and convert to snake_case
    clean_name = section_name.lower().strip().replace(" ", "_").replace("&", "and")
    
    if clean_name in slug_map:
        return slug_map[clean_name]
    
    # Generate slug from first letters
    words = clean_name.split("_")
    if len(words) == 1:
        return words[0][:4]
    else:
        return "".join(w[0] for w in words[:5])

def extract_boxed_content(text):
    """Helper function to extract content from \\boxed{} format"""
    pattern = r'\\boxed\{'
    match = re.search(pattern, text)
    if not match:
        return None
    
    start = match.end() - 1  # Position of opening brace
    brace_count = 0
    i = start
    
    while i < len(text):
        if text[i] == '{':
            brace_count += 1
        elif text[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                return text[start + 1:i]  # Content between braces
        i += 1
    return None

def extract_answer(response):
    """Extract final answer from model response"""
    response = str(response)
    # print("ANSWER TO BE PARSED: ", response)
    try:
        # First try JSON parsing
        parsed = json.loads(response)
        answer = str(parsed.get("final_answer", "No final answer found"))
        print("FINAL ANSWER 1")
        return answer  
            
    except (json.JSONDecodeError, KeyError, AttributeError):
        # JSON parsing failed, use fallback logic
        matches = re.findall(r"Finish\[(.*?)\]", response)
        if matches:
            answer = matches[-1]
            print("FINAL ANSWER 2")
            return answer
        
        # Try to get final answer from JSON style response with regex matching 
        # Try double quotes first
        # matches = re.findall(r'"final_answer"\s*:\s*"([^"]*)"', response)
        matches = re.findall(r'"final_answer"\s*:\s*"((?:\\.|[^"\\])*)"', response) # New regex, to capture entire function.
        if matches:
            answer = matches[-1]
            print("FINAL ANSWER 3")
            return answer
        
        # Try single quotes
        matches = re.findall(r"'final_answer'\s*:\s*'([^']*)'", response)
        if matches:
            answer = matches[-1]
            print("FINAL ANSWER 4")
            return answer
        
        # Handle JSON format without quotes (for simple expressions)
        matches = re.findall(r'[\'"]final_answer[\'"]\s*:\s*"([^}]+)"', response)
        if matches:
            answer = matches[-1].strip()
            # Clean up trailing characters
            answer = re.sub(r'[,}]*$', '', answer)
            print("FINAL ANSWER 5")
            return answer
        matches = re.findall(r'final_answer\\":\s*\\"(.*?)\\"\}', response) # New regex, to capture entire function.
        if matches:
            answer = matches[-1]
            print("FINAL ANSWER 8")
            # print(answer)
            return answer
        matches = re.findall(r'final_answer\\":\s*\\"(.*?)"\}', response) # New regex, to capture entire function.
        if matches:
            answer = matches[-1]
            print("FINAL ANSWER 9")
            # print(answer)
            return answer
        matches = re.findall(r'final_answer\\":\s*\\"((?:\\\\.|(?!"\})[\s\S])*)"\}', response) # New regex, to capture entire function.
        if matches:
            answer = matches[-1]
            print("FINAL ANSWER 10")
            # print(answer)
            return answer
        # Try to capture "final_answer\:"
        matches = re.findall(r'"final_answer\\":\s*\\"((?:\\\\.|[^"\\])*)\\"', response)
        if matches:
            answer = matches[-1]
            print("FINAL ANSWER 11")
            # print(answer)
            return answer
        
        # Fallback for "The final answer is: X" pattern with boxed
        final_answer_pattern = r'[Tt]he final answer is:?\s*\$?\\boxed\{'
        match = re.search(final_answer_pattern, response)
        if match:
            # Extract boxed content starting from this match
            remaining_text = response[match.start():]
            boxed_content = extract_boxed_content(remaining_text)
            if boxed_content:
                print("FINAL ANSWER 6")
                return boxed_content
        
        # More general pattern for "final answer is X"
        matches = re.findall(r'[Tt]he final answer is:?\s*([^\n.]+)', response)
        if matches:
            answer = matches[-1].strip()
            # Clean up common formatting
            answer = re.sub(r'^\$?\\boxed\{([^}]+)\}\$?$', r'\1', answer)
            answer = answer.replace('$', '').strip()
            if answer:
                print("FINAL ANSWER 7")
                return answer
        
        return "No final answer found"
    
enc = tiktoken.get_encoding("cl100k_base")
def count_tokens(prompt: str) -> int:
   return len(enc.encode(prompt))


def _save_test_or_function(mode, predicted):
    predicted = predicted.strip("\n").strip("}")
    print("THIS IS FUNCTION: -->", predicted, "<--")
    filename = "./workspace/tests/test_15.py"
    filename = "./workspace/tests/" + predicted.split("ACEFILENAME")[0]  + ".py"
    predicted = predicted.split("ACEFILENAME")[1]
    print("SAVING TEST TO .PY FILE: ", filename)
    predicted+="\n\n"
    # First save predicted answer/test in a folder workspace/test.py
    predicted = bytes(predicted, "utf-8").decode("unicode_escape")
    if (mode == "test"):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(predicted)
    elif (mode == "function"):
        with open(filename, "a", encoding="utf-8") as file:
            file.write(predicted)
    
    return predicted


def evaluate_single_test_sample(args_tuple, data_processor) -> Tuple[Dict, str]:
    """
    Evaluate a single test sample - task-agnostic implementation.
    
    Args:
        args_tuple: Tuple of (index, task_dict, generator, playbook, max_tokens, log_dir, use_json_mode)
        data_processor: DataProcessor instance with answer_is_correct method
    """
    (i, task_dict, generator, playbook, max_tokens, log_dir, use_json_mode) = args_tuple
    try:
        context = task_dict["context"]
        question = task_dict["question"]
        target = task_dict["target"]
        print(31)
        # gen_response, bullet_ids, call_info = generator.generate(
        #     question=question,
        #     playbook=playbook,
        #     context=context,
        #     reflection="(empty)",
        #     use_json_mode=use_json_mode,
        #     call_id=f"test_eval_{i}",
        #     log_dir=log_dir
        # )
        # print(32)
        # final_answer = extract_answer(gen_response)
        # is_correct = data_processor.answer_is_correct(final_answer, target)

        print("\n - EVAL SINGLE TEST SAMPLE - \n")
        print("Context: ", context, "Question: ", question, " \nTarget: ", target)
        question_name = ""
        import re
        matches = re.findall(r'def\s*([^(]*)', question) 
        if matches:
            question_name = matches[0]
            question_name = question_name.split(" ")[-1]
        imports = ""
        if question.split("def", 1)[0].__contains__("import"):
            imports = question.split("def", 1)[0].strip()
        print("Imports: ", imports)
        question_name_pure = question_name
        question_name_with_param = question_name + question.split(question_name)[1].split("):")[0] + "):"
        question_name = "test_"+question_name + "ACEFILENAME"
        print("ACEFILENAME ", question_name, question_name_pure, question_name_with_param)
        # print("Moving files:")
        basepath = "./workspace/tests/"
        newpath = "./workspace/done/"+question_name_pure
        print(basepath, newpath)
        from shutil import move
        import os
        # if not os.path.exists(newpath):
        #     os.mkdir(newpath)
        # file_names = os.listdir(basepath)
            
        # for file_name in file_names:
        #     if (file_name.endswith(".py")):
        #         print(file_name)
        #         move(basepath+file_name, newpath+"/"+file_name)
        print("\n\n Still in initial testing, creating tests...")
        question_name = "test_initial_"+question_name
        context = ""
        print("ACEFILENAME")
        gen_response, bullet_ids, call_info = generator.generate(
            question=question,
            playbook=playbook,
            context=context,
            reflection="(empty)",
            use_json_mode=use_json_mode,
            call_id=f"test_eval_{i}",
            log_dir=log_dir
        )
        
        # Extract answer and check correctness
        final_answer = extract_answer(gen_response)
        final_answer = _save_test_or_function("test", question_name+final_answer)
        is_correct, feedback = data_processor.answer_is_correct(final_answer, target)
        pre_train_post_curator_answer = final_answer
        
        print(f"Correct: {is_correct}")

        reflection_content = "(empty)"

        if is_correct:
            is_correct = False
        else:
            is_correct = True # A bit confusing, but if tests fail, thats correct.
 
        context = "GENERATE_FUNCTION"+pre_train_post_curator_answer
        # Then function implementation
        print("\n\n Now creating function.")
        gen_response, _, _ = generator.generate(
            question=question,
            playbook=playbook,
            context=context,
            reflection="(empty)",
            use_json_mode=use_json_mode,
            call_id=f"test_eval_{i}_post_curate_function",
            log_dir=log_dir
        )
        
        final_answer = extract_answer(gen_response)
        if imports != "":
            final_answer = imports+"\n"+final_answer
        final_answer = _save_test_or_function("function", question_name+final_answer)
        post_train_answer = final_answer
        
        post_train_is_correct, feedback = data_processor.answer_is_correct(final_answer, target)

        print("Now checking code quality:")
        filename_qualityscore = "./workspace/tests/test_initial_test_"+question_name_pure+".py"
        print(f"filename_qualityscore: {filename_qualityscore}")
        code_quality_score, code_quality_report = data_processor.check_code_quality(filename_qualityscore)
        print(f"CODE QUALITY SCORE FOR {question_name_pure}: {code_quality_score}")
        code_quality_report = str(code_quality_report)

        # Cheking function against reference tests:
        reference_tests_answer = _save_test_or_function("function", question_name+("".join(target[1:]).replace("def ", "def test_", 1).replace("(candidate)", "()").replace("candidate", question_name_pure))+"\n\n")

        if data_processor.answer_is_correct(reference_tests_answer, target)[0]:
            print(f"Correctly implemented function according to reference functions as well!")
            is_correct = True
            # break
        else:
            print("Reference tests failed...")
            is_correct = False

        print("Moving files:")
        basepath = "./workspace/tests/"
        newpath = "./workspace/done/"+question_name_pure+"/initial"
        print(basepath, newpath)
        from shutil import move
        import os
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        else:
            newpath = "./workspace/done/"+question_name_pure+"/final"
            os.makedirs(newpath)
        file_names = os.listdir(basepath)
            
        for file_name in file_names:
            if (file_name.endswith(".py")):
                print(file_name)
                move(basepath+file_name, newpath+"/"+file_name)
        
        with open("./workspace/done/"+question_name_pure+"/codequality.txt", "a", encoding="utf-8") as file:
            if (newpath.endswith("initial")):
                file.write(f"INITIAL CODE QUALITY SCORE FOR {question_name_pure}: {code_quality_score} | Passed test: {is_correct}")
            else:
                with open("./workspace/done/"+question_name_pure+"/codequality.txt", "r", encoding="utf-8") as file2:
                    prev = file2.read()
                init_passed = prev.split(":")[-1].strip()
                if ("Not found" in prev):
                    # prev = "0.0/10"
                    print("prev not found i")
                else:
                    # prev = float(prev.split(":")[-1].split("/")[0])
                    prev = prev.split(":")[1].split("|")[0].strip()
                with open("./workspace/done/metrics.txt", "a", encoding="utf-8") as metricsfile:
                    if ("Not found" in code_quality_score):
                        # code_quality_score = "0.0/10"
                        print("prev not found f")
                    metricsfile.write(f"\n=== {question_name_pure} ===\n")
                    metricsfile.write(f"Initial code quality: {prev} Final code quality: {code_quality_score} | Initially passed test: {init_passed} Finally passed test: {is_correct}\n")
                file.write(f"\nFINAL CODE QUALITY SCORE FOR {question_name_pure}: {code_quality_score} | Passed test: {is_correct}\n")

        return {
            "index": i,
            "final_answer": final_answer,
            "target": target,
            "is_correct": is_correct,
            "success": True
        }, None

    except Exception as e:
        return None, f"Error evaluating sample {i}: {type(e).__name__}: {str(e)}"


def evaluate_test_set(data_processor, generator, playbook, test_samples,
                      max_tokens=4096, log_dir=None, max_workers=20, 
                      use_json_mode=False) -> Tuple[Dict, Dict]:
    """
    Parallel evaluation of test set - task-agnostic implementation.
    
    Args:
        data_processor: DataProcessor instance with answer_is_correct and evaluate_accuracy methods
        generator: Generator instance
        playbook: Current playbook string
        test_samples: List of test samples
        max_tokens: Max tokens for generation
        log_dir: Directory for logs
        max_workers: Number of parallel workers
        use_json_mode: Whether to use JSON mode
        
    Returns:
        Tuple of (results_dict, error_logs_dict)
    """
    print(f"\n{'='*40}")
    max_workers = 1
    print(f"EVALUATING TEST SET - {len(test_samples)} samples, {max_workers} workers")
    print(f"{'='*40}")

    args_list = [
        (i, sample, generator, playbook, max_tokens, log_dir, use_json_mode)
        for i, sample in enumerate(test_samples)
    ]

    results = {
        "correct": 0, "total": 0, "no_answer": 0,
        "answers": [], "targets": [], "errors": []
    }

    # Use a wrapper to pass data_processor to the evaluation function
    def eval_wrapper(args_tuple):
        return evaluate_single_test_sample(args_tuple, data_processor)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_args = {
            executor.submit(eval_wrapper, args): args 
            for args in args_list
        }

        for i, future in enumerate(as_completed(future_to_args), 1):
            result, error = future.result()
            
            if error:
                print(error)
                continue

            if result and result["success"]:
                results["correct"] += (1 if result["is_correct"] else 0)
                results["total"] += 1
                results["answers"].append(result["final_answer"])
                results["targets"].append(result["target"])
                
                if not result["is_correct"]:
                    results["errors"].append({
                        "index": result["index"],
                        "prediction": result["final_answer"],
                        "ground_truth": result["target"]
                    })
                
                if result["final_answer"] == "No final answer found":
                    results["no_answer"] += 1

            if i % 50 == 0:
                curr_acc = results["correct"] / results["total"] if results["total"] > 0 else 0
                print(f"Progress: {i}/{len(args_list)}, Accuracy: {curr_acc:.3f}")
    
    if results["answers"] and results["targets"]:
        #accuracy = data_processor.evaluate_accuracy(results["answers"], results["targets"])
        try:
            accuracy = results['correct']/results['total'] if results["total"] > 0 else 0
        except:
            accuracy = 0.0
        print("ACCURACY=", accuracy)
        final_results = {
            "accuracy": accuracy,
            "correct": results["correct"],
            "total": results["total"],
            "no_answer": results["no_answer"]
        }
        
        error_logs = {
            "accuracy": accuracy,
            "errors": results["errors"]
        }
        print("final results: ", final_results)
        print(f"\n📊 Final Accuracy: {accuracy:.3f} ({results['correct']}/{results['total']})")
    else:
        results = {"accuracy": 0.0, "correct": 0, "total": 0}
        error_logs = {}
        print(f"\n📊 No valid results!")
        
    return final_results, error_logs