import tkinter as tk
from tkinter import *

#Arreglar Boton
class Simulador():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        '''----------Descripcion----------'''
        self.lblDesc = Label(text="Descripcion")
        self.lblDesc.place(x=20, y = 10)
        self.desc = Entry()
        self.desc.insert(0,"Ingresa descipcion") #if error wea.insert(valor agregado antes)
        self.desc.focus()
        self.desc.place(x=130, y=10, width = 100)

        '''----------Horas de atencion----------'''
        self.lblHoras = Label(text="Horas de Atencion")
        self.lblHoras.place(x=20, y = 40)
        self.horas = Entry(width=60)
        self.horas.place(x=130, y = 40, width = 100)

        '''----------Periodos de Tiempo----------'''
        self.lblPeriodos = Label(text="Periodos de tiempo")
        self.lblPeriodos.place(x=20, y = 70)
        self.periodos = Entry(width=60)
        self.periodos.place(x = 130, y = 70, width = 100)

        '''----------CLientes Esperados----------'''
        self.lblClientes = Label(text="Clientes Esperados")
        self.lblClientes.place(x=20, y = 100)
        self.clientes = Entry(width=60)
        self.clientes.place(x = 130, y = 100, width = 100)

        '''----------Distribucion----------'''
        self.lblDistribucion = Label(text="Distribucion")
        self.lblDistribucion.place(x=20, y = 130)
        self.distribucion = Entry(width=60)
        self.distribucion.place(x=130, y = 130, width = 100)

        '''----------Cajas Abiertas----------'''
        self.lblCajas = Label(text="Cajas Abiertas")
        self.lblCajas.place(x=20, y = 160)
        self.cajas = Entry(width=60)
        self.cajas.place(x=130, y = 160, width = 100)

        '''----------Cantidad Minima de Productos----------'''
        self.lblCMinProductos = Label(text="Productos minimos")
        self.lblCMinProductos.place(x=20, y = 130)
        self.minprod = Entry(width=60)
        self.minprod.place(x=130, y = 130, width = 100)

        '''----------Cantidad Maxima de Productos----------'''
        self.lblCMaxProductos = Label(text="Productos Maximo")
        self.lblCMaxProductos.place(x=20, y = 160)
        self.maxprod = Entry(width=60)
        self.maxprod.place(x=130, y = 160, width = 100)

        '''----------Tiempo Seleccion----------'''
        self.lblTS = Label(text="Tiempo seleccion")
        self.lblTS.place(x=20, y = 190)
        self.TS = Entry(width=60)
        self.TS.place(x=130, y = 190, width = 100)

        '''----------Tiempo Marcadp----------'''
        self.lblTM = Label(text="Tiempo Marcado")
        self.lblTM.place(x=20, y = 220)
        self.TM = Entry(width=60)
        self.TM.place(x=130, y = 220, width = 100)

        '''----------Tiempo Pago----------'''
        self.lblTP = Label(text="Tiempo Pago")
        self.lblTP.place(x=10, y =250, width = 100)
        self.TP = Entry(width=60)
        self.TP.place(x=130, y = 250, width = 100)

        self.button = tk.Button(self.frame, text="Simular", command=self.simulate)
        self.button.pack()
        self.button.place(x=130,y=280)
        #arreglar boton que no aparece
        self.frame.pack()

        '''-----------METODOS-----------'''

    def simulate(self):
        try: #Se puede hacer sin exceptions
            Desc = self.desc.get()
            BoolDesc = True
        finally:
            Desc = self.desc.get()
            if len(Desc) <= 0 or len(Desc) > 60:
                BoolDesc = False

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
            #self.master.destroy()
        #else:
            #Abrir segunda pantalla indicando los datos mal ingresados
            #Intentar setear por default los datos ingresados la anteriormente con .insert

def main():
    root = Tk()
    root.title = "Simulador"
    root.geometry('470x550')
    app = Simulador(root)
    root.mainloop()


if __name__ == '__main__':
    main()
