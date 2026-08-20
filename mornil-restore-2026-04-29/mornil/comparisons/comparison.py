import time
#import localLLM

import subprocess as sp
import sys
from threading import Timer
import datetime

running = True

def get_total_gpu_memory():
    output_to_list = lambda x: x.decode('ascii').split('\n')[:-1]
    COMMAND = "nvidia-smi --query-gpu=memory.total --format=csv"
    try:
        memory_total_info = output_to_list(sp.check_output(COMMAND.split(),stderr=sp.STDOUT))[1:]
    except sp.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    memory_total_values = [int(x.split()[0]) for i, x in enumerate(memory_total_info)]
    # print(memory_total_values)
    return memory_total_values

def get_gpu_utilization():
    output_to_list = lambda x: x.decode('ascii').split('\n')[:-1]
    COMMAND = "nvidia-smi --query-gpu=utilization.gpu --format=csv"
    try:
        gpu_utilization_info = output_to_list(sp.check_output(COMMAND.split(),stderr=sp.STDOUT))[1:]
    except sp.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    gpu_utilization_values = [int(x.split()[0]) for i, x in enumerate(gpu_utilization_info)]
    # print(gpu_utilization_values)
    return gpu_utilization_values

def get_power_draw():
    output_to_list = lambda x: x.decode('ascii').split('\n')[:-1]
    COMMAND = "nvidia-smi --query-gpu=power.draw --format=csv"
    try:
        power_draw_info = output_to_list(sp.check_output(COMMAND.split(),stderr=sp.STDOUT))[1:]
    except sp.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    power_draw_values = [float(x.split()[0]) for i, x in enumerate(power_draw_info)]
    # print(power_draw_values)
    return power_draw_values

def get_gpu_memory():
    output_to_list = lambda x: x.decode('ascii').split('\n')[:-1]
    COMMAND = "nvidia-smi --query-gpu=memory.used --format=csv"
    try:
        memory_use_info = output_to_list(sp.check_output(COMMAND.split(),stderr=sp.STDOUT))[1:]
    except sp.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    memory_use_values = [int(x.split()[0]) for i, x in enumerate(memory_use_info)]
    # print(memory_use_values)
    return memory_use_values


def print_gpu_memory_every_5secs():
    """
        This function calls itself every 5 secs and print the gpu_memory.
    """
    if running is False:
        return
    print("starting: print_gpu_memory_every_5secs")
    Timer(5.0, print_gpu_memory_every_5secs).start()
    print(get_gpu_memory())



def stubAskLLM(query):
    print("Asking LLM...")
    # time.sleep(10)
    # result = localLLM.askLLM(query)
    result = normistral_vllm_2.callvLLM(query, llm, samplingparams)
    # result = "boopadipa"+query
    return result

listOfPrompts = {
        "prompt1": "What is 2+2?", 
        "prompt2": "What is the capital of France?", 
        "prompt3": "What is the meaning of life?", 
        "prompt4": "How many continents are there on Earth?", 
        "prompt5": "How are you doing today?",
        "prompt6": "Which city is the Eiffel Tower located in?", 
        "prompt7": "How many legs does a spider have?", 
        "prompt8": "What is the largest mammal?", 
        "prompt9": "What is the chemical symbol for water?", 
        "prompt10": "Who is the current president of the United States?"}

listOfPrompts2 = {
    "prompt11": "What is 5+3?",
    "prompt12": "What is the capital of Spain?",
    "prompt13": "What color is the sky on a clear day?",
    "prompt14": "How many days are there in a week?",
    "prompt15": "How do you say hello in English?",
    "prompt16": "Which planet is known as the Red Planet?",
    "prompt17": "How many wheels does a bicycle have?",
    "prompt18": "What is the smallest prime number?",
    "prompt19": "What do bees produce?",
    "prompt20": "Who wrote the play Romeo and Juliet?"
}

def makeRequest(promptnr, query, timer_log, response_log):
    print(f"MakeRequest called with promptnr {promptnr} and query {query}")
    start = time.perf_counter()
    starttime = str(datetime.datetime.now())
    #result = localLLM.callLLM(query)
    # time.sleep(1)
    #### CALL GET GPU USAGE EVERY 3 SECONDS IN A SEPARATE THREAD, LOG TO FILE.
    gpu_usage_values = []
    gpu_utilization_values = []
    power_draw_values = []
    with ThreadPoolExecutor(max_workers=5) as exe:
        future = exe.submit(stubAskLLM, query)
        while not future.done():
            print(promptnr+": Waiting for LLM response...")
            time.sleep(3)
            gpu_usage_values.append(get_gpu_memory())
            gpu_utilization_values.append(get_gpu_utilization())
            power_draw_values.append(get_power_draw())
    result = future.result()
    endtime = str(datetime.datetime.now())
    # result = stubAskLLM(query)
    
    # result = "boopadipa"+query
    with open(response_log, "a") as f:
        f.write("\n"+promptnr + " of the 10 requests: \nQuery: " + query + "\nResponse: " + result + "\n")
    end = time.perf_counter()
    with open(timer_log, "a") as f:
        f.write("\n"+promptnr + " of the 10 requests: \nTime taken for comparisons: " + str(end - start) + " seconds.\n Starttime: " + starttime + " Endtime: " + endtime + "\nWith GPU memory usage values (MiB): " + str(gpu_usage_values) + "\nGPU utilization values (%): " + str(gpu_utilization_values) + "\nPower draw values (W): " + str(power_draw_values) + "\n")

def vLLMsimultaneousRequests():
    timer_log = "comparisons_vllm_simultaneous.txt"
    response_log = "comparisons_vllm_simultaneous_output_log.txt"
    initial_loaded_gpu_mem = get_gpu_memory()
    print("Get initial GPU memory: ", initial_loaded_gpu_mem)
    with open(timer_log, "w") as f:
        f.write("--- Starting comparisons --- \n")
        f.write("Initial GPU memory loaded: " + str(initial_loaded_gpu_mem) + " MiB\nOf total GPU memory: " + str(get_total_gpu_memory()) + " MiB\n")
    
    with open(response_log, "w") as f:
        f.write("--- Starting logging responses --- \n")

    print("Starting comparisons.")
    print("Doing 10 requests...")
    startTotal = time.perf_counter()

    newList=[]
    for key, value in listOfPrompts2.items():
        newList.append(value)
    responses = normistral_vllm_2.makeSimultaneousvLLMRequest(newList, llm, samplingparams)
    endTotal = time.perf_counter()

    with open(timer_log, "a") as f:
            f.write("\nIn total for 10 requests: Time taken for comparisons: " + str(endTotal - startTotal) + " seconds.\n")
    with open(response_log, "a") as f:
        for output in responses:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            # print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
            f.write("\n\nQuery: " + prompt + "\nResponse: " + generated_text + "\n")

def comparisonsNoThreading():
    timer_log = "comparisons.txt"
    response_log = "comparisons_output_log.txt"
    initial_loaded_gpu_mem = get_gpu_memory()
    print("Get initial GPU memory: ", initial_loaded_gpu_mem)
    with open(timer_log, "w") as f:
        f.write("--- Starting comparisons --- \n")
        f.write("Initial GPU memory loaded: " + str(initial_loaded_gpu_mem) + " MiB\nOf total GPU memory: " + str(get_total_gpu_memory()) + " MiB\n")
    
    with open(response_log, "w") as f:
        f.write("--- Starting logging responses --- \n")

    print("Starting comparisons.")

    print("1 request, baseline...")
    makeRequest("promptBaseline", "Which city is the Eiffel Tower located in?", timer_log, response_log)

    print("Doing 10 requests...")
    startTotal = time.perf_counter()
    for prompt in listOfPrompts.keys():
        query = listOfPrompts[prompt]
        print(f"Handling {prompt} with query {query}...")
        makeRequest(prompt, query, timer_log, response_log)
    endTotal = time.perf_counter()
    with open(timer_log, "a") as f:
            f.write("\nIn total for 10 requests: Time taken for comparisons: " + str(endTotal - startTotal) + " seconds.\n")


from concurrent.futures import ThreadPoolExecutor

def cube(x):
    print("in cube")
    return x*x*x
def comparisonsThreading():
    timer_log = "comparisons_threading.txt"
    response_log = "comparisons_output_log_threading.txt"
    print("Doing comparisons with threading...")
    initial_loaded_gpu_mem = get_gpu_memory()
    print("Get initial GPU memory: ", initial_loaded_gpu_mem)
    with ThreadPoolExecutor(max_workers=10) as exe:
        # fut = exe.submit(cube,2)
        # print(fut.result())
        
        # result = exe.map(cube,values)

        with open(timer_log, "w") as f:
            f.write("--- Starting comparisons --- \n")
            f.write("Initial GPU memory loaded: " + str(initial_loaded_gpu_mem) + " MiB\nOf total GPU memory: " + str(get_total_gpu_memory()) + " MiB\n")
        
        with open(response_log, "w") as f:
            f.write("--- Starting logging responses --- \n")

        print("Starting comparisons.")

        print("1 request, baseline...")
        makeRequest("promptBaseline", "Which city is the Eiffel Tower located in?", timer_log, response_log)

        print("Doing 10 requests...")
        startTotal = time.perf_counter()
        print("starting threads")
        for prompt in listOfPrompts.keys():
            query = listOfPrompts[prompt]
            print(f"Handling {prompt} with query {query}...")
            exe.submit(makeRequest, prompt, query, timer_log, response_log)
            # makeRequest(prompt, query, timer_log, response_log)
        exe.shutdown(wait=True)
        endTotal = time.perf_counter()
        print("All threads completed.")
        with open(timer_log, "a") as f:
                f.write("\nIn total for 10 requests: Time taken for comparisons: " + str(endTotal - startTotal) + " seconds.\n")


print(f"Total GPU memory: {get_total_gpu_memory()}")

print("Setup LLM...")
# import localLLMqwen
# import localLLM
# localLLM.setupLLM()
import normistral_vllm_2
if __name__ == "__main__":
    llm = normistral_vllm_2.load()
    samplingparams = normistral_vllm_2.setup()
    print("LLM finished setting up.")

# comparisonsNoThreading()
# comparisonsThreading()
vLLMsimultaneousRequests()

