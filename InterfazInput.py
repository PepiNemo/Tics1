from tkinter import *


def getters():
    '''-----get-----'''
    descripcion = desc.get()
    periodos = int(period.get())
    esperados = int(clients.get())
    cantidad_min = int(mcp.get())
    cantidad_max = int(maxcp.get())
    seleccion = int(tpp.get())
    marcado = int(tpm.get())
    pago = int(tppago.get())

    dist = distribucion.get().split(",")
    distribucion_arr = []
    for i in dist:
        distribucion_arr.append(int(i))

    cajas_arr = []
    box = cajas.get().split(",")
    for i in box:
        cajas_arr.append(int(i))
    window.destroy()


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
'''----------Periodos de Tiempo----------'''
Lbl2 = Label(window, text="Periodos de tiempo")
Lbl2.grid(column=1, row=2)
period = Entry(window, width=15)
period.grid(column=2, row=2)
'''----------Clientes Esperados----------'''
Lbl3 = Label(window, text="Periodos de tiempo")
Lbl3.grid(column=1, row=3)
clients = Entry(window, width=15)
clients.grid(column=2, row=3)
'''----------Distribucion Clientes por periodo----------'''
Lbl4 = Label(window, text="Distribucion porcentual")
Lbl4.grid(column=1, row=5)
distribucion = Entry(window, width=15)
distribucion.grid(column=2, row=5)
#Los valores se ingresan separados por comas y sin espacios
#Hacer un separador por comas
'''----------Cajas Abiertas----------'''
Lbl5 = Label(window, text="Cajas Abiertas")
Lbl5.grid(column=1, row=3)
cajas = Entry(window, width=15)
cajas.grid(column=2, row=3)
#Hacer un separador por comas
'''----------minima cantiadd de productos----------'''
Lbl6 = Label(window, text="Productos minimos")
Lbl6.grid(column=1, row=3)
mcp = Entry(window, width=15)
mcp.grid(column=2, row=3)
'''----------maxima cantiad de productos----------'''
Lbl7 = Label(window, text="Productos maximos")
Lbl7.grid(column=1, row=3)
maxcp = Entry(window, width=15)
maxcp.grid(column=2, row=3)
'''----------tiempo promedio seleccion de productos----------'''
Lbl8 = Label(window, text="Tiempo promedio seleccion")
Lbl8.grid(column=1, row=3)
tpp = Entry(window, width=15)
tpp.grid(column=2, row=3)
'''----------tiempo promedio seleccion de marcado----------'''
Lbl9 = Label(window, text="Tiempo promedio marcado")
Lbl9.grid(column=1, row=3)
tpm = Entry(window, width=15)
tpm.grid(column=2, row=3)
'''----------tiempo promedio seleccion de pago----------'''
Lbl10 = Label(window, text="Tiempo promedio pago")
Lbl10.grid(column=1, row=3)
tppago = Entry(window, width=15)
tppago.grid(column=2, row=3)








simularButton = Button(window, text="Simular", command=getters())
simularButton.grid(column=10, row=10)

window.mainloop()
