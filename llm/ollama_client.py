import ollama


def generate(prompt: str):
    try:
        response = ollama.chat(
            model="mistral",   # ✅ SAFE MODEL
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"LLM Error: {str(e)}"