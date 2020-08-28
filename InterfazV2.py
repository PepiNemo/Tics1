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
        self.lblDistribucion = Label(text="Distribucion cajas por periodo")
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
        Horas = int(self.horas.get())
        Periodos = int(self.periodos.get())
        Clientes = int(self.clientes.get())
        Minprod = int(self.minprod.get())
        Maxprod = int(self.maxprod.get())
        Tsel = int(self.TS.get())
        Tmar = int(self.TM.get())
        Tpago = int(self.TP.get())

        dis = self.distribucion.get()
        disArr = dis.split(",")
        Distrib = []
        for i in disArr:
            Distrib.append(int(i))

        caj = self.cajas.get()
        cajArr = caj.split(",")
        CAJAS = []
        for i in cajArr:
            CAJAS.append(int(i))

        self.master.destroy()
        print("simulando")

        '''-----Chequeo Errores'''

    def descCheck(self, Desc):
        if Desc.len > 60:
            return False
        return True

    def horasCheck(self, Horas):
        if isinstance(Horas, int) and Horas > 0:
            return True
        return False

    def PeriodosCheck(self, Periodos):
        if isinstance(Periodos, int) and Periodos > 9:
            return True
        return False

    def ClientesCheck(self, Clientes):
        if isinstance(Clientes, int) and Clientes > 0:
            return True
        return False

    def DistribucionCheck(self, Distrib, Periodos):
        for i in Distrib:
            if isinstance(i, int) is False:
                return False
        if Distrib.len != Periodos:
            return False
        return True

    def CajasCheck(self, CAJAS, Periodos):
        for i in CAJAS:
            if isinstance(i,int) is False:
                return False
        if CAJAS.len != Periodos:
            return False
        return True
    def ProductosMinCheck(self,MinProd):
        if(isinstance(MinProd,int) is False):
            return False
        if MinProd<0:
            return False
        return True
    def ProductosMacCheck(self,MaxProd,MinProd):
        if isinstance(MaxProd,int) is False:
            return  False
        if MaxProd<MinProd:
            return False
        return True
    def TiempoSelecCheck(self,Tsel):
        if isinstance(Tsel,int) and Tsel>0:
            return True
        return False

    def TiempoMarCheck(self, Tmar):
        if isinstance(Tmar, int) and Tmar > 0:
            return True
        return False

    def TiempopagoCheck(self, Tpago):
         if isinstance(Tpago, int) and Tpago > 0:
            return True
         return False




def main():
    root = Tk()
    root.title = "Simulador"
    root.geometry('470x500')
    app = Simulador(root)
    root.mainloop()


if __name__ == '__main__':
    main()
