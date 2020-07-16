from abc import ABC, abstractmethod

class color(ABC):

    def implementacion(self):
        print("Coloreando ")
    @abstractmethod
    def operacion(self):
        pass

class pulgadas(ABC):
    def implementacion(self):
        print("Tamaño ")
    @abstractmethod
    def operacion(self):
        pass

class tipo(ABC):
    def implementacion(self):
        print("Tipo: ")
    @abstractmethod
    def operacion(self):
        pass
 
class colorLG(color):
    def operacion(self):
        print("Color LG Azul")
class pulgadasLG(pulgadas):
    def operacion(self):
        print("LG 42Pulgadas")
class tipoLG(tipo):
    def operacion(self):
        print("LG LCD")

class colorPanasonic(color):
    def operacion(self):
        print("Color Panasonic Azul")
class pulgadasPanasonic(pulgadas):
    def operacion(self):
        print("Panasonic 42Pulgadas")
class tipoPanasonic(tipo):
    def operacion(self):
        print("Panasonic LCD")



