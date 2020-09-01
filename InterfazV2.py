import tkinter as tk
from tkinter import *


def Simulacion(Desc, Horas, Periodos, Clientes, Minprod, Maxprod, Tsel, Tmar, Tpago, Distrib, CAJAS):
    pass


class Simulador():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        '''----------Descripcion----------'''
        self.lblDesc = Label(text="Descripcion")
        self.lblDesc.place(x=20, y=10)
        self.desc = Entry()
        self.desc.insert(0, "Ingresa descipcion")  # if error wea.insert(valor agregado antes)
        self.desc.focus()
        self.desc.place(x=130, y=10, width=130)

        '''----------Horas de atencion----------'''
        self.lblHoras = Label(text="Horas de Atencion")
        self.lblHoras.place(x=20, y=40)
        self.horas = Entry(width=60)
        self.horas.place(x=130, y=40, width=130)

        '''----------Periodos de Tiempo----------'''
        self.lblPeriodos = Label(text="Periodos de tiempo")
        self.lblPeriodos.place(x=20, y=70)
        self.periodos = Entry(width=60)
        self.periodos.place(x=130, y=70, width=130)

        '''----------CLientes Esperados----------'''
        self.lblClientes = Label(text="Clientes Esperados")
        self.lblClientes.place(x=20, y=100)
        self.clientes = Entry(width=60)
        self.clientes.place(x=130, y=100, width=130)

        '''----------Distribucion----------'''
        self.lblDistribucion = Label(text="Distribucion")
        self.lblDistribucion.place(x=20, y=130)
        self.distribucion = Entry(width=60)
        self.distribucion.place(x=130, y=130, width=130)

        '''----------Cajas Abiertas----------'''
        self.lblCajas = Label(text="Cajas Abiertas")
        self.lblCajas.place(x=20, y=160)
        self.cajas = Entry(width=60)
        self.cajas.place(x=130, y=160, width=130)

        '''----------Cantidad Minima de Productos----------'''
        self.lblCMinProductos = Label(text="Productos minimos")
        self.lblCMinProductos.place(x=20, y=190)
        self.minprod = Entry(width=60)
        self.minprod.place(x=130, y=190, width=130)

        '''----------Cantidad Maxima de Productos----------'''
        self.lblCMaxProductos = Label(text="Productos Maximo")
        self.lblCMaxProductos.place(x=20, y=220)
        self.maxprod = Entry(width=60)
        self.maxprod.place(x=130, y=220, width=130)

        '''----------Tiempo Seleccion----------'''
        self.lblTS = Label(text="Tiempo seleccion")
        self.lblTS.place(x=20, y=250)
        self.TS = Entry(width=60)
        self.TS.place(x=130, y=250, width=130)

        '''----------Tiempo Marcadp----------'''
        self.lblTM = Label(text="Tiempo Marcado")
        self.lblTM.place(x=20, y=280)
        self.TM = Entry(width=60)
        self.TM.place(x=130, y=280, width=130)

        '''----------Tiempo Pago----------'''
        self.lblTP = Label(text="Tiempo Pago")
        self.lblTP.place(x=10, y=310, width=100)
        self.TP = Entry(width=60)
        self.TP.place(x=130, y=310, width=130)

        self.button = tk.Button(self.frame, text="Simular", command=self.simulate)
        self.button.pack()
        # arreglar boton que no aparece
        self.frame.place(x=130, y=340)

        '''-----------METODOS-----------'''

    def simulate(self):
        global Horas, Periodos, Clientes, Minprod, Maxprod, Tsel, Tmar, Distrib, Tpago, CAJAS
        BoolDesc = False
        BoolHoras = False
        BoolPeriodos = False
        BoolClientes = False
        BoolMinProd = False
        BoolMaxProd = False
        BoolTsel = False
        BoolTmar = False
        BoolTpago = False
        BoolDist = False
        BoolCajas = False

        try:  # Se puede hacer sin exceptions
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

        try:
            Periodos = int(self.periodos.get())
            BoolPeriodos = True
        except:
            print("Valor ingresado en periodos no entero")
            BoolPeriodos = False
        try:
            Clientes = int(self.clientes.get())
            BoolClientes = True
        except:
            print("Valor ingresado en cantidad de clientes no entero")
            BoolClientes = False

        try:
            Minprod = int(self.minprod.get())
            BoolMinProd = True
        except:
            print("Valor ingresado en minimo productos no entero")
            BoolMinProd = False

        try:
            Maxprod = int(self.maxprod.get())
            BoolMaxProd = True
        except:
            print("Valor ingresado en maximo Productos no entero")
            BoolMaxProd = False

        try:
            Tsel = int(self.TS.get())
            BoolTsel = True
        except:
            print("Valor ingresado en tiempo de seleccion no entero")
            BoolTsel = False

        try:
            Tmar = int(self.TM.get())
            BoolTmar = True
        except:
            print("Valor ingresado en tiempo de marcado no entero")
            BoolTmar = False

        try:
            Tpago = int(self.TP.get())
            BoolTpago = True
        except:
            print("Valor ingresado en tiempo de pago no entero")
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

        if BoolDesc and BoolHoras and BoolPeriodos and BoolClientes and BoolMinProd and BoolMaxProd and BoolTsel and BoolTmar and BoolTpago and BoolDist and BoolCajas:
            Simulacion(Desc, Horas, Periodos, Clientes, Minprod, Maxprod, Tsel, Tmar, Tpago, Distrib, CAJAS)
            print("Simulando")

            LabelSim = Label(text="Desea realizar una nueva simulacion?")
            LabelSim.place(x=10, y=370)
            YesBtn = tk.Button(text="Si")
            NoBtn = tk.Button(text="No", command=self.master.destroy)
            YesBtn.place(x=10, y=390, width=30)  # Hacer Funcion Yes
            NoBtn.place(x=40, y=390, width=30)
        else:
            errores(BoolDesc, BoolHoras, BoolPeriodos, BoolClientes, BoolMinProd, BoolMaxProd, BoolTsel, BoolTmar,
                    BoolTpago, BoolDist, BoolCajas)




def errores(BoolDesc, BoolHoras, BoolPeriodos, BoolClientes, BoolMinProd, BoolMaxProd, BoolTsel, BoolTmar, BoolTpago,
            BoolDist, BoolCajas):
    error = Tk()
    error.title("Errores Encontrados")
    error.geometry('300x300')
    LblD = Label(text="")
    LblD.place(x=20, y=10)

    if not BoolDesc:
        LblD = Label(text="Error Ingresando la descripcion")
    if not BoolHoras:
        LblH = Label(text="Error Ingresando la cantidad de horas")
        LblH.pack()
    if not BoolPeriodos:
        LblP = Label(text="Error Ingresando la cantidad de horas")
        LblP.pack()
    if not BoolClientes:
        LblCL = Label(text="Error Ingresando la cantidad de horas")
        LblCL.pack()
    if not BoolMinProd:
        LblMin = Label(text="Error Ingresando la cantidad de horas")
        LblMin.pack()
    if not BoolMaxProd:
        LblMax = Label(text="Error Ingresando la cantidad de horas")
        LblMax.pack()
    if not BoolTsel:
        LblTsel = Label(text="Error Ingresando la cantidad de horas")
        LblTsel.pack()
    if not BoolTmar:
        LblTmar = Label(text="Error Ingresando la cantidad de horas")
        LblTmar.pack()
    if not BoolTpago:
        LblTpago = Label(text="Error Ingresando la cantidad de horas")
        LblTpago.pack()
    if not BoolDist:
        LblDist = Label(text="Error Ingresando la cantidad de horas")
        LblDist.pack()
    if not BoolCajas:
        LblCajas = Label(text="Error Ingresando la cantidad de horas")
        LblCajas.pack()

    error.mainloop()


def main():
    root = Tk()
    root.title = "Simulador"
    root.geometry('500x375')
    app = Simulador(root)
    root.mainloop()


if __name__ == '__main__':
    main()
