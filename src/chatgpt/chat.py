import readline #permite leer input de teclas
import openai

try:
    while True: #para que el programa corra continuamente (a no ser que se aprete Ctrl + C) - esto ya que la consigna pide
                #que se pueda interrumpir el programa con la tecla arriba, de otro modo
                #no se podría ya que el programa simplemente terminaría y nunca llega a utilizarse consulta_anterior
        try:
            consulta = input("Ingrese su consulta:")

            if consulta == "\033[A": #se refiere a cursor up
                consulta = consulta_anterior 

            response = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
            {
            "role": "system",
            "content": "context" },
            {
            "role": "user",
            "content" : "usertask" },
            {
            "role": "user",
            "content": consulta }
            ],
            temperature=1,
            max_tokens=4096,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            print(f"Su consulta fue {consulta}. Procesando...")

            print(f"ChatGPT dice: {response.choices[0].message.content}")

            consulta_anterior = consulta

        except KeyboardInterrupt:
            print("\nUsted presionó Control + C, lo que interrumió el programa.")
            break
        except Exception as ex:
            print(f"Error: {ex}")

except Exception as ex:
    print(f"Error: {ex}")