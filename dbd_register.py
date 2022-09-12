import tkinter as tk
from tkinter import ttk
class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("840x620")
        self.janela.title("BDB Registrer")

        self.frm = tk.Frame(self.janela)
        self.frm.pack()

        self.lbl_nom = tk.Label(self.frm, text="NOMES")
        self.lbl_nom.pack()
        self.lbl_vic = tk.Label(self.frm, text="VITORIAS")
        self.lbl_vic.pack()
        self.lbl_der = tk.Label(self.frm, text="DERROTAS")
        self.lbl_der.pack()



app = tk.Tk()
Tela(app)
app.mainloop()