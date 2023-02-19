text_input = input("ingrese un texto: ")
letters_input = input("ingrese tres letras separadas por comas: ")
letters = list(letters_input.split(","))

# primera letra
primera_letra = letters[0]
print(f"la letra {primera_letra} se repite {text_input.count(primera_letra)} veces")

# segunda letra
segunda_letra = letters[1]
print(f"la letra {segunda_letra} se repite {text_input.count(segunda_letra)} veces")

# tercera letra
tercera_letra = letters[2]
print(f"la letra {tercera_letra} se repite {text_input.count(tercera_letra)} veces")

# cuantas palabras hay en la oracion
words = list((text_input.lower()).split(" "))
words_length = len(words)
print(f"hay {words_length} palabras")

# cual es la primera y ultima letra del texto
print(f"la primera letra es {text_input[0]}")
print(f"la última letra es {text_input[-1]}")

# palabras en orden inverso
palabras_invertidas = words[::-1];
invertidas_unidas = " ".join(palabras_invertidas)
print(f"palabras en orden inverso: {invertidas_unidas}")

# ¿la palabra python se encuentra dentro del texto?
existe = "python" in text_input
print(f"¿palabra python se encuentra en el texto? {existe}")
