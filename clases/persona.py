class Persona:   #creamos un objeto conn el nombre Persona
    edad = 0     #se le atribuye una variable de edad

    def __init__(self, un_nombre): #self se refiere al objeto #inint es para crear 
        self.mi_nombre = un_nombre    #mi_nombre es atribuido a Persona con un punto, proximamente le asignaremos un  nombre

        print("Hola naci, me llamo", self.mi_nombre) 
    def cumple(self):
        self.edad = self.edad + 1 

pepe = Persona ("Pepito")
pepe = Persona ("Pepita")
print(pepe.edad)
print(pepe.mi_nombre)

pepe.cumple()
print(pepe.edad)