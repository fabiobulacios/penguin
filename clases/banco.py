class Cuenta:
    def __init__(self, propietario, saldo_inicial, num_cuenta): #al crear nuestro objeto le asignamos sus atributos
        self.nombre = propietario   
        self.saldo = saldo_inicial
        self.socio = num_cuenta    
    def depositar(self,monto):
        self.saldo += monto #self.saldo = self.saldo + monto    
    def extraer(self,monto):
        if self.saldo < monto:
            print("no tenes plata nde mboriahu")
        else:
            self.saldo -= monto #self.saldo = self.saldo - monto

    def consulta_saldo(self):
        print("El saldo de la cuenta", self.socio, "es: ", self.saldo, "dolares")
    
    def transferir(self,cuenta,monto):
        
        if cuenta.socio == self.socio:
            pass
        else:
            self.extraer(monto) 
            cuenta.depositar(monto) 



Cuenta1 = Cuenta("Fabio Bulacios", 500, 10)
Cuenta2 = Cuenta("Enzo Borrach", 800, 12)

Cuenta2.transferir(Cuenta1, 60)
Cuenta2.consulta_saldo()
Cuenta1.consulta_saldo()
# Cuenta1.depositar (200)
# Cuenta1.consulta_saldo()
# Cuenta1.extraer(160)
# Cuenta1.consulta_saldo()
# Cuenta1.extraer(700)
# Cuenta1.consulta_saldo()


