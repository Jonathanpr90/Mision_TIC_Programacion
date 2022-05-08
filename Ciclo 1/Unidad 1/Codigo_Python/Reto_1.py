def CDT(usuario: str,capital: int, tiempo: int):
    porcentaje_perdida= 0.02
    porcentaje_interes= 0.03
    if tiempo > 2:
        valor_interes=(capital*porcentaje_interes*tiempo)/12
        valor_total = valor_interes+capital
        respuesta_CDT=str("Para el usuario "+str(usuario)+" La cantidad de dinero a recibir, según el monto inicial "+str(capital)+" para un tiempo de "+str(tiempo)+" meses es: "+str(valor_total)) 
    else:
        valor_a_perder=capital*porcentaje_perdida
        valor_total=capital-valor_a_perder
        respuesta_CDT=str("Para el usuario "+str(usuario)+" La cantidad de dinero a recibir, según el monto inicial "+str(capital)+" para un tiempo de "+str(tiempo)+" meses es: "+str(valor_total))
    return respuesta_CDT

usuario=str(input("Ingrese el nombre del usuario: "))
capital=int(input("Ingrese la cantidad a depositar en el CDT: "))
tiempo=int(input("Ingrese el tiempo en meses del CDT: "))
respuesta_imprimir=CDT(usuario,capital,tiempo)
print(respuesta_imprimir)

"""def CDT(usuario: str,capital: int, tiempo: int):
    porcentaje_perdida= 0.02
    porcentaje_interes= 0.03
    if tiempo >= 3:
        valor_interes=(capital*porcentaje_interes*tiempo)/12
        valor_total = valor_interes+capital
        respuesta_CDT=str("Para el usuario "+str(usuario)+" La cantidad de dinero a recibir, según el monto inicial "+str(capital)+" para un tiempo de "+str(tiempo)+" meses es: "+str(valor_total)) 
    else:
        valor_a_perder=capital*porcentaje_perdida
        valor_total=capital-valor_a_perder
        respuesta_CDT=str("Para el usuario "+str(usuario)+" La cantidad de dinero a recibir, según el monto inicial "+str(capital)+" para un tiempo de "+str(tiempo)+" meses es: "+str(valor_total))
    return respuesta_CDT

usuario=str("AB1012")
capital=int(1000000)
tiempo=int(3)
respuesta_imprimir=CDT(usuario,capital,tiempo)
print(respuesta_imprimir)"""
