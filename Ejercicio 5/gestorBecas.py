from becas import Beca
from beneficiarios import Beneficiario
import csv
class GestorBeca:
    __listaBecas = list
    def __init__(self):
        self.__listaBecas = []
    def get_listaBeca(self):
        return self.__listaBecas
    def mostrar(self):
        for beca in self.__listaBecas:
            beca.mostrar()
    def cargar(self):
        archivo = open("becas.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            id = int(fila[0])
            tipo = str(fila[1])
            importe = float(fila[2])
            self.__listaBecas.append(Beca(id, tipo, importe))
        archivo.close()
    def buscarBeca(self, tipo, gestorBeneficiario):
        for beca in self.__listaBecas:
            if beca.get_tipo() == tipo:
                print("Beca encontrada:")
                beca.mostrar()
                print("Beneficiarios de la beca:")
                for beneficiario in gestorBeneficiario.get_arregloBene():
                    if beneficiario.get_idBecaAsignada() == beca.get_id():
                        beneficiario.mostrar()
                return
        print("No se encontró la beca con el tipo especificado.")
