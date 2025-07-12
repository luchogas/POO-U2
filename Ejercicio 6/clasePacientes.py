class Paciente:
    __dni: str
    __nombre: str
    __unidad: str
    def __init__(self, dni, nombre, unidad):
        self.__dni = dni
        self.__nombre = nombre
        self.__unidad = unidad

    def getDNI(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getUnidad(self):
        return self.__unidad
    
    def mostrar(self):
        print(f"DNI: {self.__dni}, Nombre: {self.__nombre}, Unidad: {self.__unidad}")
    
    def __lt__(self, otro):
       result = None
       if self.__unidad == otro.__unidad:
           result = self.__nombre < otro.__nombre
       else:
           result = self.__unidad < otro.__unidad
       return result

    


