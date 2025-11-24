# tars_chat_actualizado.py

from openai import OpenAI

# ⚡ Tu API Key de OpenAI aquí
client = OpenAI(api_key="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")

def chatgpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content

print("🎙️ TARS Avatar Chat - Escribe 'salir' para terminar")

while True:
    user_input = input("\nTú: ")
    if user_input.lower() == "salir":
        print("Adiós bro 😎")
        break

    try:
        gpt_reply = chatgpt_response(user_input)
        print(f"TARS: {gpt_reply}")
    except Exception as e:
        print(f"⚠️ Error: {e}")

        
