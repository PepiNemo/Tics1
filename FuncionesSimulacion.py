

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
            InsertarClienteCaja(i, Cajas, ClientesSeleccionando, IndiceCajaMasVacia)


def CajaMenorCola(Cajas, Intervalo):
    # Retorna el Indice de la Caja con la Fila mas Corta de las Intervalo Actual
    return 2

def InsertarClienteCaja(IndiceClienteSelecccionando, Cajas, ClientesSeleccionando, IndiceCajaMasVacia):
    Cajas[IndiceCajaMasVacia].AgregarCliente(ClientesSeleccionando[IndiceClienteSelecccionando])
    # Si la caja no estaba atendiendo
    if(Cajas[IndiceCajaMasVacia].Temporizador == -1):
        # Que comience a atender inicializando el Temporizador
        Cajas[IndiceCajaMasVacia].AtenderSiguienteCliente()
