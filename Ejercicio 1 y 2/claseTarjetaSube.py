class TarjetaSube:
    __saldo : int
    __numero : int
    def __init__(self, saldo, numero):
        self.__saldo = saldo
        self.__numero = numero
    def get_saldo(self):
        return self.__saldo
    def get_numero(self):
        return self.__numero
    def cargar_saldo(self, importe):
        if(importe > 0):
            self.__saldo += importe
        else:
            print("el importe debe ser mayor a cero pelotudo")
    
    def pagar_pasaje(self, importe):
        if(self.__saldo > 1000):
            self.__saldo -= importe
        else:
            print("saldo insuficiente")
    def consular_saldo(self):
        print(f"el saldo actual es: {self.__saldo}")
        
    def mostrar(self):
        print(f"numero : {self.get_numero}, saldo: {self.get_saldo}")        
             
        
