import asyncio
import os

import requests
import websockets
from llama_cpp import Llama
from tqdm import tqdm

# Configurações do modelo
MODEL_NAME = "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)
MODEL_URL = f"https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/{MODEL_NAME}?download=true"


def check_or_download_model():
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)

    if os.path.exists(MODEL_PATH):
        print("✅ Modelo já está presente.")
        return

    print("📥 Baixando modelo...")

    response = requests.get(MODEL_URL, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(MODEL_PATH, 'wb') as f, tqdm(
        desc=MODEL_NAME,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                bar.update(len(chunk))

    print("✅ Download completo!")


async def start_server():
    print("🧠 Carregando modelo... Isso pode levar alguns segundos.")
    llm = Llama(
        model_path=MODEL_PATH,
        n_threads=4,
        n_gpu_layers=1,
        verbose=False,
    )
    print("✅ Modelo carregado!")

    async def handle_client(websocket):
        async for message in websocket:
            print(f"Prompt recebido: {message}")
            result = llm(message, max_tokens=200, stop=[
                         "</s>", "\nUser:"], echo=False)
            response = result["choices"][0]["text"].strip()
            await websocket.send(response)
            # print(f"Resposta enviada: {response}")

    server = await websockets.serve(handle_client, "localhost", 8765)
    print("🚀 Servidor WebSocket iniciado em ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    check_or_download_model()
    asyncio.run(start_server())
