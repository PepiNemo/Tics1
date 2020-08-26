import Caja
import Cliente
from FuncionesSimulacion import TemporizadorCajas
from FuncionesSimulacion import InsertarClienteCaja
from FuncionesSimulacion import TemporizadorClientes
from FuncionesSimulacion import CajaMenorCola

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
