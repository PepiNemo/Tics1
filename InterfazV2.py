import tkinter as tk
from tkinter import *


class Simulador():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        '''----------Descripcion----------'''
        self.lblDesc = Label(text="Descripcion")
        self.lblDesc.pack()
        self.desc = Entry(width=60)
        self.desc.focus()
        self.desc.pack()

        '''----------Horas de atencion----------'''
        self.lblHoras = Label(text="Horas de Atencion")
        self.lblHoras.pack()
        self.horas = Entry(width=60)
        self.horas.pack()

        '''----------Periodos de Tiempo----------'''
        self.lblPeriodos = Label(text="Periodos de tiempo")
        self.lblPeriodos.pack()
        self.periodos = Entry(width=60)
        self.periodos.pack()

        '''----------CLientes Esperados----------'''
        self.lblClientes = Label(text="Clientes Esperados")
        self.lblClientes.pack()
        self.clientes = Entry(width=60)
        self.clientes.pack()

        '''----------Distribucion----------'''
        self.lblDistribucion = Label(text="Distribucion clietnes por periodo")
        self.lblDistribucion.pack()
        self.distribucion = Entry(width=60)
        self.distribucion.pack()

        '''----------Cajas Abiertas----------'''
        self.lblCajas = Label(text="Cajas Abiertas por Periodo")
        self.lblCajas.pack()
        self.cajas = Entry(width=60)
        self.cajas.pack()

        '''----------Cantidad Minima de Productos----------'''
        self.lblCMinProductos = Label(text="Cantidad Minima de Productos")
        self.lblCMinProductos.pack()
        self.minprod = Entry(width=60)
        self.minprod.pack()

        '''----------Cantidad Maxima de Productos----------'''
        self.lblCMaxProductos = Label(text="Cantidad Maxima de Productos")
        self.lblCMaxProductos.pack()
        self.maxprod = Entry(width=60)
        self.maxprod.pack()

        '''----------Tiempo Seleccion----------'''
        self.lblTS = Label(text="Tiempo seleccion productos")
        self.lblTS.pack()
        self.TS = Entry(width=60)
        self.TS.pack()

        '''----------Tiempo Marcadp----------'''
        self.lblTM = Label(text="Tiempo Marcado")
        self.lblTM.pack()
        self.TM = Entry(width=60)
        self.TM.pack()

        '''----------Tiempo Pago----------'''
        self.lblTP = Label(text="Tiempo Pago")
        self.lblTP.pack()
        self.TP = Entry(width=60)
        self.TP.pack()

        self.button = tk.Button(self.frame, text="Simular", command=self.simulate)
        self.button.pack()
        self.frame.pack()

        '''-----------METODOS-----------'''

    def simulate(self):
        Desc = self.desc.get()
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
            suma = 0
            for i in disArr:
                j = int(i)
                Distrib.append(j)
                suma += j
            if suma == 100:
                BoolDist = True
            else:
                BoolDist = True
        except:
            print("Error ingresando datos en distribuicon porcentual")
            BoolDist = False
        #finally todos valores mayores que 0 y suma  = 100
        try: #excepcion todos los valores mayores que 0
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
        #finally todos os valores mayores que 0


        #if todas las condiciones True:
            #simulador(Datos)
        #else:
            #Abrir segunda pantalla indicando los datos mal ingresados
            #Intentar setear por default los datos ingresados la anteriormente
        self.master.destroy()
        print("simulando")



def main():
    root = Tk()
    root.title = "Simulador"
    root.geometry('470x500')
    app = Simulador(root)
    root.mainloop()


if __name__ == '__main__':
    main()
