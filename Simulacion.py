import Caja
import Cliente


def CajaMenorCola(Caja):
    return 3


def TemporizadorClientes(ClientesSeleccionando, Cajas, IndiceCajaMasVacia):
    # Escribir Logica
    # Recorrer ClientesSeleccionando y quitarle 1 segundos a su temporizador
    # Si el temporizador llega a 0 Insertar en la caja Mas Vacia

    for i in range(len(ClientesSeleccionando)):
        if(ClientesSeleccionando[i].Temporizador <= 0):
            Cajas[IndiceCajaMasVacia].AgregarCliente(ClientesSeleccionando[i])
            IndiceCajaMasVacia = CajaMenorCola(Cajas)
            # Si la caja no estaba atendiendo
            if(Cajas[IndiceCajaMasVacia].Temporizador == -1):
                # Que comience a atender inicializando el Temporizador
                Cajas[IndiceCajaMasVacia].AtenderSiguienteCliente()

        # Restamos los temporizadores
        ClientesSeleccionando[i].Temporizador = ClientesSeleccionando[i].Temporizador-1


def TemporizadorCajas(Cajas):
    for i in range(len(Cajas)):

        if(Cajas[i].Temporizador > 0):
            Cajas[i].Temporizador = Cajas[i].Temporizador-1

        elif(Cajas[i].Temporizador == 0):
            # Si no tiene mas Clientes Deja de Atender
            if not Cajas[i].Cola:
                Cajas[i].Temporizador = -1

            # Si tiene mas clientes en cola, que Atienda al Siguiente
            Cajas[i].AtenderSiguienteCliente()


# Datos Ingresados por el Cliente
NumeroTotalClientes = 1200

# Arreglos de 10 elementos para cada Intervalo
CajasAbiertas = 15
DistribucionPorcentual = 1200*0.33
# Datos que iran en los atributos de las Clases
# TP=TiempoPromedio
TPSeleccionProducto = 30
TPMarcadoCajaProducto = 10
TPPagoCliente = 45


####################################  Simulacion  ############################

# Genarar Las Cajas de Un intervalo
Cajas = []
for i in range(CajasAbiertas):
    NuevaCaja = Caja.Caja(TPMarcadoCajaProducto, TPPagoCliente)
    Cajas.append(NuevaCaja)

#Almacen de clientes Seleccionando Productos
ClientesSeleccionando = []


# Cada cuanto (s)entrara el siguiente cliente ("Los clientes se distribuyen de forma uniforme en el tiempo")
TPEntraCliente = 3600 // DistribucionPorcentual
#Ha que caja ira el proximo Cliente
IndiceCajaMasVacia = CajaMenorCola(Cajas)

# Empieza el tiempo de un Intervalo
for j in range(3600):  
    # Corremos 1 segundo en los temporizadores

    # Vista Clientes

    #Entradas de los Clientes
    TPEntraCliente = TPEntraCliente-1
    if(TPEntraCliente == 0 or j==0):  # Entra un NuevoCliente
        NuevoCliente = Cliente.Cliente(TPSeleccionProducto)
        ClientesSeleccionando.append(NuevoCliente)
        TPEntraCliente = 3600/DistribucionPorcentual

    # Quitar 1 segundos a los clientes seleccionando, para dps ir a Caja
    TemporizadorClientes(ClientesSeleccionando, Cajas, IndiceCajaMasVacia)

    # Vista Caja
    # Quitar 1 segundo a los clientes Seleccionando, para dps despachar
    TemporizadorCajas(Cajas)


