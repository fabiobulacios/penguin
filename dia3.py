ing_pan = ["Harina", "levadura","sal","azucar","agua"]

def imprimir_lista(ingredientes, nombre_producto):

    print("Lista de compras de", nombre_producto)
    print("..........................................")
    for producto in ingredientes:
        print(producto)
    print("__________________________________________")

imprimir_lista(ing_pan, "Pan")

ing_salsa = ["tomate","azucar","sal","cebolla"]

imprimir_lista(ing_salsa, "salsa de pizza")


##########################  CONDICIONALES #########################
# == igual
# > mayor que
# < menor que 
# >= mayor o igual que
# <= menor o igual que
# != distinto

a = 3 
#pregunta 1
if a > 3:
    print("Si, a es mayor a 3")
    print("chau")
else: 
    print("No, a no es mayor a 3")

#pregunta 2 
if a == 3:
    print("a es igual a 3")

nota = 60
#pregunta 3
if nota >= 60:
    print("Pasastee!!")
else: 
    print("Hule ya :c ")


#Ejr. Crear una funcion que reciba como parametro una 
#nota del 1 al 100 e imprima si pasate o te aplazaste

#Creamos una nueva funcion
#al usar if se llama a la condicion Si es que 

def Estado (puntos, nombre):
    if puntos >= 61:
        print("Pasaste", nombre)
    else:
        print("Repetis!", nombre)
    

Estado(61, "Fabio")
Estado(43,"Laura" )
Estado(87, "Juan")
Estado(35,"Alan")


a = 3
if a>5 and a<10 and a!= 7:
    print("a es mayor a 5 y menor que 10 y distinto que 7")
else: 
    print("a no esta en el rango, alguna de las 3 condiciones no se cumplieron")


if a > 5 or a < 10:
    print("a es mayor que 5 o menor que 10")
else: print("a no es mayor que 5 ni menor que 10")


#Elif sirve para decir: sino si
edad = 7
if edad > 18:
    print("deberia estar en la univerdad")
elif edad> 13:
    print("deberia estar en la secundaria")
elif edad > 6:
    print("deberia estar en la primaria")
else:
    print("deberia estar en su casa")



#Anidado
if edad > 18:
    print ("universidad")
else:
    if edad > 13:
        print("Secundaria")
    else:
        if edad > 6:
            print("Primaria") 
        else:
            print("bbdlc")

#Ejr. Crear una funcion puntaje que reciba como parametro una nota
# del 1 al 100e imprima que nota sacaste
#nota < 60 -----> 1
#nota entre 60 y 70 -----> 2
#nota entre 71 y 75-----> 3
#nota entre 76 y 85 -----> 4
#nota mayor 86 -----> 5


def Nota_final (num , alumno):
    if num < 60:
        print("Sacaste 1", alumno)
    elif num >  60 and num < 71:
        print("Sacaste 2", alumno)
    elif num > 70 and num < 76:
        print("sacaste 3", alumno)
    elif num > 75 and num < 86:
        print("sacaste 4", alumno)
    elif num > 85 and num < 96:
        print("Sacaste 5", alumno)
    else:
        print("Sacaste 5 Felicitado",alumno)
    

Nota_final(97,"name")
#### 



#############

lista_puntos = [76,45,89,97,67]

def Nota_final (notas , alumnos):
    for num in notas :
        alumno = alumnos[notas.index(num)] 
        if num < 60:
            print("Sacaste 1", alumno)
        elif num >  60 and num < 71:
            print("Sacaste 2", alumno)
        elif num > 70 and num < 76:
            print("sacaste 3", alumno)
        elif num > 75 and num < 86:
            print("sacaste 4", alumno)
        elif num > 85 and num < 96:
            print("Sacaste 5", alumno)
        else:
            print("Sacaste 5 Felicitado",alumno)
    

Nota_final(lista_puntos,["fa","tr","yu","jh","bd"])





#######  Ejer. Pedir al usuario que ingrese  tres numeros y multiplicarlos 
#entre si, imprimir el resultado

#numero1 = int(input("Ingresar el primer numero: "))
#numero2 = int(input("Ingresar el segundo numero: "))
#numero3 = int(input("Ingresar el tercer numero: "))

#print("el resultado es: " , numero1 * numero2 * numero3)


# Ejer2. Pedir al usuario un numero del 1 al 100 y llamar a la 
#funcion que retornaba la nota que creamos hace un rato
#utilizando el valor ingresado del usuario

#Nota_final(int(input("ingresar el puntaje")), "name")



###### Bucle while ==   #######
""" x = 74956
while x != 5: #mientras seea diferente a 5 va a hacer lo siguiente 
    print("Esto es  un buvle while, se va a ejecutar mientras x sea distito a 5")
    x = int(input("Ingresa un numero: ")) #ingresamos un nuevo valor para x
    print("El valor de x ahora es ", x)
print("Termino!!")
 """

#Contador inverso
contador = 10
while contador > 0 :
    print("Sigo un el bucle while")
    contador = contador - 1
    print("te quedan ", contador, "oportunidades")
print("termino")

#Contador 
contador = 0
while contador < 10 :
    print("sigo en el bucle while")
    contador = contador + 1
    print("Se repitio ", contador, " veces")


# Usando while pedir al usuario 5 engredientes para hacer una pizza
# y agregar a una lista, al final imprimir la lista

""" ing_pizza = 5
while ing_pizza > 0 :
    lista_pizza = []
    ing_pizza = ing_pizza - 1
    ing_pizza(input("Ingrese el ingrediente para la lista: "))
    lista_pizza.append() """

print("-----------------------------------------------")

#numero_secreto = 6

from random import randint
numero_secreto = randint (0,10)


adivino = False
while adivino == False:
    apuesta = int(input("Adivina el numero secreto de 1 al 10: "))

    if apuesta == numero_secreto:
        print("GANASTEE!!")
        adivino = True
    elif apuesta > 6:
        print("Pista: el numero deberia  ser menor")
    elif apuesta < 6:
        print("Pista: el numero deberia ser mayor")




#Ejr1. Crea un juego de adivinar el nummero commo el de arriba y darle pistas al usuario
#si el numero que ingreso es mayor o menor al numero a adivinar
#pista usar elif



#1 probar que funcione sin pistas
#2 que tengo que comparar
#3 dondde tengo nque comparar
#4 informar

#Ejr2. Buscar como generar un numeero aleatorio para numero secreto





