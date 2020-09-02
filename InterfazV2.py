import tkinter as tk
from tkinter import *
#lista, creo
def retornar():
    nombre = "Ingrese Nombre"
    desc = "Ingrese una descripcion"
    horas = "0"
    clientes = "0"
    distr = "0"
    cajas = "0"
    min = "0"
    max = "0"
    ts = "0"
    tm = "0"
    tp = "0"

    root = Tk()
    root.title = "Simulador"
    root.geometry('300x385')
    app = Simulador(root,nombre,desc,horas,clientes,distr,cajas,min,max,ts,tm,tp)
    root.mainloop()
    print(app.Horas)
    lista = [Desc, Horas, Periodos, Clientes, Minprod, Maxprod, Tsel, Tmar, Tpago, Distrib, CAJAS]
    return lista

class Simulador:
    def __init__(self, master,Nombre, Desc,Horas,Clientes,Distribucion,Cajas,Minprod,Maxprod,ts,tm,tp):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.Nombre = Nombre
        self.Desc = Desc
        self.Horas = Horas
        self.Clientes = Clientes
        self.Distrib = Distribucion
        self.Cajas = Cajas
        self.Min = Minprod
        self.Max = Maxprod
        self.ts = ts
        self.tm = tm
        self.tp = tp
        '''----------Nombre----------'''
        self.lblNombre = Label(text="Nombre")
        self.lblNombre.place(x=20,y=10)
        self.nombre = Entry()
        self.nombre.insert(0,self.Nombre)
        self.nombre.place(x=130,y = 10)
        self.nombre.focus()
        '''----------Descripcion----------'''
        self.lblDesc = Label(text="Descripcion")
        self.lblDesc.place(x=20, y=40)
        self.desc = Entry()
        self.desc.insert(0,self.Desc)  # if error wea.insert(valor agregado antes)
        self.desc.place(x=130, y=40, width=130)

        '''----------Horas de atencion----------'''
        self.lblHoras = Label(text="Horas de Atencion") #rango de horas ej 08:00-18:00
        self.lblHoras.place(x=20, y=70)
        self.horas = Entry(width=60)
        self.horas.insert(0,self.Horas)
        self.horas.place(x=130, y=70, width=130)

        '''----------CLientes Esperados----------'''
        self.lblClientes = Label(text="Clientes Esperados")
        self.lblClientes.place(x=20, y=100)
        self.clientes = Entry(width=60)
        self.clientes.insert(0,self.Clientes)
        self.clientes.place(x=130, y=100, width=130)

        '''----------Distribucion----------'''
        self.lblDistribucion = Label(text="Distribucion")
        self.lblDistribucion.place(x=20, y=130)
        self.distribucion = Entry(width=60)
        self.distribucion.insert(0,self.Distrib)
        self.distribucion.place(x=130, y=130, width=130)

        '''----------Cajas Abiertas----------'''
        self.lblCajas = Label(text="Cajas Abiertas")
        self.lblCajas.place(x=20, y=160)
        self.cajas = Entry(width=60)
        self.cajas.insert(0,self.Cajas)
        self.cajas.place(x=130, y=160, width=130)

        '''----------Cantidad Minima de Productos----------'''
        self.lblCMinProductos = Label(text="Productos minimos")
        self.lblCMinProductos.place(x=20, y=190)
        self.minprod = Entry(width=60)
        self.minprod.insert(0,self.Min)
        self.minprod.place(x=130, y=190, width=130)

        '''----------Cantidad Maxima de Productos----------'''
        self.lblCMaxProductos = Label(text="Productos Maximo")
        self.lblCMaxProductos.place(x=20, y=220)
        self.maxprod = Entry(width=60)
        self.maxprod.insert(0,self.Max)
        self.maxprod.place(x=130, y=220, width=130)

        '''----------Tiempo Seleccion----------'''
        self.lblTS = Label(text="Tiempo seleccion")
        self.lblTS.place(x=20, y=250)
        self.TS = Entry(width=60)
        self.TS.insert(0,self.ts)
        self.TS.place(x=130, y=250, width=130)

        '''----------Tiempo Marcadp----------'''
        self.lblTM = Label(text="Tiempo Marcado")
        self.lblTM.place(x=20, y=280)
        self.TM = Entry(width=60)
        self.TM.insert(0,self.tm)
        self.TM.place(x=130, y=280, width=130)

        '''----------Tiempo Pago----------'''
        self.lblTP = Label(text="Tiempo Pago")
        self.lblTP.place(x=10, y=310, width=100)
        self.TP = Entry(width=60)
        self.TP.insert(0,self.tp)
        self.TP.place(x=130, y=310, width=130)

        self.button = tk.Button(self.frame, text="Simular", command=self.simulate)
        self.button.pack()
        self.frame.place(x=130, y=340)

        '''-----------METODOS-----------'''
    def simulate(self):
        global Desc, Horas, Clientes, Minprod, Maxprod, Tsel, Tmar, Distrib, Tpago, CAJAS
        BoolDesc = False
        BoolHoras = False
        BoolClientes = False
        BoolMinProd = False
        BoolMaxProd = False
        BoolTsel = False
        BoolTmar = False
        BoolTpago = False
        BoolDist = False
        BoolCajas = False

        #finally if num <0 false y try nombre sin espacios
        try:
            Name = self.nombre.get()
            name = Name[0]
            BoolName = True
        finally:
            Name = self.nombre.get()
            name = Name[0]
            if len(name) <=0:
                BoolName = False

        try:
            Desc = self.desc.get()
            BoolDesc = True
        finally:
            Desc = self.desc.get()
            if len(Desc) <= 0 or len(Desc) > 60:
                BoolDesc = False
                print("Error en la descripcion")

        try:
            Horas = int(self.horas.get())
            BoolHoras = True
        except:
            print("Valor ingresado en horas de atencion no entero")
            BoolHoras = False
        finally:
            if Horas <=0:
                BoolHoras = False

        try:
            Clientes = int(self.clientes.get())
            BoolClientes = True
        except:
            print("Valor ingresado en cantidad de clientes no entero")
            BoolClientes = False
        finally:
            if Clientes<0:
                BoolClientes = False

        try:
            Minprod = int(self.minprod.get())
            BoolMinProd = True
        except:
            print("Valor ingresado en minimo productos no entero")
            BoolMinProd = False
        finally:
            if Minprod < 0:
                BoolMinProd = False

        try:
            Maxprod = int(self.maxprod.get())
            BoolMaxProd = True
        except:
            print("Valor ingresado en maximo Productos no entero")
            BoolMaxProd = False
        finally:
            if Maxprod < Minprod:
                BoolMaxProd = False

        try:
            Tsel = int(self.TS.get())
            BoolTsel = True
        except:
            print("Valor ingresado en tiempo de seleccion no entero")
            BoolTsel = False
        finally:
            if Tsel <0:
                BoolTsel = False

        try:
            Tmar = int(self.TM.get())
            BoolTmar = True
        except:
            print("Valor ingresado en tiempo de marcado no entero")
            BoolTmar = False
        finally:
            if Tmar <0:
                BoolTmar = False

        try:
            Tpago = int(self.TP.get())
            BoolTpago = True
        except:
            print("Valor ingresado en tiempo de pago no entero")
            BoolTpago = False
        finally:
            if Tpago <0:
                BoolTpago = False

        try:
            dis = self.distribucion.get()
            disArr = dis.split(",")
            Distrib = []
            for i in disArr:
                j = int(i)
                Distrib.append(j)
        except:
            print("Error ingresando datos en distribuicon porcentual")
            BoolDist = False
        finally:
            suma = 0
            for i in Distrib:
                suma += i
            if suma == 100:
                BoolDist = True
            else:
                BoolDist = False
                print("Distribucion no suma 100")
            if len(Distrib)!= 10:
                BoolDist = False
        try:
            caj = self.cajas.get()
            cajArr = caj.split(",")
            CAJAS = []
            for i in cajArr:
                j = int(i)
                CAJAS.append(j)
            BoolCajas = True
        except:
            print("Error ingresando datos en cantidad de cajas")
            BoolCajas = False
        finally:
            for i in CAJAS:
                if i <= 0:
                    BoolCajas = False
            if len(CAJAS) != 10:
                BoolCajas = False

        if BoolName and BoolDesc and BoolHoras and BoolClientes and BoolMinProd and BoolMaxProd and BoolTsel and BoolTmar and BoolTpago and BoolDist and BoolCajas:
            #Simulacion(Desc, Horas, Periodos, Clientes, Minprod, Maxprod, Tsel, Tmar, Tpago, Distrib, CAJAS)
            print("Simulando")
            self.master.geometry('280x430')
            LabelSim = Label(text="Simulacion en proceso.")
            LabelSim.place(x=10, y=370)
            NoBtn = tk.Button(text="Salir", command=self.No)
            NoBtn.place(x=70, y=390, width=50)
        else:
            WarningLbl = Label(text = "Varios Errores")
            WarningLbl.place(x=10, y = 370)
            self.master.geometry('600x395')
            lblN = tk.Label()
            lblD = tk.Label()
            lblH = tk.Label()
            lblC = tk.Label()
            lblDist = tk.Label()
            lblCajas = tk.Label()
            lblMin = tk.Label()
            lblMax = tk.Label()
            lblTsel = tk.Label()
            lblTmar = tk.Label()
            lblTpago= tk.Label()

            if not BoolName:
                lblN['text'] = "Error Ingresando nombre"
            lblN.place(x=285, y=10)
            if not BoolDesc:
                lblD['text'] = 'Error en la Descripcion ingresada.'
            lblD.place(x=285, y=40)
            if not BoolHoras:
                lblH['text']="Error en las horas ingresadas, debe ser mayor que 0."
            lblH.place(x=285,y=70)
            if not BoolClientes:
                lblC['text']="Error en la cantidad de clientes, debe ser mayor que 0."
            lblC.place(x=285,y=100)
            if not BoolDist:
                lblDist['text']== "Error en la distribicion de cajas, deben ser 10 valores y sumar 100"
                self.master.geometry('650x375')
            lblDist.place(x=285,y=130)
            if not BoolCajas:
                lblCajas['text']="Error en la cantidad de cajas, deben ser 10 valores"
            lblCajas.place(x=285,y=160)
            if not BoolMinProd:
                lblMin['text']="Error en cantidad minima de productos, debe ser mayor o igual a 0."
            lblMin.place(x=285, y=190)
            if not BoolMaxProd:
                lblMax['text']="Error en cantidad maxima de productos, debe ser mayor que "+str(Minprod)+"."
            lblMax.place(x=285,y=220)
            if not BoolTsel:
                lblTsel['text']="Error en tiempo promedio seleccion de productos, debe ser mayor que 0."
            lblTsel.place(x=285,y=250)
            if not BoolTmar:
                lblTmar['text']="Error en tiempo promedio de marcado, debe ser mayor que 0."
            lblTmar.place(x=285,y=280)
            if not BoolTpago:
                lblTpago['text']="Error en tiempo promedio de pago, debe ser mayor que 0."
            lblTpago.place(x=285,y=310)

    def No(self):
        self.master.destroy()
def main():
    retornar()

if __name__ == '__main__':
    main()
