#print("hola mundo")
"""a=float(27.8)
b= int(a)
print(bin(b))
print(oct(b))
print(hex(b))"""
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un 
mensaje en pantalla indicando que debe abonar impuestos."""

sueldo = int(input("Ingrese el valor de sueldo \n"))
if sueldo > 3000:
    print("Debe declarar renta")
else:
    print("no debe pagar nada")