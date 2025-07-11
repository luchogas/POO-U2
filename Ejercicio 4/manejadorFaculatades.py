import csv
import numpy as np
from claseFacultad import Facultad
class manejadorFac:
    __facultades = []
    def __init__(self):
        __facultades = np.array(6)
    
    def cargar(self):
        archivo = open("Facultades.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            codigo = str(fila[0])
            nombre = str(fila[1])
            direccion = str(fila[2])
            localidad = str(fila[3])
            telefono = str(fila[4])
            self.__facultades.append(Facultad(codigo, nombre, direccion, localidad, telefono))        
    def listar(self):
        for i in self.__facultades:
            i.mostrar()
            
    #def listar_otraForma(self):
        #long = len(self.__facultades)
        #for i in range(long):
            #self.__facultades[i].mostrar()
    def buscar_nombre_porID(self, id):
        band = False
        i = 0
        long = len(self.__facultades)
        while i < long and not band:
            if(self.__facultades[i].getCodigo() == id):
                band = True
            else:
                i+=1
        if(band == True):
            return self.__facultades[i].getNombre()
        else:
            print("no encontrado")

    def cantCarreras(self, listaCarrera):
        long =  len(listaCarrera)
        for i in self.__facultades:
            indice = i.getCodigo()
            j = 0
            cont = 0
            while j < long:
                if(listaCarrera[j].getCodigoFacultad() == indice):
                    cont += 1   
                j += 1
            print("facultad ", i.getNombre(), "tiene: ", cont, "carreras")
    
    def buscarFacultadporNombre(self, nombre):
        band = False
        long = len(self.__facultades)
        i = 0
        while 1 < long and not band:
            if(self.__facultades[i].getNombre() == nombre):
                band = True
            else:
                i += 1
        if(band == True):
            return self.__facultades[i].getCodigo()
        else:
            print("no encontrado")