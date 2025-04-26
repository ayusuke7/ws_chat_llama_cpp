# 🧠 Chat LLM Local com llama.cpp e WebSocket

Este projeto é uma aplicação de **chat local** usando **modelos de linguagem (LLMs)** executados 100% **offline**, com interface Web e backend em Python via **WebSocket**. Ele utiliza a biblioteca `llama.cpp` para rodar modelos compactos no formato GGUF, ideais para uso local, sem necessidade de GPU.

---

## ✨ Funcionalidades

- Servidor Python com WebSocket
- Suporte a modelos `.gguf` via `llama-cpp-python`
- Download automático do modelo na primeira execução
- Cliente Web com interface tipo chat (balões à esquerda/direita)
- Botões de conectar e desconectar
- 100% offline

---

### Estrutura

chat-llm-local/
│
├── models/ # Onde o modelo .gguf será baixado
│
├── client.html # Interface web (chat)
├── server.py # Servidor Python com WebSocket + LLM
├── client.py # Client Python para terminal
└── README.md # Este arquivo

---

## 🛠️ Tecnologias e Dependências

### Backend (Python)

- `llama-cpp-python` — interface Python para `llama.cpp`
- `websockets` — servidor WebSocket
- `requests` — download do modelo
- `tqdm` — barra de progresso

Instale com:

```bash
pip install llama-cpp-python websockets requests tqdm

or

pip install -r requirements.txt

```

### Executando o Servidor

```bash
python server.py

```

### 📌 Observações

A performance depende do seu hardware (CPU ou GPU compatível com AVX2 ou Metal)
Modelos maiores também são suportados, mas exigem mais RAM
Você pode customizar o prompt, histórico, estilos e streaming conforme desejar
