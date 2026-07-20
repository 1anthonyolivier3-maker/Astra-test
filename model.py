cat << 'EOF' > model.py
import os
import requests

HF_TOKEN = os.environ.get("HF_TOKEN")
MODEL_ID = "HuggingFaceH4/zephyr-7b-beta"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

def generate_answer(prompt: str) -> str:
    if not HF_TOKEN:
        return "Erreur : Le token HF_TOKEN n'est pas configuré dans Railway."

    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {
        "inputs": f"<|user|>\n{prompt}<|end|>\n<|assistant|>",
        "parameters": {"max_new_tokens": 250, "temperature": 0.7}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        output = response.json()

        if isinstance(output, list) and "generated_text" in output[0]:
            full_text = output[0]["generated_text"]
            return full_text.split("<|assistant|>")[-1].strip()
        else:
            return f"Erreur de l'API : {output}"

    except Exception as e:
        return f"Une erreur est survenue : {str(e)}"
EOF
