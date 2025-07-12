from manjeadorPacientes import ManejaPacientes
from manejadorAtenciones import ManejaAtenciones



def menu():
    print("\n--- MENÚ ---")
    print("a. Informar atenciones por fecha")
    print("b. Informar datos y cantidad de atenciones por DNI")
    print("c. Pacientes sin ninguna atención")
    print("d. Listar pacientes ordenados por Unidad y Apellido")
    print("x. Salir")

if __name__ == '__main__':
    mp = ManejaPacientes()
    ma = ManejaAtenciones()
    
    mp.carga()
    ma.carga()
    
    opcion = ''
    while opcion != 'x':
        menu()
        opcion = input("Ingrese una opción: ").lower()
        
        if opcion == 'a':
            fecha = input("Ingrese una fecha (dd/mm/aaaa): ")
            ma.atenciones_por_fecha(fecha)
        elif opcion == 'b':
            dni = input("Ingrese DNI: ")
            mp.informar_por_dni(dni, ma)
        elif opcion == 'c':
            mp.listar_sin_atencion(ma)
        elif opcion == 'd':
            mp.ordenar_y_mostrar()
        elif opcion == 'x':
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Intente de nuevo.")
    