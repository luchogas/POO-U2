from beneficiarios import Beneficiario
import csv
import numpy as np

class GestorBene:
    __arregloBene: np.ndarray
    __cantidad : int
    __dimension : int
    def __init__(self):
        self.__arregloBene = np.empty(14, dtype=Beneficiario)
        self.__cantidad = 0
        self.__dimension = 14
    def get_arregloBene(self):
        return self.__arregloBene
    def mostrar(self):
        for beneficiario in self.__arregloBene:
            beneficiario.mostrar()
    def agregar(self, unBeneficiario):
        if self.__cantidad < self.__dimension:
            self.__arregloBene[self.__cantidad] = unBeneficiario
            self.__cantidad += 1
        else:
            print("no se puede agregar mas")
    def cargar(self):
        archivo = open("beneficiarios.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            dni = int(fila[0])
            nombre = str(fila[1])
            apellido = str(fila[2])
            carrera = str(fila[3])
            facultad = str(fila[4])
            anioCursa = int(fila[5])
            promedio = float(fila[6])
            idBecaAsignada = int(fila[7])
            self.agregar(Beneficiario(dni, nombre, apellido, carrera, facultad, anioCursa, promedio, idBecaAsignada))
        archivo.close() 
    
    
            
    
    
    