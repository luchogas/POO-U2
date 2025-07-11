from claseTarjetaSube import TarjetaSube
class ControladorSube:
    __listaSube = []
    def __init__(self):
        self.__listaSube = []
    
    def agregar(self, tarjeta):
        if type(tarjeta) == TarjetaSube:
            self.__listaSube.append(tarjeta)
            
    def mostrar(self):
        i = 0
        long = len(self.__listaSube)
        for i in range(long):
            print("i=", i)
            print("numero: ",self.__listaSube[i].get_numero(), "saldo: ",self.__listaSube[i].get_saldo())
               
    def recorre(self):
        long = len(self.__listaSube)
        for i in range (long):
            if(self.__listaSube[i].get_saldo() < 0):
                print(f"el numero con saldo negativo es: ",self.__listaSube[i].get_numero())
                
    def buscar(self, nro):
        long = len(self.__listaSube)
        i = 0
        band = False
        while i < long and band == False:
            if(self.__listaSube[i].get_numero() == nro):
                band = True
            else:
                i+=1    
        if band == True:
            print("el saldo es: $",self.__listaSube[i].get_saldo())
        else:
            print("no encontrado")        
                            
    