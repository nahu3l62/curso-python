from CuentaBancaria import*
from CuentaCorriente import*
from CuentaAhorro import*


print("--------------- CUENTA 1 --------------------")

cuenta1 = CuentaCorriente("Sebastian",2222222,date(1990,3,2),1000)

cuenta1.depositar(200)
cuenta1.depositar(0)
cuenta1.extraer(500)
cuenta1.extraer(1000)
cuenta1.extraer(500)

print(" ")
print(" ")

print("--------------- CUENTA 2 --------------------")

cuenta2 = CuentaAhorro("Nahuel",11111111,date(1995,10,28),7000)

cuenta2.depositar(1000)
cuenta1.depositar(0)
cuenta2.extraer(2000)
cuenta2.extraer(5000)