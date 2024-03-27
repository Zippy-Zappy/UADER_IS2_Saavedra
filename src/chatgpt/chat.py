# import openai

# try:

#     consulta = input("Ingrese su consulta:")

#     response = openai.chat.completions.create(
#     model="gpt-3.5-turbo-0125",
#     messages=[
#     {
#     "role": "system",
#     "content": "context" },
#     {
#     "role": "user",
#     "content" : "usertask" },
#     {
#     "role": "user",
#     "content": consulta }
#     ],
#     temperature=1,
#     max_tokens=4096,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
#     )
#     print (f"Su consulta fue {consulta}. Procesando...")

#     print(f"ChatGPT dice: {response.choices[0].message.content}")

# except Exception as ex:
#     print(f"Error: {ex}")