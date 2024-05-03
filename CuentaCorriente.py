from CuentaBancaria import*

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0,limite_extraccion = 500):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion
    
    def extraer(self, monto):
        if monto <= self.getSaldo() and monto <= self._limite_extraccion:
            self.setSaldo(self.getSaldo() - monto)
            print(f"Se ha extraido {monto} de la cuenta de {self.getNombreTitular()}, su saldo actual es de: {self.getSaldo()}")
        else:
            if monto > self._limite_extraccion:
                print("Usted no puede extraer ese monto, supera el limite")
            else:
                print("Usted no posee saldo suficiente para realizar la operación")
                
    def depositar(self,monto):
        if monto > 0:
            self.setSaldo(self.getSaldo() + monto)
            print(f"Se ha depositado {monto} a la cuenta de {self.getNombreTitular()}, su saldo es de: {self.getSaldo()}")
        else:
            print("El monto a depositar debeser mayor a 0")