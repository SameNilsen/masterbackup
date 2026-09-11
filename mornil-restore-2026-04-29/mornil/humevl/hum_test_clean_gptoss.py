

import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer


from deepeval.models.base_model import DeepEvalBaseLLM

class GptOss20b(DeepEvalBaseLLM):
    def __init__(
        self,
    ):
        super().__init__(model="Gpt Oss 20b")

    def load_model(self):
        print("Loading model!!!")

        model_id = "openai/gpt-oss-20b"
        print("Setting up local LLM:", model_id)

        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype="auto", # was auto
            device_map="cuda", # was cuda, could be auto.
        )
        return model
    


    def generate(self, prompt: str) -> str:
        print("Got a prompt!!!")

        messages = [
        {"role": "user", "content": prompt},
        ]

        inputs = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt",
            return_dict=True,
        ).to(self.model.device)

        # Can add "reasoning_effort="high"" after return_dict.

        generated = self.model.generate(**inputs, max_new_tokens=2000)
        result = self.tokenizer.decode(generated[0][inputs["input_ids"].shape[-1]:])
        # print(tokenizer.decode(generated[0][inputs["input_ids"].shape[-1]:]))

        # Return only JSON part of the response:
        # try:
        #     result = result.split("assistantfinal", 1)[1]
        #     print("Detected gpt_oss-style output, extracting JSON part")
        # except:
        #     print("Not able to split on assistantfinal, returning full result")
        return result


    async def a_generate(self, prompt: str) -> str:
        return self.generate(prompt)
    
    def generate_samples(
        self,
        prompt: str,
        n: int,
        temperature: float
        ):
        print("Generating samples, one question, many times!")
        print("THis is the prompt->" + prompt + "<-")
        
        samples = []

        for _ in range(n):
            result = self.generate(prompt)
            print("\n\nAnd this is the initial response->" + result + "<-\n\n")
            try:
                result = "def"+result.split("def")[-1]
                result = result.split("<|return|>")[0]
                import re
                pattern = r"entry[\s_]?point"
                result = result.split(re.findall(pattern, result, re.IGNORECASE)[0])[0]
            except Exception as e:
                print("CLEANING ERROR:", repr(e))
            print("\n\n This is the used result--> " + result + "<--\n\n")
            samples.append(result)
        # print(samples)
        return samples


    def get_model_name(self):
        return "Gpt Oss 20b"


gptOss20b = GptOss20b()


print("Starting evals...")

from deepeval.benchmarks import HumanEval
from deepeval.benchmarks.tasks import HumanEvalTask

# Define benchmark with specific tasks and number of code generations
benchmark = HumanEval(
    tasks=[HumanEvalTask.HAS_CLOSE_ELEMENTS, HumanEvalTask.SORT_NUMBERS, HumanEvalTask.BELOW_ZERO, HumanEvalTask.TRUNCATE_NUMBER],
    n=1, verbose_mode=True
)

# Replace 'gpt_4' with your own custom model
benchmark.evaluate(model=gptOss20b, k=1) # k må være mindre enn eller lik n. Har vanlighvis n=5 og k=3.
print(benchmark.overall_score)
