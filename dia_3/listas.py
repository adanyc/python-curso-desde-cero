mi_lista = ['a', 'c', 'b']
mi_lista_2 = ['d', 'e', 'f']

lista_unida = mi_lista + mi_lista_2

# reemplazar elemento
lista_unida[0] = "alfa"

# agregar elemento a lista
lista_unida.append("g")

# quitar el ultimo elemento
lista_unida.pop()

# quitar un elemento determinado (por indice)
lista_unida.pop(0)

# ordenar elementos de una lista
lista_unida.sort()

# invertir el orden
lista_unida.reverse()

print(lista_unida)
