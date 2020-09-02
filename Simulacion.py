import Caja
import Cliente
from FuncionesSimulacion import TemporizadorCajas
from FuncionesSimulacion import InsertarClienteCaja
from FuncionesSimulacion import TemporizadorClientes
from FuncionesSimulacion import CajaMenorCola
from FuncionesSimulacion import ObtenerDatosCajas
from FuncionesSimulacion import GenerarPDF


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
for t in range (10):
    TiempoSimulado.append(0)
    ClientesIngresados.append(0)
    ClientesDespachados.append(0)
    ProductosDespachados.append(0)
    MaximaCola.append(0)


####################################  Simulacion  ############################

# Genarar Las Cajas de Un intervalo
Cajas = []
# Almacen de clientes Seleccionando Productos
ClientesSeleccionando = []
# Tiempo de cuanto segundo se simulan en la ejecucion del programa


for i in range(10):  # i =Intervalos

    print("Numero de intervalo :"+str(i+1))
    for j in range(CajasAbiertas[i]):
        # Abre las nuevas Cajas del Intervalo Correspondiente
        NuevaCaja = Caja.Caja(TPMarcadoCajaProducto, TPPagoCliente, i)
        Cajas.append(NuevaCaja)
    #Contador temporal del intervalo para el tamano de las colas de las cajas
    ContClientesCola=[0,0]

    # Temporizador que indica cada cuanto entra un nuevo Cliente
    TPEntraCliente = 3600 // (NumeroTotalClientes*DistribucionPorcentual[i])


    #Para que el contador de tiempo del intervalo comienze a contar considerando el tiempo transcurrido
    if(i>0):
        TiempoSimulado[i]=TiempoSimulado[i-1]

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
        TemporizadorCajas(Cajas, i, ClientesDespachados, ProductosDespachados)

    ObtenerDatosCajas(Cajas, i, ClientesDespachados, ProductosDespachados)
    #Almacenamos los contadores de la cola, para calcular el promedio de cola y lo almecenamos para dps generar el pdf  
    ColasPromedio.append(ContClientesCola[0]//ContClientesCola[1]) 



# Construccion de la tabla que mostrara los datos solicitados

data = [
    ['Intervalo', 'Tiempo Simulado[s]', 'clientes ingresados', 'clientes despachados',
        'promedio de productos', 'colas promedio', 'maxima cola'],

    ['1', str(TiempoSimulado[0]), str(ClientesIngresados[0]), str(ClientesDespachados[0]), str(
        ProductosDespachados[0]//ClientesDespachados[0]), str(ColasPromedio[0]), str(MaximaCola[0])],
    ['2', str(TiempoSimulado[1]), str(ClientesIngresados[1]), str(ClientesDespachados[1]), str(
        ProductosDespachados[1]//ClientesDespachados[1]), str(ColasPromedio[1]), str(MaximaCola[1])],
    ['3', str(TiempoSimulado[2]), str(ClientesIngresados[2]), str(ClientesDespachados[2]), str(
        ProductosDespachados[2]//ClientesDespachados[2]), str(ColasPromedio[2]), str(MaximaCola[2])],
    ['4', str(TiempoSimulado[3]), str(ClientesIngresados[3]), str(ClientesDespachados[3]), str(
        ProductosDespachados[3]//ClientesDespachados[3]), str(ColasPromedio[3]), str(MaximaCola[3])],
    ['5', str(TiempoSimulado[4]), str(ClientesIngresados[4]), str(ClientesDespachados[4]), str(
        ProductosDespachados[4]//ClientesDespachados[4]), str(ColasPromedio[4]), str(MaximaCola[4])],
    ['6', str(TiempoSimulado[5]), str(ClientesIngresados[5]), str(ClientesDespachados[5]), str(
        ProductosDespachados[5]//ClientesDespachados[5]), str(ColasPromedio[5]), str(MaximaCola[5])],
    ['7', str(TiempoSimulado[6]), str(ClientesIngresados[6]), str(ClientesDespachados[6]), str(
        ProductosDespachados[6]//ClientesDespachados[6]), str(ColasPromedio[6]), str(MaximaCola[6])],
    ['8', str(TiempoSimulado[7]), str(ClientesIngresados[7]), str(ClientesDespachados[7]), str(
        ProductosDespachados[7]//ClientesDespachados[7]), str(ColasPromedio[7]), str(MaximaCola[7])],
    ['9', str(TiempoSimulado[8]), str(ClientesIngresados[8]), str(ClientesDespachados[8]), str(
        ProductosDespachados[8]//ClientesDespachados[8]), str(ColasPromedio[8]), str(MaximaCola[8])],
    ['10', str(TiempoSimulado[9]), str(ClientesIngresados[9]), str(ClientesDespachados[9]), str(
        ProductosDespachados[9]//ClientesDespachados[9]), str(ColasPromedio[9]), str(MaximaCola[9])],

]

# llamado a la funcion que se encarga de generar una tabla con los datos en un PDF

GenerarPDF(data)
