import os

from llama_cpp import Llama

MODEL_NAME = "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)


llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=4,
    verbose=False
)

history = ""

while True:

    answer = input("You: ")
    if answer.lower() in ["exit", "quit"]:
        break

    history += f"You: {answer}\n"

    response = llm(
        history,
        max_tokens=256,
        stop=["\n", "You:"],
        temperature=0.5,
        echo=False
    )

    text_response = response["choices"][0]["text"].strip()
    history += f"LLM: {text_response}\n"

    print(f"LLM: {text_response}")
