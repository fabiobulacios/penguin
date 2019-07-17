#tipo de dato string/caddena/str de texto
"esto es un string"
#tipo de dato Integer/Entero/int
105
#Listas
[] #Lista_vacia
["Fabio", 21, "Hernandarias"]

#Bucles/Loops/ciclos
#impprime cada elemento, recorriendo cada uno
for cualquiercosa in range(10):
    print(cualquiercosa + 1 )

############## FUNCIONES ################
#def nombre_de_funcion (argumento/parametro):
#         nombre_de_funcion(parametro) #llamada a la funcion


def suma (num1, num2):
        resultado = num1 + num2
        return resultado

#Equivalente a la de arriba
def suma2 (num1, num2):
    return num1 + num2

#TENSORFLOW

print(suma(5,10))
resul = suma(5,8)
print(resul)

#Crear una funcion resta, que reciba como parametro dos numeros
#y retorne la resta de esos dos numeros
#luego llamar a la funcion e imprimir el resultado


def resta (num1,num2):
    return num1 - num2 
print(resta(9,6))
print(resta(7,4))

#Crear una funcion saludo2 que reciba como parametro nombre y edad
#e imprimir "Hola soy ____ y tengo ___ años"
#llamar veces a la funcion con distintos valores
#mota: retornar algo es opcional

def saludo2 (argumento , num3):
    print ("mi nombre es", argumento, "y tengo", num3) #se pude que imprima la funcion al llamar la funcion saludo2

saludo2 ("Fabio",21) #al crear la funcion solo hay que llamarla , luego llenar el () y probar



def saludo3 (argumento , num3):
    identificacion = 'mi nombre es ' + argumento + ' y tengo '+ num3
    print(identificacion)
    return "exito"
    
saludo3("Marce", "54") #aca imprime solo hasta el print por que el return está despues
print(saludo3("Marce", "54"))  #aca se imprime return por pedir que imprima la funcion 


############# ejercicio
# Crear una funcion suma_lista que reciba como argumento una lista de numero 
#y retorne la suma de sus elementos 
#Pista: usar un acumulador
#Pista2: la llamda deberia ser:
#suma_lista(listita)

listita = [1,2,3,4,5] # 1 + 2 + 3 + 4 + 5 = 15
listota = [100,5,5] #el valor de retorno seria 110

def suma_lista (una_lista):
    suma = 0                                  
    for b in una_lista :                    
        suma = suma + b
    return suma         
         
print(suma_lista(listita))

print (suma_lista(listota))






def lista_cuadrado(Lista_nueva): #se crea la funcion Lista_cuadrado con un argumento privado en def 
    listanew= []                 #lista vacia a llenarse de numeros al cuadrado
    for valor in Lista_nueva:    #inicia un ciclo con un nombre Valor a trabajar con el argumento

        lista_p = valor * valor  #una variable nueva dentro del ciclo  para multiplicar los valores de los elementos del ciclo
        listanew.append(lista_p) #append es para sumar elementos creados arriba  a la Lista_nueva
    return listanew              #retorna los valores de la lista antes vacia Listanew
print(lista_cuadrado(listita))   #imprime la ex lista vacia con los nuevos elementos asignados por Lista_p dentro del ciclo que agrega a la lista elementos.


grupo5 = ["E", "F","N","F1","F2","A"]     #realizacion de codigo de actividad al aire libre
print("antes", grupo5)
for j in range(len(grupo5)):
    grupo5.pop()
print("despues", grupo5 )

#Creaar una funcion suma_cuadrado que reciba una lista de numeros
#y retorne el valor de la suma de cada numero al cuadrado
#[1,2,3,4] es a 1+4+9+16=30

lista_numeross = [1,2,3,4]
def suma_cuadrado (lista_n):
    suma = 0
    for p in lista_n:

        suma = suma + (p*p)
    return suma 
print(suma_cuadrado(lista_numeross))

#ejemplo de la compañera, abajo

def suma_cuadrado2 (lista_n):
    return suma_lista(lista_cuadrado(lista_numeross))
print(suma_cuadrado2(lista_numeross)) 


     






