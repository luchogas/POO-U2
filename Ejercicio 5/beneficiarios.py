class Beneficiario:
    __dni : str
    __nombre : str
    __apellido : str
    __carrera : str
    __facultad : str
    __anioCursa : int
    __promedio : float
    __idBecaAsignada : int
    def __init__(self, dni, nombre, apellido, carrera, facultad, anioCursa, promedio, idBecaAsignada):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carrera = carrera
        self.__facultad = facultad
        self.__anioCursa = anioCursa
        self.__promedio = promedio
        self.__idBecaAsignada = idBecaAsignada
    def get_dni(self):
        return self.__dni
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_carrera(self):
        return self.__carrera
    def get_facultad(self):
        return self.__facultad
    def get_anioCursa(self):
        return self.__anioCursa
    def get_promedio(self):
        return self.__promedio
    def get_idBecaAsignada(self):
        return self.__idBecaAsignada
    def mostrar(self):
        print(f'DNI: {self.__dni}, Nombre: {self.__nombre}, Apellido: {self.__apellido}, Carrera: {self.__carrera}, Facultad: {self.__facultad}, Anio Cursa: {self.__anioCursa}, Promedio: {self.__promedio}, ID Beca Asignada: {self.__idBecaAsignada}')
    
    
    