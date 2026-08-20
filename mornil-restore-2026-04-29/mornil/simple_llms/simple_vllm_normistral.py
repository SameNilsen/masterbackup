# !pip install jedi
# #!pip install protobuf==5.29.3
# #!pip install vllm==0.7.0
# !pip install transformers==4.57.6
# !pip install vllm==0.11.0
# #!pip install vllm

# if __name__ == '__main__':

from vllm import LLM, SamplingParams
def main():
    print("\nLoading model...\n")
    # load the NorMistral model
    llm = LLM(
        model="norallm/normistral-11b-thinking",
        dtype="half", # prev bfloat16.
        tensor_parallel_size=4,
        gpu_memory_utilization=0.8,
        max_model_len=32768
    )
    print("\nmodel loaded...\n")
    # create a conversation
    messages = [
        {"role": "user", "content": "Hva er hovedstaden i Norge?"},
        {"role": "assistant", "content": "Hovedstaden i Norge er Oslo. Denne byen ligger i den sørøstlige delen av landet, ved Oslofjorden. Oslo er en av de raskest voksende byene i Europa, og den er kjent for sin rike historie, kultur og moderne arkitektur. Noen populære turistattraksjoner i Oslo inkluderer Vigelandsparken, som viser mer enn 200 skulpturer laget av den berømte norske skulptøren Gustav Vigeland, og det kongelige slott, som er den offisielle residensen til Norges kongefamilie. Oslo er også hjemsted for mange museer, gallerier og teatre, samt mange restauranter og barer som tilbyr et bredt utvalg av kulinariske og kulturelle opplevelser."},
        {"role": "user", "content": "Gi meg en liste over de beste stedene å besøke i hovedstaden"}
    ]

    # set up sampling parameters (equivalent to the generate() parameters)
    sampling_params = SamplingParams(
        max_tokens=2048,  # limit max number of generated tokens
        top_k=64,  # top-k sampling
        top_p=0.9,  # nucleus sampling
        temperature=0.3,  # a low temperature to make the outputs less chaotic
        repetition_penalty=1.0,  # turn the repetition penalty off
    )

    # run the generation using the chat interface (applies chat template automatically)
    outputs = llm.chat(messages, sampling_params=sampling_params)

    # get the generated text
    output_str = outputs[0].outputs[0].text.strip()

    # separate the reasoning trace that's enclosed in the special <think> ... </think> tokens
    reasoning_trace = output_str.split("</think>")[0].lstrip("<think>").strip()

    # separate the actual response that follows after the </think> token
    response = output_str.split("</think>")[-1].rstrip("</s>").strip()

    print("\nReasoning trace:\n", reasoning_trace)
    print("Generated response:\n", response)

if __name__ == "__main__":
    main()
