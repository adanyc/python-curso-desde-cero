# diccionario = {
#     "nombre": "juan",
#     "apellido": "perez",
#     "peso": 80,
#     "talla": 1.73
# }
# print(diccionario)

# buscar
# print(diccionario["apellido"])

# listas complejas
# dic = {"c1": 55, "c2": [1, 2, 3], "c3": {"s1": 100, "s2": 200}}
# print(dic["c2"][1])

# dic = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}
# print(dic["c2"][1].upper())

# agregar elemento
dic = {1: "a", 2: "b"}
dic[3] = "c"
print(dic)

# sobreescribir
dic[1] = "B"
print(dic)

# obtener todas las keys
print(dic.keys())

# obtener todos los valores
print(dic.values())

# conocer todo lo que hay en un diccionario
print(dic.items())


mi_dict = {
    "valores_1": {
        "v1": 3,
        "v2": 6
    },
    "puntos": {
        "points1": 9,
        "points2": [10, 300, 15]
    }}
print(mi_dict["puntos"]["points2"][1])
