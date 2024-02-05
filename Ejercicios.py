'''
Ejercicio 1
Realizar un programa que guarde la cadena de caracteres contraseña en una variable
y pregunte al usuario por la contraseña hasta que coincida con la contraseña
guardada.
'''
import string


def checkContrasenia():
    contraseniaUsuario = ""
    contrasenia = input("Introduce la contrasenia: ")
    while (contrasenia != contraseniaUsuario):
        contraseniaUsuario = input("Introduce la contrasenia: ")
    if (contrasenia == contraseniaUsuario):
        print("La contrasenia es correcta")


'''
checkContrasenia()
'''

'''
Ejercicio 2
Realizar un programa que guarde los módulos de un curso en una lista y la muestre
por pantalla indicando el mensaje Yo estudio “módulo” donde “módulo” es cada uno de
los módulos de la lista.
'''


def checkModulos():
    lista = ["base de datos", "programacion", "informatica"]
    for l in lista:
        print("Yo estudio ", l)


checkModulos()

'''
Ejercicio 3
Basado en el ejercicio anterior realizar un programa que pregunte al usuario la nota
que ha sacado en cada módulo y elimine de la lista los módulos aprobados. Al final el
programa debe mostrar por pantalla los módulos que el usuario tiene que repetir.
'''


def checkNota():
    modulos = ["acceso a datos", "psp", "pmdm"]
    modulos_repetidos = []
    index = 0  # Index to keep track of the current position in the list
    while index < len(modulos):
        m = modulos[index]
        print("Dime la nota del modulo ", m)
        nota = float(input())
        if nota < 5:
            modulos_repetidos.append(m)
            modulos.remove(m)
        else:
            index += 1
    return modulos_repetidos


'''
repetidos = checkNota()
print("Módulos a recuperar:", repetidos)
'''

'''
Ejercicio 4
Realizar una función que pida al usuario una palabra y muestre por pantalla si es un
palíndromo o no.
'''


def esPalindromo():
    palabra = input("Introduce palabra: ")
    index = 0
    palindromo = True
    while index < len(palabra) // 2 and palindromo:
        if palabra[index] != palabra[len(palabra) - index - 1]:
            palindromo = False
        index += 1
    if palindromo:
        print("Es palindromo")
    else:
        print("No es palindromo")

'''
esPalindromo()
'''
'''
Ejercicio 5
Realizar un programa que guarde en un diccionario los precios de las frutas de la
tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el
precio de la fruta. Si la fruta no está en el diccionario debe mostrar un mensaje
informando de ello.
Fruta Precio
Plátano 1.35
Manzana 0.80
Pera 0.85
Naranja 0.70
'''
def precios():
    frutas = {"Plátano": 1.35,"Manzana": 0.80,"Pera": 0.85,"Naranja": 0.70,"Pera": 0.85
             , "Pera":0.85, "Naranja":0.70}
    f = input("Fruta: ")

    if f in frutas:
        numKilos = float(input("¿Cuántos kilos deseas? "))
        for fr in frutas:
            if f == fr:
                print(f,"->",float(frutas[fr])*numKilos)
                break;
    else:
        print("No existe la fruta introducida")
'''
precios()
'''

'''
Ejercicio 6
Realizar una función que reciba una frase y devuelva un diccionario con las palabras
que contiene y su longitud.
'''

def checkDiccionario(frase):
    diccionario = {}
    palabras = frase.split(" ")
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
    print(diccionario)
'''
checkDiccionario("El mundo es un pañuelo")
'''

'''
Ejercicio 7
Realizar una función que pida la anchura de un triángulo y lo dibuje con caracteres
producto (*)
'''
def dibujar_triangulo(anchura):
    for i in range(1, anchura + 1):
        print('*' * i)
    for i in range(anchura, 0, -1):  # Empezamos desde la anchura y decrementamos hasta 1
        print('*' * i)


dibujar_triangulo(5)


'''
Ejercicio 8
Realizar un programa que cree una lista de palabras (que puede ser vacía). El
programa debe pedir el número de palabras que van a estar en la lista y luego solicitar
ese número de palabras para crear la lista. Por último, el programa tiene que escribir la
lista.
'''

def creaLista():
    lista = []
    numPalabras = float(input("Número de palabras: "))
    num = 0
    while(num < numPalabras):
        lista.append(input("Introduce: "))
        num+=1
    print(lista)

'''
creaLista()
'''
'''
Ejercicio 9
Realizar un programa que guarde los números que el usuario vaya introduciendo; el
criterio de finalización es cuando introduzca algo que no sea un número. Una vez que
haya terminado, el usuario debe indicar un número que haya introducido y el
ordenador deberá decirle el puesto en el que lo metió.
'''

def introduceDatos():
    datos = []
    index = 0
    while(True):
        dato = input("Introduce dato: ")
        if dato.isnumeric():
            datos.append(dato)
        else:
            print("saddasd")
            break

    numIntroducido = input("Introduce numero: ")
    while index<len(datos):
        if(numIntroducido==datos[index]):
            print(datos[index],"->",index+1)
        index+=1

introduceDatos()

'''
Ejercicio 10
El siguiente programa debería imprimir el número 2 si se le ingresan como valores
x=5, y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?
def maximo(a,b):
    if x>y:
        return x
    else:
    return y
    
def minimo(a,b):
    if x<y:
        return x
    else:
    return y
#programa principal
x=int(input("Un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo(x+2, y-5))
'''
'''
Está mal lo que le pasa por parámetros. En el primero está pasando a,b y usa dentro del metodo x e y. En el otro es al revés
'''