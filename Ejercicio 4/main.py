from claseCarrera import Carrera
from claseFacultad import Facultad
from manejadorCarreraras import manejadorCarrera
from manejadorFaculatades import manejadorFac

if __name__ =='__main__':
    manejadorF = manejadorFac()
    manejadorF.cargar()
    print("------FACULTADES-------")
    manejadorF.listar()
    print("\n")
    manejadorCarre = manejadorCarrera()
    manejadorCarre.cargar()
    print("------CARRERAS-------")
    manejadorCarre.listar()
    
 #  nomC = input("ingrese nombre de la carrera: ")
 #  id = manejadorCarre.buscar_carrera(nomC)
 #  nomF = manejadorF.buscar_nombre_porID(id)
 #  print("la carrera", nomC, "se dicta en la facultad de : ", nomF)
    
    #manejadorF.cantCarreras(manejadorCarre.getCarrera())
    
    nombre = input("ingrese el nombre de la facultad a buscar: ")
    idfacultad = manejadorF.buscarFacultadporNombre(nombre)
    
    manejadorCarre.mostrarDatos(idfacultad, nombre)
    
    
    
    
    
    
    
    
    