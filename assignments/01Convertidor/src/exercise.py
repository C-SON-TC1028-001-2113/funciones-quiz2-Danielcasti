# Escribe tus funciones abajo de esta línea
def pies_cm(pies): 
    respuesta1 = (pies*30.48)
    return(respuesta1)

def pulgadas_cm(pulgadas):
    respuesta2 = (pulgadas*2.54)
    return (respuesta2)

def yardas_cm(yardas): 
    respuesta3 = (yardas*91.44)
    return(respuesta3)
def main():
    # Escribe tu código abajo de esta línea
    print('1. pies a cm, 2. pulgadas a cm, 3. yardas a cm')
    procedimiento= str(input('Introduce una opcion: '))
    cantidad = int(input('Introduce la cantidad: '))
    if cantidad > 0 : 
        if procedimiento == '1': 
            respuesta1 = pies_cm(cantidad)
            print(respuesta1)
        elif procedimiento == '2': 
            respuesta2 = pulgadas_cm(cantidad)
            print(respuesta2)
        elif procedimiento == '3':
            respuesta3 = yardas_cm(cantidad)
            print(respuesta3)
        else:
            print('Error')
    else: 
        print('Error')
if __name__ == '__main__':
    main()
