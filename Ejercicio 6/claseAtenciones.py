class Atencion:
    __dni: str
    __fecha: str
    __importe: float
    def __init__(self, dni, fecha, importe):
        self.__dni = dni
        self.__fecha = fecha
        self.__importe = importe

    def getDNI(self):
        return self.__dni

    def getFecha(self):
        return self.__fecha

    def getImporte(self):
        return self.__importe
    def mostrar(self):
        print(f"DNI: {self.__dni}, Fecha: {self.__fecha}, Importe: {self.__importe}")
