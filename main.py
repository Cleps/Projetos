import tkinter as tk
from tkinter import ttk
class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("840x620")
        self.janela.title("BDB Registrer")
#-----------TEMA -- EDIÇÃO DOS STYLES
        s = ttk.Style()
        s.theme_use('clam')
#---------pra ficar GROSSO
        s.configure('Treeview', rowheight=40)

        colunas = ['Nomes', 'Vitorias', 'Derrotas']
        self.frm = tk.Frame(self.janela)
        self.frm.pack()
        self.frm_btn = tk.Frame(self.janela)
        self.frm_btn.pack()

        self.tvw = ttk.Treeview(self.frm, show="headings", columns=colunas, height=13)
        self.tvw.pack()
        self.tvw.heading('Nomes', text='Nome')
        self.tvw.heading('Vitorias', text='Vitorias')
        self.tvw.heading('Derrotas', text='Derrotas')
        self.tvw.column('Nomes', minwidth=0, width=300)
        self.tvw.column('Vitorias', minwidth=0, width=100)
        self.tvw.column('Derrotas', minwidth=0, width=100)


        for i in range(1):
            self.tvw.insert('', 'end', values=['Trapper',0, 0])

#--------------BUTTONS E LABELS
        self.btn_vic = tk.Button(self.frm_btn, text="Vitoria +", bg="dodger blue", height=2, width=10, command=self.incrementar_vic)
        self.btn_vic.pack(side=tk.LEFT)
        self.btn_der = tk.Button(self.frm_btn, text="Derrota +", bg="dodger blue", height=2, width=10, command=self.incrementar_der)
        self.btn_der.pack(side=tk.LEFT)

       
        self.btn_vic_min = tk.Button(self.frm_btn, text="Vitoria -", bg="pale violet red", height=1, width=10, command=self.decrementar_vic)
        self.btn_vic_min.pack(side=tk.TOP)
        self.btn_der_min = tk.Button(self.frm_btn, text="Derrota -", bg="pale violet red", height=1, width=10, command=self.decrementar_der)
        self.btn_der_min.pack(side=tk.BOTTOM)


    def incrementar_vic(self):
        selecionado = self.tvw.selection()
        itens = self.tvw.item(selecionado, 'values')
        vic = int(itens[1])
        vic += 1
        nome = itens[0]
        derrotas = itens[2]
        self.tvw.item(selecionado, values=[nome,vic,derrotas])

    def decrementar_vic(self):
        selecionado = self.tvw.selection()
        itens = self.tvw.item(selecionado, 'values')
        vic = int(itens[1])
        vic -= 1
        nome = itens[0]
        derrotas = itens[2]
        self.tvw.item(selecionado, values=[nome, vic, derrotas])

    def incrementar_der(self):
        selecionado = self.tvw.selection()
        itens = self.tvw.item(selecionado, 'values')
        vic = itens[1]
        nome = itens[0]
        derrotas = int(itens[2])
        derrotas += 1
        self.tvw.item(selecionado, values=[nome, vic, derrotas])

    def decrementar_der(self):
        selecionado = self.tvw.selection()
        itens = self.tvw.item(selecionado, 'values')
        vic = itens[1]
        nome = itens[0]
        derrotas = int(itens[2])
        derrotas -= 1
        self.tvw.item(selecionado, values=[nome, vic, derrotas])

app = tk.Tk()
Tela(app)
app.mainloop()
