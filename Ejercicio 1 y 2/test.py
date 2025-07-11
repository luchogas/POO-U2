from claseTarjetaSube import TarjetaSube

def test(self):
    numero = int(input("ingrese el numero: "))
    saldo = int(input("ingrese el saldo: ")) 
        
           
    unaTarjeta = TarjetaSube(saldo, numero)
    unaTarjeta.mostrar()
    unaTarjeta.cargar_saldo(1000)
    unaTarjeta.pagar_pasaje(750)
    unaTarjeta.consular_saldo()

