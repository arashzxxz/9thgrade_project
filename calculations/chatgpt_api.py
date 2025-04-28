
import requests

url = "https://api.puter.com/v2/ai/chat"

payload = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "hello"}
    ]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("massage :", data['message']['content'])
else:
    print("error:", response.status_code, response.text)
