
import requests
import time


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"


def generate_response(prompt):

    start_time = time.time()

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    result = response.json()

    end_time = time.time()

    return {
        "response": result.get("response", ""),
        "input_tokens": result.get("prompt_eval_count", 0),
        "output_tokens": result.get("eval_count", 0),
        "response_time": round(end_time - start_time, 2)
    }


if __name__ == "__main__":

    result = generate_response(
        "Explain MongoDB in simple words."
    )

    print("AI Response:")
    print(result["response"])

    print("Input Tokens:", result["input_tokens"])
    print("Output Tokens:", result["output_tokens"])
    print("Response Time:", result["response_time"], "seconds")
