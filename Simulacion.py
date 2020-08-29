import Caja
import Cliente
from FuncionesSimulacion import TemporizadorCajas
from FuncionesSimulacion import InsertarClienteCaja
from FuncionesSimulacion import TemporizadorClientes
from FuncionesSimulacion import CajaMenorCola
from FuncionesSimulacion import ObtenerDatosCajas

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
#Tiempo de cuanto segundo se simulan en la ejecucion del programa
TiempoSimulado=0

for i in range(10):#i =Intervalos
    print("Numero de intervalo :"+str(i))
    for j in range(CajasAbiertas[i]):
        #Abre las nuevas Cajas del Intervalo Correspondiente
        NuevaCaja = Caja.Caja(TPMarcadoCajaProducto, TPPagoCliente, i)
        Cajas.append(NuevaCaja)


    # Temporizador que indica cada cuanto entra un nuevo Cliente
    TPEntraCliente = 3600 // (NumeroTotalClientes*DistribucionPorcentual[i])

    #Variables para los requerimientos
    #Contador Clientes por Intervalo que entraron
    ContClientesEntraron=0
    #Cantidad de clientes despachados
    ContClientesDesp=[0]
    #Promedio de productos por cliente despachado (Cont/Cantidad clientes despachados) 
    ContProductosDesp=[0]
    #Promedio de clientes en espera en colas de Caja (Cont/Cantidad clientes Entraron)
    ContClientesCola=[0,0]
    #Longitud máxima de cola de espera de Caja
    MaxCola=[0] 

    # Empieza el tiempo de un solo Intervalo
    for z in range(3600):
        # Corremos 1 segundo en los temporizadores
        TiempoSimulado=TiempoSimulado+1
        # Vista Clientes

        # Cuando el temporizador TPEntraCliente llega a 0 entra un nuevo Cliente
        TPEntraCliente = TPEntraCliente-1
        if(TPEntraCliente == 0 or z == 0): # Entra un NuevoCliente
            ContClientesEntraron=ContClientesEntraron+1
            NuevoCliente = Cliente.Cliente(TPSeleccionProducto)
            ClientesSeleccionando.append(NuevoCliente)
            TPEntraCliente = 3600 // (NumeroTotalClientes*DistribucionPorcentual[i])

        # Quitar 1 segundos a los clientes seleccionando, para dps ir a Caja (Temporizador e InsertarCliente)
        TemporizadorClientes(ClientesSeleccionando, Cajas, i,ContClientesCola,MaxCola)

        # Vista Caja
        # Quitar 1 segundo a los clientes Seleccionando, para dps despachar
        TemporizadorCajas(Cajas,i,ContClientesDesp,ContProductosDesp)

    ObtenerDatosCajas(Cajas,ContClientesDesp,ContProductosDesp)
    print("Tiempo simulado :"+str(TiempoSimulado)+"(s)")
    print("Clientes que Entraron :"+str(ContClientesEntraron))
    print("Clientes despachados :"+str(ContClientesDesp))
    print("Productos despachados :"+str(ContProductosDesp))
    print("Colas Promedio del Intervalo :"+str(ContClientesCola[0]//ContClientesCola[1]))
    print("Maxima Cola del Intervalo :"+str(MaxCola[0]))
    print()

"""
Requerimientos
Tiempo total simulado en minutos yes
-Para cada intervalo del horario de atención:
-Cantidad de clientes ingresados yes
-Cantidad de clientes despachados yes 
-Promedio de productos por clientedespachado\
    Para esto crear un atributo de la caja, CantProductoCliente, que se setea cuando se AtiendeCliente(),
    , para cuando el temporizador llegue a sero, sumarlo al contador de producto de clientes despachados
-Promedio de clientes en espera en colas de Caja
-Longitud máxima de cola de espera de Caja /
"""

