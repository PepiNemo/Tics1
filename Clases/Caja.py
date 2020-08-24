import Cliente
class Caja:
    def __init__(self, TiempoMarcadoPProd):
        self.Cola=[]
        self.Temporizador=0
        self.TiempoMarcadoPProd=TiempoMarcadoPProd
        

    def AgregarCliente(self, Clien):
        self.Cola.insert(0,Clien)
    
    def AtenderCliente(self):
        self.Temporizador=self.Cola.pop().NumProductos*self.TiempoMarcadoPProd
        #La idea de este temporizador es ir restandolo con el For de la simulacion
        #No en este mismo metodo, si no en el mismo For

#Creamos un Cliente que por defecto tiene 20 productos
felipe =Cliente.Cliente(3)#El parametro es cuanto tardo en selecionar los prod
#Creamos una Caja que el tiempo de marcado por producto es 2(Segundos)
caj=Caja(2)
#Agregamos a la Cola de la Caja un (Clase)Cliente
caj.AgregarCliente(felipe)
#Imprimmos la cola, para ver si se agrego el Cliente
print(caj.Cola)
#Inicializar el Temporizador de la atencion del cliente, si llega a 0 atendemos otro Cliente
caj.AtenderCliente()
print(caj.Temporizador)

