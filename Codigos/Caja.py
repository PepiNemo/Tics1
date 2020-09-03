import Cliente

class Caja:
    def __init__(self, TPMarcadoPProd, TPPagoCliente,Intervalo):
        self.Temporizador=-1
        self.Intervalo=Intervalo
        self.Cola=[]
        self.TPMarcadoPProd=TPMarcadoPProd
        self.TPPagoCliente=TPPagoCliente
        self.ClientesDespachados=0
        self.ProductosDespachados=0
        self.TempProductosEnCaja=0

    def AgregarCliente(self, Clien):
        self.Cola.insert(0,Clien)
    
    def AtenderSiguienteCliente(self):
        SiguienteCliente=self.Cola.pop()
        self.TempProductosEnCaja=SiguienteCliente.NumProductos
        self.Temporizador=SiguienteCliente.NumProductos*self.TPMarcadoPProd+self.TPPagoCliente

    def DespacharCliente(self):
        self.ClientesDespachados =self.ClientesDespachados+1
        self.ProductosDespachados=self.ProductosDespachados+self.TempProductosEnCaja




