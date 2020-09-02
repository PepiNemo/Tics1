
def TemporizadorClientes(ClientesSeleccionando, Cajas, InterValo,ContClientesCola,MaxCola):
    # Recorrer ClientesSeleccionando y quitarle 1 segundos a su temporizador
    # Si el temporizador llega a 0 Insertar en la caja Mas Vacia
    contador=[]
    for i in range(len(ClientesSeleccionando)):
        if(ClientesSeleccionando[i].Temporizador > 0):
            # Restamos los temporizadores
            ClientesSeleccionando[i].Temporizador = ClientesSeleccionando[i].Temporizador-1

        elif(ClientesSeleccionando[i].Temporizador == 0):
            #Guardamos el indice, para dps eliminarlo                                               
            contador.append(i)
            #Mandamos al Cliente a la Caja con Menor Cola
            IndiceCajaMasVacia = CajaMenorCola(Cajas, InterValo)
            InsertarClienteCaja(i, Cajas, ClientesSeleccionando, IndiceCajaMasVacia)
            #Obtener datos de las Colas, para los requerimientos
            ContClientesCola[0]=ContClientesCola[0]+len(Cajas[IndiceCajaMasVacia].Cola)
            ContClientesCola[1]=ContClientesCola[1]+1
            if(MaxCola[InterValo]<len(Cajas[IndiceCajaMasVacia].Cola)):
                MaxCola[InterValo]=len(Cajas[IndiceCajaMasVacia].Cola)

    #Este for es para eliminar los clientes ingresados sin tener problemas con los index fuera de rango
    for j in range(len(contador)):
        del ClientesSeleccionando[contador[j]-j]

def CajaMenorCola(Cajas, Intervalo):
    #Retorna el indice da la Caja con menor cola y que pertenezca al intervalo actual
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
    
def InsertarClienteCaja(IndiceCliente ,Cajas, ClientesSeleccionando, IndiceCajaMasVacia):
    Cajas[IndiceCajaMasVacia].AgregarCliente(ClientesSeleccionando[IndiceCliente])
    # Si la caja no estaba atendiendo
    if(Cajas[IndiceCajaMasVacia].Temporizador == -1):
        # Que comience a atender inicializando el Temporizador
        Cajas[IndiceCajaMasVacia].AtenderSiguienteCliente()

def TemporizadorCajas(Cajas,Intervalo,ContClientesDesp, ContProductosDesp):
    Indices=[]
    for i in range(len(Cajas)):
        if(Cajas[i].Temporizador > 0):
            Cajas[i].Temporizador = Cajas[i].Temporizador-1

        elif(Cajas[i].Temporizador == 0):
            #Si el temporizador llego a 0, el cliente ya fue atendido y queda despachar
            Cajas[i].DespacharCliente()
            # Si no tiene mas Clientes en cola Deja de Atender
            if ( len(Cajas[i].Cola)==0 ):
                if(Cajas[i].Intervalo!=Intervalo):
                    #Lo guardamos para dps eliminarlo, para cerrar la caja 
                    Indices.append(i)
                #La caja queda en espera
                Cajas[i].Temporizador = -1

            else:
                # Si la caja tiene mas clientes en cola, que Atienda al Siguiente
                Cajas[i].AtenderSiguienteCliente()
    
    #Este for es para eliminar los clientes ingresados sin tener problemas con los index fuera de rango
    for j in range(len(Indices)):
        #Obtenemos los datos de la caja antes de cerrarla
        ContClientesDesp[Intervalo]=ContClientesDesp[Intervalo]+Cajas[Indices[j]-j].ClientesDespachados
        ContProductosDesp[Intervalo]=ContProductosDesp[Intervalo]+Cajas[Indices[j]-j].ProductosDespachados
        del Cajas[Indices[j]-j]
                  
def ObtenerDatosCajas(Cajas,Intervalo, ContClientesDesp, ContProductosDesp):
    Indices=[]
    for i in range(len(Cajas)):
        #Obtenemos los datos del intervalo
        ContClientesDesp[Intervalo]=ContClientesDesp[Intervalo]+Cajas[i].ClientesDespachados
        ContProductosDesp[Intervalo]=ContProductosDesp[Intervalo]+Cajas[i].ProductosDespachados
        #Si la caja ya atendio a sus clientes, cerrar 
        if(Cajas[i].Temporizador==-1):
            Indices.append(i)
        else:
            #Seteamos los cajas en 0 para que inicie un nuevo intervalo
            Cajas[i].ClientesDespachados=0
            Cajas[i].ProductosDespachados=0

    #Este for es para eliminar los clientes ingresados sin tener problemas con los index fuera de rango
    for j in range(len(Indices)):
        del Cajas[Indices[j]-j]

def GenerarPDF(data):
    fileName = 'pdfTable.pdf'

    from reportlab.platypus import SimpleDocTemplate
    from reportlab.lib.pagesizes import letter

    pdf = SimpleDocTemplate(
            fileName,
        pagesize=letter
    )

    from reportlab.platypus import Table
    table = Table(data)

    # add style
    from reportlab.platypus import TableStyle
    from reportlab.lib import colors

    style = TableStyle([
        ('BACKGROUND', (0,0), (7,0), colors.yellow),
        ('TEXTCOLOR',(0,0),(-1,0),colors.black),
            

        ('ALIGN',(0,0),(-1,-1),'CENTER'),

        ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 7),

        ('BOTTOMPADDING', (0,0), (-1,0), 7),

        ('BACKGROUND',(0,1),(-1,-1),colors.beige),
    ])
    table.setStyle(style)




    # 3) Add borders
    ts = TableStyle(
        [
        ('BOX',(0,0),(-1,-1),2,colors.black),

        ('LINEBEFORE',(2,1),(2,-1),2,colors.red),
        ('LINEABOVE',(0,2),(-1,2),2,colors.green),

        ('GRID',(0,1),(-1,-1),2,colors.black),
        ]
    )
    table.setStyle(ts)

    elems = []
    elems.append(table)

    pdf.build(elems)


