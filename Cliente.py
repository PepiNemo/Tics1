import random

class Cliente:
    def __init__(self, TiempoSeleccionPProd):
        self.NumProductos=self.CantidadProductos()
        self.Temporizador=self.TiempoSeleccionProductos(TiempoSeleccionPProd)

    def CantidadProductos(self, c1, c2):
        ran = random.randint(c1,c2)
        return ran

    def TiempoSeleccionProductos(self,TiempoSeleccionPProd):
        return TiempoSeleccionPProd*self.NumProductos