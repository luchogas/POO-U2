class Carrera:
    __codigo: int
    __nombre: str
    __fecha_inicio: str
    __duracion: int
    __titulo: str
    __codigo_facultad: int

    def __init__(self, codigo, nombre, fecha_inicio, duracion, titulo, codigo_facultad):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__duracion = duracion
        self.__titulo = titulo
        self.__codigo_facultad = codigo_facultad

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getFechaInicio(self):
        return self.__fecha_inicio

    def getDuracion(self):
        return self.__duracion

    def getTitulo(self):
        return self.__titulo

    def getCodigoFacultad(self):
        return self.__codigo_facultad
    def mostrar(self):
        print(self.__codigo, self.__nombre, self.__fecha_inicio, self.__duracion, self.__titulo, self.__codigo_facultad)
    
    def __lt__(self, otroNombre):
        return self.__nombre < otroNombre