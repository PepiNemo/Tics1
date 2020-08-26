import Caja
import Cliente


def TemporizadorCajas(Cajas,Intervalo):
    for i in range(len(Cajas)):

        if(Cajas[i].Temporizador > 0):
            Cajas[i].Temporizador = Cajas[i].Temporizador-1

        elif(Cajas[i].Temporizador == 0):

            # Si tiene mas clientes en cola, que Atienda al Siguiente
            Cajas[i].AtenderSiguienteCliente()

            # Si no tiene mas Clientes en cola Deja de Atender
            if ( len(Cajas[i].Cola)==0 ):
                #Si la caja que estaba atendiendo, no es del intervalo actual, y ya no tiene mas Cliente, la Caja se elimina
                if(Cajas[i].Intervalo!=Intervalo):
                    Cajas.remove(i)
                else :
                    #Si la Caja si es del intervalo, solo deja de antender, hasta tener Clientes
                    Cajas[i].Temporizador = -1
            


def TemporizadorClientes(ClientesSeleccionando, Cajas, InterValo):
    # Escribir Logica
    # Recorrer ClientesSeleccionando y quitarle 1 segundos a su temporizador
    # Si el temporizador llega a 0 Insertar en la caja Mas Vacia

    for i in range(len(ClientesSeleccionando)):

        if(ClientesSeleccionando[i].Temporizador > 0):
            # Restamos los temporizadores
            ClientesSeleccionando[i].Temporizador = ClientesSeleccionando[i].Temporizador-1

        elif(ClientesSeleccionando[i].Temporizador == 0):
            #Mandamos al Cliente a la Caja con Menor Cola
            IndiceCajaMasVacia = CajaMenorCola(Cajas, InterValo)
            InsertarClienteCaja(i, Cajas, IndiceCajaMasVacia)


def CajaMenorCola(Cajas, Intervalo):
    # Retorna el Indice de la Caja con la Fila mas Corta de las Intervalo Actual
    return 2

def InsertarClienteCaja(IndiceClienteSelecccionando, Cajas, IndiceCajaMasVacia):
    Cajas[IndiceCajaMasVacia].AgregarCliente(ClientesSeleccionando[i])
    # Si la caja no estaba atendiendo
    if(Cajas[IndiceCajaMasVacia].Temporizador == -1):
        # Que comience a atender inicializando el Temporizador
        Cajas[IndiceCajaMasVacia].AtenderSiguienteCliente()


#----------------------------------- Input ------------------------------------------------
# Datos Ingresados por el Cliente
NumeroTotalClientes = 1200

# Arreglos de 10 elementos para cada Intervalo
CajasAbiertas = [5, 5, 5, 10, 10, 10, 15, 15, 10, 10]
DistribucionPorcentual = [0.05, 0.07, 0.09,
                          0.11, 0.14, 0.14, 0.09, 0.07, 0.11, 0.13]
# Datos que iran en los atributos de las Clases
# TP=TiempoPromedio
TPSeleccionProducto = 30
TPMarcadoCajaProducto = 10
TPPagoCliente = 45


####################################  Simulacion  ############################

# Genarar Las Cajas de Un intervalo
Cajas = []
# Almacen de clientes Seleccionando Productos
ClientesSeleccionando = []
for i in range(10):#i =Intervalos
    print("Numero de intervalo :"+str(i))
    for j in range(CajasAbiertas[i]):
        #Abre las nuevas Cajas del Intervalo Correspondiente
        NuevaCaja = Caja.Caja(TPMarcadoCajaProducto, TPPagoCliente, i)
        Cajas.append(NuevaCaja)


    # Temporizador que indica cada cuanto entra un nuevo Cliente
    TPEntraCliente = 3600 // (NumeroTotalClientes*DistribucionPorcentual[i])

    # Empieza el tiempo de un solo Intervalo
    for z in range(3600):
        # Corremos 1 segundo en los temporizadores

        # Vista Clientes

        # Cuando el temporizador TPEntraCliente llega a 0 entra un nuevo Cliente
        TPEntraCliente = TPEntraCliente-1
        if(TPEntraCliente == 0 or z == 0):  # Entra un NuevoCliente
            NuevoCliente = Cliente.Cliente(TPSeleccionProducto)
            ClientesSeleccionando.append(NuevoCliente)
            TPEntraCliente = 3600 // (NumeroTotalClientes*DistribucionPorcentual[i])

        # Quitar 1 segundos a los clientes seleccionando, para dps ir a Caja (Temporizador e InsertarCliente)
        TemporizadorClientes(ClientesSeleccionando, Cajas, i)

        # Vista Caja
        # Quitar 1 segundo a los clientes Seleccionando, para dps despachar
        TemporizadorCajas(Cajas,i)
