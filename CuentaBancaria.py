from abc import ABC , abstractmethod
from datetime import date

class CuentaBancaria(ABC):
    def __init__(self,nombre_titular,dni_titular, fecha_nacimiento, saldo=0):
        self._nombre_titular = nombre_titular       
        self._dni_titular = dni_titular             
        self._fecha_nacimiento = fecha_nacimiento   
        self._saldo = saldo                         

    def getSaldo(self):
        return self._saldo
    
    def getFechaDeNacimiento(self):
        return self._fecha_nacimiento
    
    def getNombreTitular(self):
        return self._nombre_titular
    
    def setSaldo(self,saldo):
        self._saldo = saldo
            
    @abstractmethod
    def depositar(self,monto):
        pass

    @abstractmethod
    def extraer(self,monto):
        pass

    def _calcular_edad(self):
        edad = date.today() - self.getFechaDeNacimiento()
        return edad.days // 365
    
    def obtener_edad(self):
        return self._calcular_edad()