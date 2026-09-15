# !pip install transformers==4.57.6
# !pip install -U bitsandbytes
# !pip install accelerate
# !pip install langchain-huggingface

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

def setupLLM():
    print("SETTING UP LOCAL LLM: normistral-11b-thinking")
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
    # bitsandbytes parameters
    #################################################################

    # Activate 4-bit precision base model loading
    use_4bit = True

    # Compute dtype for 4-bit base models
    bnb_4bit_compute_dtype = "float16"

    # Quantization type (fp4 or nf4)
    bnb_4bit_quant_type = "nf4"

    # Activate nested quantization for 4-bit base models (double quantization)
    use_nested_quant = False

    #################################################################
    # Set up quantization config
    #################################################################
    compute_dtype = getattr(torch, bnb_4bit_compute_dtype)

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=use_4bit,
        bnb_4bit_quant_type=bnb_4bit_quant_type,
        bnb_4bit_compute_dtype=compute_dtype,
        bnb_4bit_use_double_quant=use_nested_quant,
    )

    # Check GPU compatibility with bfloat16
    if compute_dtype == torch.float16 and use_4bit:
        major, _ = torch.cuda.get_device_capability()
        if major >= 8:
            print("=" * 80)
            print("Your GPU supports bfloat16: accelerate training with bf16=True")
            print("=" * 80)

    #################################################################
    # Load pre-trained config
    #################################################################
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=bnb_config,
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


    print(print_number_of_trainable_model_parameters(model))


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

    global mistral_llm
    mistral_llm = HuggingFacePipeline(pipeline=text_generation_pipeline)

    ## Jeg aner ikke hva dette brukes til...
    import nest_asyncio
    nest_asyncio.apply()

    # Legg til model, tokenizer for contextcite.
    return mistral_llm

def print_number_of_trainable_model_parameters(model):
    trainable_model_params = 0
    all_model_params = 0
    for _, param in model.named_parameters():
        all_model_params += param.numel()
        if param.requires_grad:
            trainable_model_params += param.numel()
    return f"trainable model parameters: {trainable_model_params}\nall model parameters: {all_model_params}\npercentage of trainable model parameters: {100 * trainable_model_params / all_model_params:.2f}%"


def askLLMinteractive(prompt):
    #print("Setting up LLM")
    #mistral_llm = setupLLM()
    while True:
        question = input(f"\n -> Spør {model_name} LLM et spørsmål: ")
        prompt_template = """
        <|im_start|> user
        Instruksjon: Du er en assistent som skal svare på spørsmål. Svar på norsk:

        Spørsmål:
        {spørsmål}<|im_end|>
        <|im_start|> assistant
        """

        prompt_big = """
        You are an analysis expert tasked with answering questions using your knowledge, a curated playbook of strategies and insights and a reflection that goes over the diagnosis of all previous mistakes made while answering the question.

        **Instructions:**
        - Read the playbook carefully and apply relevant strategies, formulas, and insights
        - Pay attention to common mistakes listed in the playbook and avoid them
        - Show your reasoning step-by-step
        - Be concise but thorough in your analysis
        - If the playbook contains relevant code snippets or formulas, use them appropriately
        - Double-check your calculations and logic before providing the final answer

        Your output should be a json object, which contains the following fields:
        - reasoning: your chain of thought / reasoning / thinking process, detailed analysis and calculations
        - bullet_ids: each line in the playbook has a bullet_id. all bulletpoints in the playbook that's relevant, helpful for you to answer this question, you should include their bullet_id in this list
        - final_answer: your concise final answer


        **Playbook:**
        {}

        **Reflection:**
        {}

        **Question:**
        {What is 1+4+2+1?} 

        **Context:**
        {}

        **Answer in this exact JSON format:**
        {{
          "reasoning": "[Your chain of thought / reasoning / thinking process, detailed analysis and calculations]",  
          "bullet_ids": ["calc-00001", "fin-00002"],  
          "final_answer": "[Your concise final answer here]"
        }}

        ---
        """ 
        prompt_template = """
        Instruksjon: Du er en assistent som skal svare på spørsmål. Svar på norsk:

        Spørsmål:
        {spørsmål}
        """

        prompt = PromptTemplate(
                input_variables=["spørsmål"],
                template=prompt_template,
                            )

        #print(question)
        prompt = prompt.invoke(question).to_string()
        print(prompt)
        print("\n\n")
        print(prompt_big)
        result = mistral_llm.invoke(prompt_big)
        print("RESULTAT:")
        print(result)

def askLLM(prompt):
    # print("\nCALLING LOCAL LLM WITH PROMPT:", prompt + "\n")
    # question = input(f"\n -> Spør {model_name} LLM et spørsmål: ")
    

    prompt_big = """
    You are an analysis expert tasked with answering questions using your knowledge, a curated playbook of strategies and insights and a reflection that goes over the diagnosis of all previous mistakes made while answering the question.

    **Instructions:**
    - Read the playbook carefully and apply relevant strategies, formulas, and insights
    - Pay attention to common mistakes listed in the playbook and avoid them
    - Show your reasoning step-by-step
    - Be concise but thorough in your analysis
    - If the playbook contains relevant code snippets or formulas, use them appropriately
    - Double-check your calculations and logic before providing the final answer

    Your output should be a json object, which contains the following fields:
    - reasoning: your chain of thought / reasoning / thinking process, detailed analysis and calculations
    - bullet_ids: each line in the playbook has a bullet_id. all bulletpoints in the playbook that's relevant, helpful for you to answer this question, you should include their bullet_id in this list
    - final_answer: your concise final answer


    **Playbook:**
    {}

    **Reflection:**
    {}

    **Question:**
    {What is 1+4+2+1?} 

    **Context:**
    {}

    **Answer in this exact JSON format:**
    {{
        "reasoning": "[Your chain of thought / reasoning / thinking process, detailed analysis and calculations]",  
        "bullet_ids": ["calc-00001", "fin-00002"],  
        "final_answer": "[Your concise final answer here]"
    }}

    ---
    """ 
    prompt_template = """
    Instruksjon: Du er en assistent som skal svare på spørsmål. Svar på norsk:

    Spørsmål:
    {spørsmål}
    """

    # prompt = PromptTemplate(
    #         input_variables=["spørsmål"],
    #         template=prompt_template,
    #                     )

    #print(question)
    # prompt = prompt.invoke(question).to_string()
    # print(prompt)
    # print("\n\n")
    # print(prompt_big)
    result = mistral_llm.invoke(prompt)
    # print("RESULTAT:")
    # print(result)
    #result = "Dette er et testresultat fra askLLM funksjonen. Her skal det egentlig komme et svar fra LLM basert på prompten som sendes."
    result = result.split("---", 1)[1]
    return result



# print("Setting up LLM")
# mistral_llm = setupLLM()

# askLLM()
