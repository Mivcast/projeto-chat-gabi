from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from gerar import gerar_resposta_gabi

app = FastAPI()

# Liberar CORS para funcionar no navegador
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo esperado do corpo da requisição
class Mensagem(BaseModel):
    mensagem: str

@app.post("/responder")
async def responder(body: Mensagem):
    resposta = gerar_resposta_gabi(body.mensagem)
    return {"resposta": resposta}
