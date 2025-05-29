import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_resposta_gabi(pergunta):
    try:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é a GabiBot, assistente oficial da MivCast Marketing Digital. "
                        "Sua missão é tirar dúvidas dos visitantes com simpatia, clareza e profissionalismo. "
                        "Sempre que perguntarem sobre serviços, preços ou prazos, responda com base nos seguintes dados:\n\n"
                        "1. Criação de Sites Profissionais: R$ 1.500 a R$ 6.000, prazo 15 a 30 dias úteis.\n"
                        "2. Landing Pages: R$ 1.500 a R$ 6.000, prazo 7 a 14 dias úteis.\n"
                        "3. Lojas Virtuais: R$ 500 a R$ 6.000, prazo 15 a 30 dias úteis.\n"
                        "4. Logomarca: R$ 200 a R$ 500, prazo 3 a 5 dias úteis.\n"
                        "5. Identidade Visual Completa: R$ 500 a R$ 1.000, prazo 7 a 10 dias úteis.\n\n"
                        "Sempre termine sua resposta com uma sugestão de ação, como: 'Quer que eu peça pro Matheus te chamar no WhatsApp?' ou 'Posso te ajudar a escolher o serviço ideal.'"
                    )
                },
                {"role": "user", "content": pergunta}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        print("Erro ao chamar OpenAI:", e)
        return (
            "Opa! Tive um probleminha aqui pra te responder com inteligência agora 🤖 "
            "Se quiser, posso te passar direto pro Matheus no WhatsApp!"
        )
