import requests

def check_ollama_status():
    try:
        response = requests.get("http://localhost:11434/api/generate")
        if response.status_code == 200:
            print("Ollama's Llama 3 is running!")
            print(response.json())
        else:
            print("Failed to connect to Ollama's Llama 3.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_ollama_status()
