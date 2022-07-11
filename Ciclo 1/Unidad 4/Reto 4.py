from functools import reduce

def ordenes(rutinaContqable):
    ordenTotal = list(map(lambda x: [x[0]] + list(map(lambda y: y[1] * y[2], x[1:])), rutinaContqable))
    ordenTotal = list(map(lambda x: [x[0]] + [reduce(lambda a,b: round(a+b,2), x[1:])], ordenTotal))
    ordenTotal = list(map(lambda x: x if x[1] >= 600000 else (x[0], x[1] + 25000), ordenTotal))
    
    print('------------------------ Inicio Registro diario ---------------------------------')
    for i in range(len(ordenTotal)):
        print(f"La factura {ordenTotal[i][0]} tiene un total en pesos de {ordenTotal[i][1]:,.2f}")
    print('-------------------------- Fin Registro diario ----------------------------------')