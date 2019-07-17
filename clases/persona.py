class Persona:   #creamos un objeto conn el nombre Persona, una receta para crear un objeto
    edad = 0     #se le atribuye una variable de edad

    def __init__(self, un_nombre, nacionalidad, peso): #self se refiere al objeto #innt es para crear 
        self.mi_nombre = un_nombre    #mi_nombre es atribuido a Persona con un punto, proximamente le asignaremos un  nombre
        self.peso = peso              #
        self.nacionalidad = nacionalidad
        
    def cumple(self): #cumple. es metodo de la clase de persona
        self.edad = self.edad + 1 #que aumenta la propiedad edad en 1

    def asignar_edad(self, una_edad):
        self.edad = una_edad

    def asignar_nacionaliadad(self, una_nacionalidad):
        self.nacionalidad = una_nacionalidad

    def asignar_peso(self, un_peso):
        self.peso = un_peso

    def saludar(self):
        print("Hola me llamo", self.mi_nombre, "y soy de nacionalidad", self.nacionalidad, ", Peso", self.peso ) 

Fabio = Persona ("Fabio", "Paraguaya", 76)       #pepe es un objeto de la clase Persona
Pepe = Persona ("Pepito", "Cubana",65)

Fabio.saludar()


# print(pepe.edad)
# print(pepe.mi_nombre)

# pepe.cumple()
# print(pepe.edad)

##Ejercicio
#agregar un metodo clase Persona que asigne una nacionalidad y otro metodo "saludar"
#que imprima Hola soy ... y mi  nacionalidad es ...