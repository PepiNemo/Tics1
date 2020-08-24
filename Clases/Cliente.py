class Cliente:
    def __init__(self, TiempoSeleccionPProd):
        self.NumProductos=self.CantidadProductos()
        self.TiempoSeleccion=self.TiempoSeleccionProductos(TiempoSeleccionPProd)

    def CantidadProductos(self):
        return 20
        #El aleatorio entra c1 y c2

    def TiempoSeleccionProductos(self,TiempoSeleccionPProd):
        return TiempoSeleccionPProd*self.NumProductos

    def PrintAtributos(self):
        print(self.NumProductos)
        print(self.TiempoSeleccion)

