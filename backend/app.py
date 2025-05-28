from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.assistente_virtual import gerar_resposta_gabi

app = FastAPI()

# Permite requisições de qualquer origem (ideal para testes locais ou integração em sites)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/responder")
async def responder(request: Request):
    dados = await request.json()
    pergunta = dados.get("mensagem", "")
    resposta = gerar_resposta_gabi(pergunta)
    return {"resposta": resposta}
