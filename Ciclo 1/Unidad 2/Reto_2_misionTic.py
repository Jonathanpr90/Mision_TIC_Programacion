informacion = {
    'Id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 14,
    'primer_ingreso': True
}


def cliente(informacion: dict) -> dict:
    pass
    if informacion['edad'] >= 19:
        atraccion = 'X-Treme'
        apto = True
        if informacion['primer_ingreso'] == True:
            total_boleta = 20000-(20000*0.05)
        else:
            total_boleta = 20000

    elif  informacion['edad'] >= 15  and informacion['edad'] <= 18:
        atraccion = 'Carros chocones'
        apto = True  
        if informacion['primer_ingreso'] == True:
            total_boleta = 5000-(5000*0.07)
        else:    
            total_boleta = 5000
        
    elif informacion['edad'] >= 7 and informacion['edad'] < 15:
        atraccion = 'Sillas voladoras'
        apto = True
        if  informacion['primer_ingreso'] == True:   
            total_boleta = 10000-(10000*0.05)    
        else:
            total_boleta = 10000
            
    else: 
        atraccion = 'N/A'
        apto = False
        total_boleta = 'N/A'

    respuesta = {'nombre': informacion['nombre'],
                 'edad': informacion['edad'],
                 'atraccion': atraccion,
                 'apto': apto,
                 'primer_ingreso': informacion ['primer_ingreso'],
                 'total_boleta': total_boleta
                 }
    return respuesta

cliente(informacion)

