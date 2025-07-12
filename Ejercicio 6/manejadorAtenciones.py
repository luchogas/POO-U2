import csv
import numpy as np
from claseAtenciones import Atencion

class ManejaAtenciones:
    __atenciones = np.ndarray
    __cantidad = int
    __dimension = int
    def __init__(self):
        self.__atenciones = np.empty(48, dtype=Atencion)
        self.__cantidad = 0
        self.__dimension = 48
    
    def getAtenciones(self):
        
        return self.__atenciones

    def mostrarA(self):
        for atencion in self.__atenciones:
            atencion.mostrar()
            
    def agregar(self, unaAtencion):
        if self.__cantidad < self.__dimension:
            self.__atenciones[self.__cantidad] = unaAtencion
            self.__cantidad += 1
        else:
            print("No se pueden agregar más atenciones.")
    
    def carga(self):
        archivo = open("atenciones.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader: 
            dni = str(fila[0])
            fecha = str(fila[1])
            importe = float(fila[2])
            self.agregar(Atencion(dni, fecha, importe))
        archivo.close()
        
    def atenciones_por_fecha(self, fecha):
        importTotal = 0
        cont = 0
        i = 0
        while i < self.__cantidad:
            if self.__atenciones[i].getFecha() == fecha:
                cont += 1
                importTotal += (self.__atenciones[i].getImporte())
            i += 1
        print(f"Total de atenciones en la fecha {fecha}: {cont}")
        print(f"Importe total: {importTotal}")
        
    def atenciones_por_dni(self, dni):
        cont = 0
        i = 0
        while i < self.__cantidad:
            if self.__atenciones[i].getDNI() == dni:
                cont += 1
            i += 1
        return cont

        
