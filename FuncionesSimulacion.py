
def TemporizadorClientes(ClientesSeleccionando, Cajas, InterValo, ContClientesCola, MaximaCola):
    # Recorrer ClientesSeleccionando y quitarle 1 segundos a su temporizador
    # Si el temporizador llega a 0 Insertar en la caja Mas Vacia

    #Condicion para cuando ya terminaron los intervalos y aun quedan clientes 
    b=False
    if InterValo==10:
        InterValo=9
        b=True

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
            InsertarClienteCaja(i, Cajas, ClientesSeleccionando, IndiceCajaMasVacia, ContClientesCola, MaximaCola)
            
            #Obtener datos de las Colas, para los requerimientos
            ContClientesCola[0]=ContClientesCola[0]+len(Cajas[IndiceCajaMasVacia].Cola)
            ContClientesCola[1]=ContClientesCola[1]+1
            if b==False:
                if(MaximaCola[InterValo]<len(Cajas[IndiceCajaMasVacia].Cola)):
                    MaximaCola[InterValo]=len(Cajas[IndiceCajaMasVacia].Cola)
            else:
                if(MaximaCola[InterValo+1]<len(Cajas[IndiceCajaMasVacia].Cola)):
                    MaximaCola[InterValo+1]=len(Cajas[IndiceCajaMasVacia].Cola)


            
            


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
    
def InsertarClienteCaja(IndiceCliente ,Cajas, ClientesSeleccionando, IndiceCajaMasVacia,ContClientesCola,MaxCola):
    Cajas[IndiceCajaMasVacia].AgregarCliente(ClientesSeleccionando[IndiceCliente])
    # Si la caja no estaba atendiendo
    if(Cajas[IndiceCajaMasVacia].Temporizador == -1):
        # Que comience a atender inicializando el Temporizador
        Cajas[IndiceCajaMasVacia].AtenderSiguienteCliente()


def TemporizadorCajas(Cajas,Intervalo,ContClientesDesp, ContProductosDesp,ContClientesCola,MaxCola):
    Indices=[]

    for i in range(len(Cajas)):
        if(Cajas[i].Temporizador > 0):
            Cajas[i].Temporizador = Cajas[i].Temporizador-1

        elif(Cajas[i].Temporizador == 0):
            #Obtener datos de las Colas, para los requerimientos
            ContClientesCola[0]=ContClientesCola[0]+len(Cajas[i].Cola)
            ContClientesCola[1]=ContClientesCola[1]+1
            if(MaxCola[Intervalo]<len(Cajas[i].Cola)):
                MaxCola[Intervalo]=len(Cajas[i].Cola)
            
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

def GenerarTabla(TiempoSimulado, ClientesIngresados,ClientesDespachados,ProductosDespachados,ColasPromedio,MaximaCola):
    # Construccion de la tabla que mostrara los datos solicitados
    
    PromedioProductos=[]
    for i in range(11):
        if(ClientesDespachados[i]==0):
            PromedioProductos.append(0)
        else:
            PromedioProductos.append(ProductosDespachados[i]//ClientesDespachados[i])


    data = [
        ['Intervalo', 'Tiempo Simulado[s]', 'clientes ingresados', 'clientes despachados',
            'promedio de productos', 'colas promedio', 'maxima cola'],

        ['1', str(TiempoSimulado[0]), str(ClientesIngresados[0]), str(ClientesDespachados[0]), str(
            PromedioProductos[0]), str(ColasPromedio[0]), str(MaximaCola[0])],
        ['2', str(TiempoSimulado[1]), str(ClientesIngresados[1]), str(ClientesDespachados[1]), str(
            PromedioProductos[1]), str(ColasPromedio[1]), str(MaximaCola[1])],
        ['3', str(TiempoSimulado[2]), str(ClientesIngresados[2]), str(ClientesDespachados[2]), str(
            PromedioProductos[2]), str(ColasPromedio[2]), str(MaximaCola[2])],
        ['4', str(TiempoSimulado[3]), str(ClientesIngresados[3]), str(ClientesDespachados[3]), str(
            PromedioProductos[3]), str(ColasPromedio[3]), str(MaximaCola[3])],
        ['5', str(TiempoSimulado[4]), str(ClientesIngresados[4]), str(ClientesDespachados[4]), str(
            PromedioProductos[4]), str(ColasPromedio[4]), str(MaximaCola[4])],
        ['6', str(TiempoSimulado[5]), str(ClientesIngresados[5]), str(ClientesDespachados[5]), str(
            PromedioProductos[5]), str(ColasPromedio[5]), str(MaximaCola[5])],
        ['7', str(TiempoSimulado[6]), str(ClientesIngresados[6]), str(ClientesDespachados[6]), str(
            PromedioProductos[6]), str(ColasPromedio[6]), str(MaximaCola[6])],
        ['8', str(TiempoSimulado[7]), str(ClientesIngresados[7]), str(ClientesDespachados[7]), str(
            PromedioProductos[7]), str(ColasPromedio[7]), str(MaximaCola[7])],
        ['9', str(TiempoSimulado[8]), str(ClientesIngresados[8]), str(ClientesDespachados[8]), str(
            PromedioProductos[8]), str(ColasPromedio[8]), str(MaximaCola[8])],
        ['10', str(TiempoSimulado[9]), str(ClientesIngresados[9]), str(ClientesDespachados[9]), str(
            PromedioProductos[9]), str(ColasPromedio[9]), str(MaximaCola[9])],
        ['Extra', str(TiempoSimulado[10]), str(ClientesIngresados[10]), str(ClientesDespachados[10]), str(
            PromedioProductos[10]), str(ColasPromedio[10]), str(MaximaCola[10])],

    ]

    # llamado a la funcion que se encarga de generar una tabla con los datos en un PDF

    GenerarPDF(data)

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

    from reportlab.lib.styles import getSampleStyleSheet
    sample_style_sheet = getSampleStyleSheet()
    from reportlab.platypus import Paragraph
    paragraph_0 = Paragraph('', sample_style_sheet['Heading1'])
    paragraph_1 = Paragraph('Resultados Simulación', sample_style_sheet['Heading1'])
    paragraph_2 = Paragraph(
        "Some normal body text",
        sample_style_sheet['BodyText']
    )
    elems.append(paragraph_0)
    elems.append(paragraph_0)
    elems.append(paragraph_0)
    elems.append(paragraph_1)
    elems.append(paragraph_2)

    pdf.build(elems)


