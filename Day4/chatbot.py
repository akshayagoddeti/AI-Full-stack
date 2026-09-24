import ollama
msgs=[{
      
    "role":"System",
    "content":"I teach 18 old students"
}
]
while True:
    question=input("Ask question :")
    if question.lower() == "exit":
        break
    msgs.append(
        {
            "role":"user",
            "content":question
        }
    )
    response = ollama.chat(
        model="llama3.2:3b",
        messages=msgs
    )
    msgs.append({
        "role":"assistant",
        "content":response["message"]["content"]}
    )
    print(response["message"]["content"])
print("-----Chat history------")
for msg in msgs:
        print(msg["role"],":",msg["content"])