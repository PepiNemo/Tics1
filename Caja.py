class Caja:
    #TP=TiempoPromedio
    def __init__(self, TPMarcadoPProd, TPPagoCliente):
        self.Cola=[]
        self.Temporizador=0
        self.TPMarcadoPProd=TPMarcadoPProd
        self.TPPagoCliente=TPPagoCliente
        self.Temporizador=-1
        
    def AgregarCliente(self, Clien):
        self.Cola.insert(0,Clien)
    
    def AtenderSiguienteCliente(self):
        self.Temporizador=self.Cola.pop().NumProductos*self.TPMarcadoPProd+self.TPPagoCliente
        #La idea de este temporizador es ir restandolo con el For de la simulacion
        #No en este mismo metodo, si no en el mismo For



