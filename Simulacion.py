import Caja
import Cliente
from InterfazV2 import retornar
from FuncionesSimulacion import TemporizadorCajas
from FuncionesSimulacion import InsertarClienteCaja
from FuncionesSimulacion import TemporizadorClientes
from FuncionesSimulacion import CajaMenorCola
from FuncionesSimulacion import ObtenerDatosCajas
from FuncionesSimulacion import GenerarTabla



# ----------------------------------- Input ------------------------------------------------
# Datos Ingresados por el Cliente
entrada=retornar()
print(entrada)
HorasDeAtencion=entrada[2]
NumeroTotalClientes = entrada[3]

# Arreglos de 10 elementos para cada Intervalo
CajasAbiertas = entrada[4]
DistribucionPorcentual = entrada[5]
MinimoDeProductos=entrada[6]
MaximoDeProductos=entrada[7]
# Datos que iran en los atributos de las Clases
TPSeleccionProducto = entrada[8]
TPMarcadoCajaProducto = entrada[9]
TPPagoCliente = entrada[10]

# Listas para almacenar los datos pedidos
TiempoSimulado = []
ClientesIngresados = []
ClientesDespachados = []
ProductosDespachados = []
ColasPromedio = []
MaximaCola = []
TPEntraCliente=[]
for t in range(11):
    TiempoSimulado.append(0)
    ClientesIngresados.append(0)
    ClientesDespachados.append(0)
    ColasPromedio.append(0)
    ProductosDespachados.append(0)
    MaximaCola.append(0)
    TPEntraCliente.append(0)


#------------------------------------ Simulacion  ---------------------------------------------------------------------#

# Genarar Las Cajas de Un intervalo
Cajas = []
# Almacen de clientes Seleccionando Productos
ClientesSeleccionando = []
# Tiempo de cuanto segundo se simulan en la ejecucion del programa
#TPEntraCliente = int(3600 // (NumeroTotalClientes*DistribucionPorcentual[i]/100))

#Caso unico para poder completar los clientes ingresados diarios
Unico=False

for i in range(10):  # i =Intervalos

    print("Numero de intervalo : "+str(i+1))
    for j in range(CajasAbiertas[i]):
        # Abre las nuevas Cajas del Intervalo Correspondiente
        NuevaCaja = Caja.Caja(TPMarcadoCajaProducto, TPPagoCliente, i)
        Cajas.append(NuevaCaja)
    # Contador temporal del intervalo para el tamano de las colas de las cajas
    ContClientesCola = [0, 0]

    # Temporizador que indica cada cuanto entra un nuevo Cliente
    #print(float((DistribucionPorcentual[i]/100)))
    TPEntraCliente[i] = int(3600 // (NumeroTotalClientes*DistribucionPorcentual[i]/100))

    # Para que el contador de tiempo del intervalo comienze a contar considerando el tiempo transcurrido
    if(i > 0):
        TiempoSimulado[i] = TiempoSimulado[i-1]
        TPEntraCliente[i]=int(3600 // (NumeroTotalClientes * DistribucionPorcentual[i]/100))-TPEntraCliente[i-1]
        if(TPEntraCliente[i]<0):
            ClientesIngresados[i] = ClientesIngresados[i]+1
            NuevoCliente = Cliente.Cliente(TPSeleccionProducto,MinimoDeProductos,MaximoDeProductos)
            ClientesSeleccionando.append(NuevoCliente)
            TPEntraCliente[i] = int(3600 // (NumeroTotalClientes*DistribucionPorcentual[i]/100))


        print(TPEntraCliente[i])


    # Empieza el tiempo de un solo Intervalo
    for z in range(3600):
        # Corremos 1 segundo en los temporizadores
        TiempoSimulado[i] = TiempoSimulado[i]+1
        # Vista Clientes

        # Cuando el temporizador TPEntraCliente llega a 0 entra un nuevo Cliente
        
        if(TPEntraCliente[i] == 0 or Unico==False) :  # Entra un NuevoCliente
            Unico=True
            ClientesIngresados[i] = ClientesIngresados[i]+1
            NuevoCliente = Cliente.Cliente(TPSeleccionProducto,MinimoDeProductos,MaximoDeProductos)
            ClientesSeleccionando.append(NuevoCliente)
            TPEntraCliente[i] = int(3600 // (NumeroTotalClientes * DistribucionPorcentual[i]/100))
        #Restamos 1 al temporizador de entrada de clientes
        TPEntraCliente[i] = TPEntraCliente[i]-1

        # Quitar 1 segundos a los clientes seleccionando, para dps ir a Caja (Temporizador e InsertarCliente)
        TemporizadorClientes(ClientesSeleccionando, Cajas,
                             i, ContClientesCola, MaximaCola)

        # Vista Caja
        # Quitar 1 segundo a los clientes Seleccionando, para dps despachar
        TemporizadorCajas(Cajas, i, ClientesDespachados, ProductosDespachados, ContClientesCola, MaximaCola)

    # Almacenamos los contadores de la cola, para calcular el promedio de cola y lo almecenamos para dps generar el pdf
    ObtenerDatosCajas(Cajas, i, ClientesDespachados, ProductosDespachados)
    #Si no en un intervalo ningun cliente alcanza a estar en cola, con los if evitamos la division con 0
    if ContClientesCola[1]==0:
        ColasPromedio[i]=0
    else:
        ColasPromedio[i]=ContClientesCola[0]//ContClientesCola[1]


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
    ColasPromedio[i]=ContClientesCola[0]//ContClientesCola[1]
    ObtenerDatosCajas(Cajas, i, ClientesDespachados, ProductosDespachados)   


# Construccion de la tabla que mostrara los datos solicitados
GenerarTabla(TiempoSimulado, ClientesIngresados,ClientesDespachados,ProductosDespachados,ColasPromedio,MaximaCola)
