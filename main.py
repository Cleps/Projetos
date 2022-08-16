import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo Treeview TABELA")
        self.janela.geometry('480x280')
        # -------------FRAME PADRÃO
        self.frame = tk.Frame(self.janela)
        self.frame.pack(side=tk.TOP)
        # ------------FRAME DE BOTÕES
        self.btn_frm = tk.Frame(self.janela)
        self.btn_frm.pack(side=tk.BOTTOM)
        #------------FRAME DO MAIS E MENOS
        self.frm_btn = tk.Frame(self.janela)
        self.frm_btn.pack(side=tk.RIGHT)


        colunas = ["Nome", 'Vitorias', 'Derrotas']

        self.tvw = ttk.Treeview(self.frame, show="headings", columns=colunas)
        self.tvw.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # ------CABEÇALHO
        self.tvw.heading('Nome', text='Nome')
        self.tvw.heading('Vitorias', text='Vitorias')
        self.tvw.heading('Derrotas', text='Derrotas')

        self.tvw.column('Nome', minwidth=0, width=150)
        self.tvw.column('Vitorias', minwidth=0, width=80)
        self.tvw.column('Derrotas', minwidth=0, width=80)

        # ---------EXEMPLOS INSERIDOS MANUALMENTE
        self.tvw.insert("", 'end', values=('Rogerio', 0,0))
        self.tvw.insert("", 'end', values=('Machon', '0','0'))
        self.tvw.insert("", 'end', values=('Maicow Jacks', '0','0'))

        # -----------SCROLLBAR
        self.scr = tk.Scrollbar(self.frame, command=self.tvw.yview).pack(side=tk.RIGHT, fill=tk.Y)

        # ------------BOTÕES NO FRAME BOTOES

        self.btn = tk.Button(self.btn_frm, text="+", command=self.incrementar)
        self.btn.pack(side=tk.LEFT)

    def incrementar(self):
        select = self.tvw.selection()
        select[1]+=1

        self.btn_min = tk.Button(self.btn_frm, text="-")
        self.btn_min.pack(side=tk.RIGHT)

        #------------MAIS E MENOS BUTTON






app = tk.Tk()
Tela(app)
app.mainloop()