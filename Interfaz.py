from tkinter import *

class Window1:
    def __init__(self, root):
        '''----------DESCRIPCION----------'''
        Lbl1 = Label(root, text="Descripcion")
        Lbl1.grid(column=1, row=1)
        desc = Entry(root, width=15)
        desc.grid(column=2, row=1)
        '''---------Horas diarias de atencion--------------'''
        Lbl11 = Label(root, text="Horas de atencion")
        Lbl11.grid(column=1, row=2)
        horas = Entry(root, width=15)
        horas.grid(column=2, row=2)
        '''----------Periodos de Tiempo----------'''
        Lbl2 = Label(root, text="Periodos de tiempo")
        Lbl2.grid(column=1, row=3)
        period = Entry(root, width=15)
        period.grid(column=2, row=3)
        '''----------Clientes Esperados----------'''
        Lbl3 = Label(root, text="Clientes Esperados")
        Lbl3.grid(column=1, row=4)
        clients = Entry(root, width=15)
        clients.grid(column=2, row=4)
        '''----------Distribucion Clientes por periodo----------'''
        Lbl4 = Label(root, text="Distribucion porcentual")
        Lbl4.grid(column=1, row=5)
        distribucion = Entry(root, width=15)
        distribucion.grid(column=2, row=5)
        '''----------Cajas Abiertas----------'''
        Lbl5 = Label(root, text="Cajas Abiertas")
        Lbl5.grid(column=1, row=6)
        cajas = Entry(root, width=15)
        cajas.grid(column=2, row=6)
        '''----------minima cantiadd de productos----------'''
        Lbl6 = Label(root, text="Productos minimos")
        Lbl6.grid(column=1, row=7)
        mcp = Entry(root, width=15)
        mcp.grid(column=2, row=7)
        '''----------maxima cantiad de productos----------'''
        Lbl7 = Label(root, text="Productos maximos")
        Lbl7.grid(column=1, row=8)
        maxcp = Entry(root, width=15)
        maxcp.grid(column=2, row=8)
        '''----------tiempo promedio seleccion de productos----------'''
        Lbl8 = Label(root, text="Tiempo promedio seleccion")
        Lbl8.grid(column=1, row=9)
        tpp = Entry(root, width=15)
        tpp.grid(column=2, row=9)
        '''----------tiempo promedio seleccion de marcado----------'''
        Lbl9 = Label(root, text="Tiempo promedio marcado")
        Lbl9.grid(column=1, row=10)
        tpm = Entry(root, width=15)
        tpm.grid(column=2, row=10)
        '''----------tiempo promedio seleccion de pago----------'''
        Lbl10 = Label(root, text="Tiempo promedio pago")
        Lbl10.grid(column=1, row=11)
        tppago = Entry(root, width=15)
        tppago.grid(column=2, row=11)
        '''--------------------------'''

        btn = Button(root, text="Simular", command=self.simular)
        btn.grid(column=10, row=10)
    def simular(self):
        descripcion = self.desc.get()
        pass



def main():
    root = Tk()
    root.title("Simulador Supermercados")
    root.geometry('500x400')
    app = Window1(root)
    root.mainloop()
if __name__ == '__main__':
    main()