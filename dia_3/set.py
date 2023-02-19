# solo admiten elementos unicos.
# no estan ordenados en indices
# sus elementos son inmutables


mi_set = set([1, 2, 3, 4, 5])

# otra forma
# mi_set = set((1,2,3,4,5)<)

# otra forma
# mi_set = {1,2,3}

print(mi_set)

# buscar
print(2 in mi_set)

# union de sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

# agregar
s1.add(4)
print(s1)

# eliminar
s1.remove(3) # si le mandas a eliminar un elemento que no existe, saldrá error.

# descartar
s1.discard(9)

# pop (elimina un elemento aleatorio ya que los sets no tienen posiciones)
s1.pop()

# limpiar todo el set
s1.clear()