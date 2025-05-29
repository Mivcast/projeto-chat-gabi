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

from pydantic import BaseModel

class Mensagem(BaseModel):
    mensagem: str

@app.post("/responder")
async def responder(dados: Mensagem):
    pergunta = dados.mensagem
    resposta = gerar_resposta_gabi(pergunta)
    return {"resposta": resposta}

