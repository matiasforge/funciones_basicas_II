# Cuenta regresiva

def countdown(numero):
    lista_countdown = []
    for i in range(numero, -1, -1):
        lista_countdown.append(i)
    return lista_countdown

print(countdown(8))


# Imprimir y devolver
def imprimir_y_devolver(lista):
        print(lista[0])
        return lista[1]

valor_devuelto = imprimir_y_devolver([7, 9])
print(valor_devuelto)


# Primero más longitud
def primero_mas_longitud(lista):
    suma = lista[0] + len(lista)
    return suma

print(primero_mas_longitud([10,20,30,40]))


# Valores mayores a segundo
def valores_mayores_que_el_segundo(lista):
    if len(lista) < 2:
        return False
    segundo_valor = lista[1]
    nueva_lista = []
    for valor in lista:
        if valor > segundo_valor:
            nueva_lista.append(valor) 
    print(len(nueva_lista))
    return nueva_lista

resultado = valores_mayores_que_el_segundo([8, 12, 5, 4, 15, 3])
print(resultado)


# Esta longitud, ese valor

def tamaño_y_valor(tamano, valor):
    nueva_lista = [valor] * tamano
    return nueva_lista

resultado3 = tamaño_y_valor(3, 10)
print(resultado3)

resultado4 = tamaño_y_valor(5, 0)
print(resultado4)



