import tkinter as tk
from tkinter import *


def simulate():
    print("Simulando")


class Simulador:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button = tk.Button(self.frame, text="Simular", command=simulate)



def main():
    root = Tk()
    root.title = "Simulador"
    root.geometry('270x270')
    app = Simulador(root)
    root.mainloop()


if __name__ == '__main__':
    main()
