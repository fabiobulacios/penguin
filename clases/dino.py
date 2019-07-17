class Dino:
    ojos = 2

    def __init__ (self, un_nombre , un_color, canti_patas, un_genero):
        self.nombre = un_nombre
        self.color = un_color
        self.patas = canti_patas
        self.genero = un_genero
        print("naci")
    
    def saludar(self):
        print("Hola me lamo", self.nombre, "tengo", self.patas, "patas y soy", self.color)

    def cortar_patas(self, cantidad_de_patas_a_cortar=1):
        self.patas = self.patas - cantidad_de_patas_a_cortar

    def decir_genero(self):
        print("Hola soy ", self.nombre, "y me identifico como", self.genero)


rexi = Dino("Tiranosaurio Rex","Verde oscuro",4, "macho")

rexi.saludar()