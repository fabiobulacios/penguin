class Vehiculo:
    cant_ruedas = 0
    # tipo_cubiertas = ""
    # motor = 0

    def __init__(self, cant_ruedas): #, tipo_cubiertas, motor
        self.cant_ruedas = cant_ruedas
        # self.tipo_cubiertas = tipo_cubiertas
        # self.motor = motor
    
    def tipo_movil (self):
        if self.cant_ruedas == 2:
            print("Es una moto")
        elif self.cant_ruedas == 3:
            print("Es un triciclo")
        elif self.cant_ruedas == 4:
            print("Es un auto")  

        else:
            print("No disponible, tenemos 2, 3 y 4 ruedas")

auto = Vehiculo (4)
moto = Vehiculo (2)

auto.tipo_movil()
moto.tipo_movil()