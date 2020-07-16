from Pyth.fabricas import *

fabricas = [FabricaLG(), FabricaPanasonic()]

fabrica = fabricas[(int(input("Seleccione Fabrica:\n 0. LG\n 1. Panasonic")))]
productos = [fabrica.colorear(), fabrica.definirpulgadas(),fabrica.definirtipo()]
for i in productos:
    i.implementacion()
    i.operacion()
