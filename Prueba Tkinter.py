from tkinter import *

def clicked():
    text1 = txt.get()
    lbl.configure(text = text1)
window = Tk()
window.title("App")
lbl = Label(window, text = "Hello", font =("new times roman", 14) )
lbl.grid(column = 1, row = 0)
txt = Entry(window,width = 10)
#txt.focus() //para escribir altiro en el cuadro de texto
txt.grid(column = 5, row = 0)
window.geometry('400x300')
btn = Button(window, text = "Click", command = clicked)
btn.grid(column = 7, row = 7)


window.mainloop()