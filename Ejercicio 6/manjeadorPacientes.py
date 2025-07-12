import csv
from clasePacientes import Paciente

class ManejaPacientes:
    __listaPacientes = list
    def __init__(self):
        self.__listaPacientes = []
       
    def getPacientes(self):
        return self.__listaPacientes  
    
    def mostrar(self):
        for paciente in self.__listaPacientes:
            paciente.mostrar()
    
            
    def carga(self):
        archivo = open("pacientes.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader: 
            dni = str(fila[0])
            nombre = str(fila[1])
            unidad = str(fila[2])
            self.__listaPacientes.append(Paciente(dni, nombre, unidad))
            
    def informar_por_dni(self, dni, ma):
        i = 0
        longitud = len(self.__listaPacientes)
        while i < longitud:
            if self.__listaPacientes[i].getDNI() == dni:    
                print(f"Nombre: {self.__listaPacientes[i].getNombre()}")    
                print(f"Unidad: {self.__listaPacientes[i].getUnidad()}")
                print(f"Atenciones: {ma.atenciones_por_dni(dni)}")
                return
            i += 1
        print("Paciente no encontrado.")
        
    def listar_sin_atencion(self, ma):
        i = 0
        longitud = len(self.__listaPacientes)
        while i < longitud:
            if  ma.atenciones_por_dni(self.__listaPacientes.getDNI()) == 0:
                print(f"Paciente sin atenciones: {self.__listaPacientes.getNombre()} - DNI: {self.__listaPacientes.getDNI()}")
    
    def ordenar_y_mostrar(self):
        self.__listaPacientes.sort()
        for paciente in self.__listaPacientes:
            paciente.mostrar()
            
