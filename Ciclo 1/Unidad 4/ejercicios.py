# from functools import reduce

# lista = ["Python", "Java", "C++", "C#", "JavaScript"]

# resultado = reduce(lambda x, y: x +" - "+ y, lista)
# print (resultado)

# El codigo anterior es una funcion lambda que suma los elementos de una lista utilizando reduce

# nombres = ["Raul", "Juan", "Pedro", "Luis", "Carlos"]
# apellidos = ["Perez", "Gonzalez", "Perez", "Gonzalez", "Perez"]
# edades = ["20", "30", "40", "50", "60"]

# personas = set(zip(nombres, apellidos, edades))
# print (personas)

# El codigo anterior es una funcion que crea un conjunto de tuplas con los datos de 
# diferentes listas con la funcion zip

# lista = [True,True,True]
lista = [False,True]
print(all(lista))
print(any(lista))