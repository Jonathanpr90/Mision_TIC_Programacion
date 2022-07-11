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

# # lista = [True,True,True]
# lista = [False,True]
# print(all(lista))
# print(any(lista))

# uids = ['B1CD102354','B1CDEF2354']

# for uid in uids:
#     cond = []
#     # Verificación de por lo menos dos mayusculas
#     cond.append(len(list(filter(lambda x : x.isupper(), list(uid)))) >= 2)
#     # Verificación de por lo menos tres digitos
#     cond.append(len(list(filter(lambda x : x.isdigit(), list(uid)))) >= 3)
#     # Verificación solo caracteres alfanumericos
#     cond.append(len(list(filter(lambda x : not(x.isalnum()), list(uid)))) == 0)
#     # Verificación sin repeticiones
#     cond.append(len(uid) == len(set(uid)))
#     # Verificación debe tener 10 caracteres
#     cond.append(len(uid) == 10)
    
#     print("Valido") if all(cond) else print("Invalido")

# El ejercio anterior se valida 5 condiciones sobre un identificador de una lista

# info =[int(input('Ingrese la cantidad de digitos: ')), input('Ingrese el numero: ').split(' ')] #Split me lo convierte en lista
# print('True' if  all (list(map(lambda x: x>0, list(map(int, info[1]))))) and any (list(map(lambda x : x[0] == x[1] or x[0] == '5', list (zip(info[1], list(map(lambda x : x[-1:(len(x)+1)*-1:-1], info[1]))))))) else 'False')


