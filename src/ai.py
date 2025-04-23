import requests

def ask_llama(prompt):
    instructions="You are an empathetic mental health chatbot. Respond with warmth, understanding, and keep replies brief (1–2 sentences max). "
    prompt=instructions+prompt.strip()
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.2",  # Match the tag you saw in `ollama list`
        "prompt": prompt,
        "stream": False
    }

    try:
        res = requests.post(url, json=payload, timeout=15)
        res.raise_for_status()
        data = res.json()
        return data.get("response", "I'm here to listen. Tell me more.")
    except Exception as e:
        print("LLaMA fallback error:", e)
        return "I'm here for you, even when it's hard to talk."

# Test it
if __name__ == "__main__":
    answer = ask_llama("My dog is running")
    print(answer)
