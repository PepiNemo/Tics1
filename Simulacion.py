import Caja
import Cliente
from FuncionesSimulacion import TemporizadorCajas
from FuncionesSimulacion import InsertarClienteCaja
from FuncionesSimulacion import TemporizadorClientes
from FuncionesSimulacion import CajaMenorCola
from FuncionesSimulacion import ObtenerDatosCajas
from FuncionesSimulacion import GenerarTabla


# ----------------------------------- Input ------------------------------------------------
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


# Listas para almacenar los datos pedidos
TiempoSimulado = []
ClientesIngresados = []
ClientesDespachados = []
ProductosDespachados = []
ColasPromedio = []
MaximaCola = []
for t in range(11):
    TiempoSimulado.append(0)
    ClientesIngresados.append(0)
    ClientesDespachados.append(0)
    ProductosDespachados.append(0)
    MaximaCola.append(0)


#------------------------------------ Simulacion  ---------------------------------------------------------------------#

# Genarar Las Cajas de Un intervalo
Cajas = []
# Almacen de clientes Seleccionando Productos
ClientesSeleccionando = []
# Tiempo de cuanto segundo se simulan en la ejecucion del programa


for i in range(10):  # i =Intervalos

    print("Numero de intervalo : "+str(i+1))
    for j in range(CajasAbiertas[i]):
        # Abre las nuevas Cajas del Intervalo Correspondiente
        NuevaCaja = Caja.Caja(TPMarcadoCajaProducto, TPPagoCliente, i)
        Cajas.append(NuevaCaja)
    # Contador temporal del intervalo para el tamano de las colas de las cajas
    ContClientesCola = [0, 0]

    # Temporizador que indica cada cuanto entra un nuevo Cliente
    TPEntraCliente = 3600 // (NumeroTotalClientes*DistribucionPorcentual[i])

    # Para que el contador de tiempo del intervalo comienze a contar considerando el tiempo transcurrido
    if(i > 0):
        TiempoSimulado[i] = TiempoSimulado[i-1]

    # Empieza el tiempo de un solo Intervalo
    for z in range(3600):
        # Corremos 1 segundo en los temporizadores
        TiempoSimulado[i] = TiempoSimulado[i]+1
        # Vista Clientes

        # Cuando el temporizador TPEntraCliente llega a 0 entra un nuevo Cliente
        TPEntraCliente = TPEntraCliente-1
        if(TPEntraCliente == 0 or z == 0):  # Entra un NuevoCliente
            ClientesIngresados[i] = ClientesIngresados[i]+1
            NuevoCliente = Cliente.Cliente(TPSeleccionProducto)
            ClientesSeleccionando.append(NuevoCliente)
            TPEntraCliente = 3600 // (NumeroTotalClientes *
                                      DistribucionPorcentual[i])

        # Quitar 1 segundos a los clientes seleccionando, para dps ir a Caja (Temporizador e InsertarCliente)
        TemporizadorClientes(ClientesSeleccionando, Cajas,
                             i, ContClientesCola, MaximaCola)

        # Vista Caja
        # Quitar 1 segundo a los clientes Seleccionando, para dps despachar
        TemporizadorCajas(Cajas, i, ClientesDespachados, ProductosDespachados, ContClientesCola, MaximaCola)

    # Almacenamos los contadores de la cola, para calcular el promedio de cola y lo almecenamos para dps generar el pdf
    ColasPromedio.append(ContClientesCola[0]//ContClientesCola[1])
    ObtenerDatosCajas(Cajas, i, ClientesDespachados, ProductosDespachados)   


# Tiempo Extra
i=10
TiempoExtra=False
if(len(Cajas) > 0 or len(ClientesSeleccionando) > 0):
    # Para que el contador de tiempo del intervalo comienze a contar considerando el tiempo transcurrido
    TiempoSimulado[i] = TiempoSimulado[i-1]
    # Contador temporal del intervalo para el tamano de las colas de las cajas
    ContClientesCola = [0, 0]
    TiempoExtra=True

while(len(Cajas) > 0 or len(ClientesSeleccionando) > 0):

    TiempoSimulado[i] = TiempoSimulado[i]+1
    # Quitar 1 segundos a los clientes seleccionando, para dps ir a Caja (Temporizador e InsertarCliente)
    TemporizadorClientes(ClientesSeleccionando, Cajas,
                         i,ContClientesCola, MaximaCola)

    # Vista Caja
    # Quitar 1 segundo a los clientes Seleccionando, para dps despachar
    TemporizadorCajas(Cajas, i, ClientesDespachados, ProductosDespachados, ContClientesCola, MaximaCola)

#Si Hubo tiempo Extra almacenar los contadores para los requerimientos del programa, tamano Colas, Clientes despachados y Productos Despachados
if(TiempoExtra== True):
    print("Numero de intervalo :","TiempoExtra")
    # Almacenamos los contadores de la cola, para calcular el promedio de cola y lo almecenamos para dps generar el pdf
    ColasPromedio.append(ContClientesCola[0]//ContClientesCola[1])
    ObtenerDatosCajas(Cajas, i, ClientesDespachados, ProductosDespachados)   


# Construccion de la tabla que mostrara los datos solicitados
GenerarTabla(TiempoSimulado, ClientesIngresados,ClientesDespachados,ProductosDespachados,ColasPromedio,MaximaCola)
