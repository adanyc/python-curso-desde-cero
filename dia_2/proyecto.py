nombre = input("Nombre: ")
ventas = input("Ventas ($): ")
comision = round(((float(ventas) * 13)/100),2)
print(f"Te corresponde una comisión de $ {comision}")
