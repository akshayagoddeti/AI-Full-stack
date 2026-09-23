import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content":"I teach 5 years old students give me 3 lines"
        },
        {
            "role": "user",
            "content": "Explain ai"
        }
    ]
)
print(response["message"]["content"])