from gestorBecas import GestorBeca
from gestorBeneficiario import GestorBene

def menuOP():
    print("a")
    print("b")
    print("c")
    print("d")
    print("x. salir")

if __name__ == "__main__":
    gestorBeca = GestorBeca()
    gestorBeneficiario = GestorBene()
    
    gestorBeca.cargar()
    gestorBeneficiario.cargar()
    opcion = ""
    
    while opcion != "x":
        menuOP()
        opcion = input("Ingrese una opción: ").lower()
        if opcion == "a":
           tipo = input("ingrese un tipo de beca: ")
           gestorBeca.buscarBeca(tipo, gestorBeneficiario)
        
        elif opcion == "b":
            print("b")
        elif opcion == "c":
            print("c")
        elif opcion == "d":
            print("d")
        elif opcion == "x":
            print("Saliendo del programa...")
        else:
            print("Opción no válida.")