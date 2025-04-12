import os, openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def prever_movimento(moeda="BTC"):
    resposta = openai.ChatCompletion.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "Analise técnica rápida para BTC hoje."},
            {"role": "user", "content": "BTC preço atual $86,000, tendência forte de alta nas últimas 6h."}
        ]
    )
    decisao = resposta.choices[0].message.content
    return decisao

print(prever_movimento())
