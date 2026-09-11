# -> env: mastertestenv
# python3 -m venv mastertestenv
# source mastertestenv/bin/activate
# module load Python/3.12.3-GCCcore-13.3.0 # for å få pip
# pip install transformers==4.57.6
# pip install torch==2.9.0
# pip install langchain-huggingface
# pip install nest_asyncio
# pip install -U bitsandbytes
# pip install accelerate

import torch
import transformers
from transformers import (
  AutoTokenizer,
  AutoModelForCausalLM,
  BitsAndBytesConfig,
  pipeline
)

from transformers import BitsAndBytesConfig
from langchain_huggingface import HuggingFacePipeline

#from langchain.prompts import PromptTemplate
from langchain_core.prompts import PromptTemplate

import nest_asyncio

import time
import datetime

from deepeval.models.base_model import DeepEvalBaseLLM

class NorMistral11B(DeepEvalBaseLLM):
    def __init__(
        self,
    ):
        super().__init__(model="NorMistral 11B")
    def load_model(self):
        print("Loading model!!!")
        #################################################################
        # Tokenizer
        #################################################################

        ## I denne variabelen setter man LLM modellen.
        ## Om man skal bruke nb-gpt: model_name='NbAiLab/nb-gpt-j-6B'
        global model_name
        #model_name='norallm/normistral-7b-warm-instruct'
        model_name='norallm/normistral-11b-thinking'

        model_config = transformers.AutoConfig.from_pretrained(
            model_name,
        )

        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True, model_max_length=32768)
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.padding_side = "right"


        #################################################################
        # Load pre-trained config
        #################################################################
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map='auto',
            torch_dtype=torch.bfloat16
        )

        ## Setter chat template for norallm/normistral-7b-warm-instruct, med en annen modell er det mulig denne må endres.
        messages = [
            {"role": "user", "content": "Hva er hovedstaden i Norge?"},
            {"role": "assistant", "content": "Hovedstaden i Norge er Oslo. Denne byen ligger i den sørøstlige delen av landet, ved Oslofjorden. Oslo er en av de raskest voksende byene i Europa, og den er kjent for sin rike historie, kultur og moderne arkitektur. Noen populære turistattraksjoner i Oslo inkluderer Vigelandsparken, som viser mer enn 200 skulpturer laget av den berømte norske skulptøren Gustav Vigeland, og det kongelige slott, som er den offisielle residensen til Norges kongefamilie. Oslo er også hjemsted for mange museer, gallerier og teatre, samt mange restauranter og barer som tilbyr et bredt utvalg av kulinariske og kulturelle opplevelser."},
            {"role": "user", "content": "Gi meg en liste over de beste stedene å besøke i hovedstaden"}
        ]
        gen_input = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)
        print("-----------GENINPUT", gen_input)


        ## Om man skal bytte LLM må man påse at disse parameterene er satt riktig.
        ## De som er satt her er det som ble anbefalt for normistral instruct: https://huggingface.co/norallm/normistral-7b-warm-instruct
        text_generation_pipeline = pipeline(
            model=model,
            task="text-generation",
            tokenizer=tokenizer,
            max_new_tokens=2048,
            top_k=64,  # top-k sampling
            top_p=0.9,  # nucleus sampling
            temperature=0.3,  # a low temparature to make the outputs less chaotic
            repetition_penalty=1.0,  # turn the repetition penalty off, having it on can lead to very bad outputs
            do_sample=True,  # randomly sample the outputs
            use_cache=True,  # speed-up generation
        )

        mistral_llm = HuggingFacePipeline(pipeline=text_generation_pipeline)

        ## Jeg aner ikke hva dette brukes til...
        import nest_asyncio
        nest_asyncio.apply()

        # Legg til model, tokenizer for contextcite.
        return mistral_llm


    def generate(self, prompt: str) -> str:
        print("Got a prompt!!!")
        result = self.model.invoke(prompt)

        return result


    async def a_generate(self, prompt: str) -> str:
        return self.generate(prompt)
    
    def generate_samples(
        self,
        prompt: str,
        n: int,
        temperature: float
        ):
        # prompt += "NOTE: Remember to include relevant imports." # Caused the sort list test to fail...
        print("Generating samples, one question, many times!")
        print("THis is the prompt->" + prompt + "<-")
        
        samples = []

        for _ in range(n):
            result = self.model.invoke(
                prompt
            )
            print("\n\nAnd this is the initial response->" + result + "<-\n\n")
            try:
                result = "def"+result.split("def")[-1]
                import re
                pattern = r"entry[\s_]?point"
                # matches = re.findall(pattern, result, re.IGNORECASE)
                # for match in matches:
                #     print(match)
                result = result.split(re.findall(pattern, result, re.IGNORECASE)[0])[0]
            except Exception as e:
                print("CLEANING ERROR:", repr(e))
            # except:
            #     result = result
            # result = "from typing import List\n\n " + result # Caused the sort list test to fail...
            print("\n\n This is the used result--> " + result + "<--\n\n")
            samples.append(result)
        print(samples)
        return samples


    def get_model_name(self):
        return "NorMistral 11B"


normistral_11b = NorMistral11B()
# print(normistral_11b.generate("Write me a joke"))
# print(normistral_11b.generate("Write me a super short horror story"))


print("Starting evals...")

from deepeval.benchmarks import HumanEval
from deepeval.benchmarks.tasks import HumanEvalTask

# Define benchmark with specific tasks and number of code generations
benchmark = HumanEval(
    tasks=[HumanEvalTask.HAS_CLOSE_ELEMENTS, HumanEvalTask.SORT_NUMBERS, HumanEvalTask.BELOW_ZERO],
    n=1, verbose_mode=True
)

# Replace 'gpt_4' with your own custom model
benchmark.evaluate(model=normistral_11b, k=1) # k må være mindre enn eller lik n. Har vanlighvis n=5 og k=3.
print(benchmark.overall_score)
