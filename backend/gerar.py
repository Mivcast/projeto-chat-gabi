import openai
import os

def gerar_resposta_gabi(pergunta):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": pergunta}],
            max_tokens=500,
            temperature=0.7
        )
        return resposta.choices[0].message["content"].strip()
    except Exception as e:
        print("Erro ao chamar OpenAI:", e)
        return "Opa! Tive um probleminha aqui pra te responder com inteligência agora 🤖 Se quiser, posso te passar direto pro Matheus no WhatsApp!"
