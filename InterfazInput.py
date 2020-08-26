from tkinter import *

'''se ingresan los valores mal ingresados para tirar labels con warnings'''


def warnings():
    print("error")



def app():
    print("Hola")

window = Tk()
window.title("Simulador Supermercado")
window.geometry('500x400')
Lbl = Label(window, text="")
Lbl.grid(column=5, row=0)
'''----------DESCRIPCION----------'''
Lbl1 = Label(window, text="Descripcion")
Lbl1.grid(column=1, row=1)
desc = Entry(window, width=15)
desc.grid(column=2, row=1)
'''---------Horas diarias de atencion--------------'''
Lbl11 = Label(window, text="Horas de atencion")
Lbl11.grid(column=1, row=2)
horas = Entry(window, width=15)
horas.grid(column=2, row=2)
'''----------Periodos de Tiempo----------'''
Lbl2 = Label(window, text="Periodos de tiempo")
Lbl2.grid(column=1, row=3)
period = Entry(window, width=15)
period.grid(column=2, row=3)
'''----------Clientes Esperados----------'''
Lbl3 = Label(window, text="Clientes Esperados")
Lbl3.grid(column=1, row=4)
clients = Entry(window, width=15)
clients.grid(column=2, row=4)
'''----------Distribucion Clientes por periodo----------'''
Lbl4 = Label(window, text="Distribucion porcentual")
Lbl4.grid(column=1, row=5)
distribucion = Entry(window, width=15)
distribucion.grid(column=2, row=5)
'''----------Cajas Abiertas----------'''
Lbl5 = Label(window, text="Cajas Abiertas")
Lbl5.grid(column=1, row=6)
cajas = Entry(window, width=15)
cajas.grid(column=2, row=6)
'''----------minima cantiadd de productos----------'''
Lbl6 = Label(window, text="Productos minimos")
Lbl6.grid(column=1, row=7)
mcp = Entry(window, width=15)
mcp.grid(column=2, row=7)
'''----------maxima cantiad de productos----------'''
Lbl7 = Label(window, text="Productos maximos")
Lbl7.grid(column=1, row=8)
maxcp = Entry(window, width=15)
maxcp.grid(column=2, row=8)
'''----------tiempo promedio seleccion de productos----------'''
Lbl8 = Label(window, text="Tiempo promedio seleccion")
Lbl8.grid(column=1, row=9)
tpp = Entry(window, width=15)
tpp.grid(column=2, row=9)
'''----------tiempo promedio seleccion de marcado----------'''
Lbl9 = Label(window, text="Tiempo promedio marcado")
Lbl9.grid(column=1, row=10)
tpm = Entry(window, width=15)
tpm.grid(column=2, row=10)
'''----------tiempo promedio seleccion de pago----------'''
Lbl10 = Label(window, text="Tiempo promedio pago")
Lbl10.grid(column=1, row=11)
tppago = Entry(window, width=15)
tppago.grid(column=2, row=11)
'''--------------------------'''

simular = Button(window, text="Simular", command=getters)
simular.grid(column=10, row=10)

window.mainloop()

def main():
    app()
