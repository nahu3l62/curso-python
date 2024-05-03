from CuentaBancaria import*

class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular,dni_titular, fecha_nacimiento, saldo, tasaInteres = 0.001):
        super().__init__(nombre_titular,dni_titular, fecha_nacimiento, saldo)
        self._tasaInteres = tasaInteres
       
    def sumarInteres(self):
        return self.getSaldo()+(self.getSaldo() * self._tasaInteres)
             
    def depositar(self,monto):
        if monto > 0:
            self.setSaldo(self.getSaldo() + monto)
            self.setSaldo(self.sumarInteres()) 
            print(f"Se ha depositado {monto} a la cuenta de {self.getNombreTitular()}, su saldo actual con intereses es de: {self.getSaldo()}")
            
        else:
            print("El monto a depositar debe ser mayor a 0")

    def extraer(self,monto):
        if monto <= self.getSaldo():
            self.setSaldo(self.getSaldo() - monto)
            self.setSaldo(self.sumarInteres())
            print(f"Se ha extraido {monto} de la cuenta de {self.getNombreTitular()}, su saldo actual con intereses de: {self.getSaldo()}")
        else:
            print("No posee saldo suficiente para esta operación")    
        
    
        