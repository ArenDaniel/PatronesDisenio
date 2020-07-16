from abc import ABC, abstractmethod
from .productos import *

class FabricaAbstracta(ABC):
    @abstractmethod
    def colorear(self):
        pass
    @abstractmethod
    def definirpulgadas(self):
        pass
    @abstractmethod
    def definirtipo(self):
        pass

class FabricaLG(FabricaAbstracta):
    def colorear(self):
        return colorLG()
    def definirpulgadas(self):
        return pulgadasLG()
    def definirtipo(self):
        return tipoLG()

class FabricaPanasonic(FabricaAbstracta):
    def colorear(self):
        return colorPanasonic()
    def definirpulgadas(self):
        return pulgadasPanasonic()
    def definirtipo(self):
        return tipoPanasonic()


