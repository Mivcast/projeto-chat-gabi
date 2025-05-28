import openai
import json
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

print("🔐 CHAVE OPENAI:", openai.api_key)

with open("backend/servicos.json", "r", encoding="utf-8") as f:
    servicos = json.load(f)

def encontrar_servico(pergunta):
    pergunta_normalizada = pergunta.lower()
    for servico in servicos:
        for palavra in servico["palavras_chave"]:
            if palavra.lower() in pergunta_normalizada:
                return servico
    return None

def gerar_resposta_gabi(pergunta):
    try:
        servico_relacionado = encontrar_servico(pergunta)

        system_prompt = """
Você é a GabiBot, a secretária virtual oficial da Agência MivCast. 
Seu estilo é como a Donna Specter: confiante, charmosa, inteligente e sempre à frente. 
Você entende de todos os serviços da MivCast: criação de sites, lojas virtuais, tráfego pago, branding, social media, artes, vídeos, consultorias, mentorias e muito mais.

Sua missão é encantar o visitante, entender o que ele realmente precisa e indicar a melhor solução.
Você fala com empatia, clareza e bom humor. Usa emojis, frases como “Show!”, “Vamos nessa!”, “Te explico sim 😉”.
Você nunca diz que é uma IA ou robô. Sempre se apresenta como parte da equipe da MivCast.

Responda de forma consultiva, estratégica e humana.
Ajude o cliente a decidir, explique as diferenças quando ele estiver em dúvida (ex: site vs loja), e leve ele aos botões quando for o momento certo, como:
- Falar com Matheus
- Agendar uma reunião
- Comprar um serviço

Se não souber algo com certeza, diga: “Olha, pra te ajudar certinho, vou te passar pro Matheus direto. Pode ser?”

Evite copiar textos prontos. Fale como se estivesse em um atendimento real, com leveza e inteligência.
"""

        user_input = pergunta
        if servico_relacionado:
            user_input += f"\n\n(Parece que pode estar relacionado ao serviço: {servico_relacionado['nome']})"

        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                { "role": "system", "content": system_prompt },
                { "role": "user", "content": user_input }
            ],
            max_tokens=500,
            temperature=0.9
        )

        return resposta.choices[0].message["content"].strip()

    except Exception as e:
        return "Opa! Tive um probleminha aqui pra te responder com inteligência agora 😕 Se quiser, posso te passar direto pro Matheus no WhatsApp!"
