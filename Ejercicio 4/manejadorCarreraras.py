import csv
import numpy as np
from claseCarrera import Carrera
class manejadorCarrera:
    __Carreras = []
    def __init__(self):
        __Carreras = np.array(6)
    
    def getCarrera(self):
        return self.__Carreras
    
    def cargar(self):
        archivo = open("Carreras.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            codigo = str(fila[0])
            nombre = str(fila[1])
            fecha_inicio = str(fila[2])
            duracion = str(fila[3])
            titulo = str(fila[4])
            codigo_facultad = str(fila[5])
            self.__Carreras.append(Carrera(codigo, nombre, fecha_inicio, duracion, titulo, codigo_facultad))   
    def listar(self):
        for i in self.__Carreras:
            i.mostrar()
            
    def buscar_carrera(self, nom):
        band = False
        i = 0
        long = len(self.__Carreras)
        while i < long and not band:
            if (self.__Carreras[i].getNombre().lower() == nom.lower()): 
                band = True

                i+=1
        if(band == True):
            
            return self.__Carreras[i].getCodigo()
        else:
            print("error")
    def mostrarDatos(self, idfacultad, nombre):
        j = 0
        lcarreras =[]
        long = len(self.__Carreras)
        while j < long:
            if(self.__Carreras[j].getCodigoFacultad() == idfacultad):
                lcarreras.append(self.__Carreras[j])
            j += 1
        lcarreras.sort()
        
        longCarreras = len(lcarreras)
        print("carreras de la ", nombre)
        for i in range(len(lcarreras)):
            print(lcarreras[i].getNombre(), "", lcarreras[i].getDuracion())    
                