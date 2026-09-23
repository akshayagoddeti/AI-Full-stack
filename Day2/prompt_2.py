import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "explain what is ai and two types of ai and one example in 6 lines"
        }
    ]
)
print(response["message"]["content"])