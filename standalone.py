import os

from llama_cpp import Llama

MODEL_NAME = "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)


# 1. Carregue o modelo
llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_threads=4, verbose=False)

# 2. Crie uma variável para armazenar o histórico
historico = ""

# 3. Loop de chat
while True:
    # Pergunta do usuário
    pergunta = input("Você: ")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        break

    # Atualiza o histórico
    historico += f"Usuário: {pergunta}\nAssistente:"

    # Faz a inferência
    resposta = llm(
        historico,
        max_tokens=256,
        stop=["Usuário:"],  # Para parar no final da resposta
        echo=False
    )

    # Extrai e mostra a resposta
    texto_resposta = resposta["choices"][0]["text"].strip()
    print(f"Assistente: {texto_resposta}\n")

    # Atualiza histórico com a resposta também
    historico += f" {texto_resposta}\n"
