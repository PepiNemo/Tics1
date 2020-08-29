

def TemporizadorCajas(Cajas,Intervalo,ContClientesDesp, ContProductosDesp):
    for i in range(len(Cajas)):

        if(Cajas[i].Temporizador > 0):
            Cajas[i].Temporizador = Cajas[i].Temporizador-1

        elif(Cajas[i].Temporizador == 0):
            #Si el temporizador llego a 0, el cliente ya fue atendido y queda despachar
            Cajas[i].DespacharCliente()
            # Si la caja tiene mas clientes en cola, que Atienda al Siguiente
            Cajas[i].AtenderSiguienteCliente()

            # Si no tiene mas Clientes en cola Deja de Atender
            if ( len(Cajas[i].Cola)==0 ):
                #Si la caja que estaba atendiendo, no es del intervalo actual, y ya no tiene mas Cliente, la Caja se elimina
                if(Cajas[i].Intervalo!=Intervalo):
                    #Obtenemos los datos antes de cerrar la caja
                    ContClientesDesp[0]=ContClientesDesp[0]+Cajas[i].ClientesDespachados
                    ContProductosDesp[0]=ContProductosDesp[0]+Cajas[i].ProductosDespachados
                    #Eliminamos la Caja
                    Cajas.remove(i)
                else :
                    #Si la Caja si es del intervalo, solo deja de antender, hasta tener Clientes
                    Cajas[i].Temporizador = -1
            
def ObtenerDatosCajas(Cajas,ContClientesDesp, ContProductosDesp):
    for i in range(len(Cajas)):
        #Obtenemos los datos antes de cerrar la caja
        ContClientesDesp[0]=ContClientesDesp[0]+Cajas[i].ClientesDespachados
        ContProductosDesp[0]=ContProductosDesp[0]+Cajas[i].ProductosDespachados

def TemporizadorClientes(ClientesSeleccionando, Cajas, InterValo,ContClientesCola,MaxCola):
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
            InsertarClienteCaja(i, Cajas, ClientesSeleccionando, IndiceCajaMasVacia)
            #Obtener datos de las Colas, para los requerimientos
            ContClientesCola[0]=ContClientesCola[0]+IndiceCajaMasVacia
            ContClientesCola[1]=ContClientesCola[1]+1
            if(MaxCola[0]<IndiceCajaMasVacia):
                MaxCola[0]=IndiceCajaMasVacia


def CajaMenorCola(Cajas, Intervalo):
        Min = 0
        b = 0
        Indice = 0
        for a in range(len(Cajas)):
            if (Cajas[a].Intervalo == Intervalo):
                b += 1
                if (b == 1): # Caso para guardar el largo de la primera caja del intervalo actual
                    Min = len(Cajas[a].Cola)
                    Indice = a
                else:
                    if (len(Cajas[a].Cola) < Min):
                        Min = len(Cajas[a].Cola)
                        Indice = a
        return Indice
    

def InsertarClienteCaja(IndiceClienteSelecccionando, Cajas, ClientesSeleccionando, IndiceCajaMasVacia):
    Cajas[IndiceCajaMasVacia].AgregarCliente(ClientesSeleccionando[IndiceClienteSelecccionando])
    # Si la caja no estaba atendiendo
    if(Cajas[IndiceCajaMasVacia].Temporizador == -1):
        # Que comience a atender inicializando el Temporizador
        Cajas[IndiceCajaMasVacia].AtenderSiguienteCliente()
