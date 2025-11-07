import os
from dotenv import load_dotenv

load_dotenv()

import openai
import anthropic
import google.generativeai as gemini
import groq
import xai_sdk
import ollama

# -- Chamando keys do .env --
openai_Cliente = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# anthropic_Cliente = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
# xai_Cliente = xai_sdk.Client(api_key=os.getenv("XAI_API_KEY"))
# gemini.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# groq_Cliente = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

response = openai_Cliente.responses.create(
    model='gpt-5-nano',
    reasoning={
        "effort":"low"
    },
    input=[
        {
            "role":"system",
            "content":[
                {
                    "type":"input_text",
                    "text":"Seja direto e consiso, use uma unica frase nas respostas"
                }
            ]
        },
        {
            "role":"user",
            "content":[
                {
                    "type":"input_text",
                    "text":"Qual o sentido da vida?"
                }
            ]
        }
    ]
)

print(response.output_text)