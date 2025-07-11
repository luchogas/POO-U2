from test import test
from claseTarjetaSube import TarjetaSube
from controlador import ControladorSube

if __name__ == '__main__':
    #test()
    unControlador = ControladorSube()
    for i in range(3):
        numero = int(input("ingrese el numero:"))
        saldo = int(input("ingrese el saldo:"))
        otraTarjeta = TarjetaSube(saldo, numero)
        unControlador.agregar(otraTarjeta)

    unControlador.mostrar()
    unControlador.recorre()
    unControlador.buscar(123)