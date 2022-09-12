import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo Treeview TABELA")
        self.janela.geometry('580x280')
        # -------------FRAME PADRÃO
        self.frame = tk.Frame(self.janela)
        self.frame.pack(side=tk.TOP)
        # ------------FRAME DE BOTÕES
        self.btn_frm = tk.Frame(self.janela)
        self.btn_frm.pack(side=tk.BOTTOM)

        colunas = ["Nome", 'CPF', 'Email']

        self.tvw = ttk.Treeview(self.frame, show="headings", columns=colunas)
        self.tvw.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # ------CABEÇALHO
        self.tvw.heading('Nome', text='Nome')
        self.tvw.heading('CPF', text='CPF')
        self.tvw.heading('Email', text='Email')

        self.tvw.column('Nome', minwidth=0, width=100)
        self.tvw.column('CPF', minwidth=0, width=150)
        self.tvw.column('Email', minwidth=0, width=200)

        # ---------EXEMPLOS INSERIDOS MANUALMENTE
        self.tvw.insert("", 'end', values=['Rogerio', '23434234', 'rogerio@emailmassa.com'])
        self.tvw.insert("", 'end', values=['Machon', '234234234', 'Maxon@email.com'])
        self.tvw.insert("", 'end', values=['Maicow Jacks', '234234234234', 'rusbé@gmail.com'])

        # -----------SCROLLBAR
        self.scr = tk.Scrollbar(self.frame, command=self.tvw.yview).pack(side=tk.RIGHT, fill=tk.Y)

        # ------------BOTÕES NO FRAME BOTOES

        self.btn_cad = tk.Button(self.btn_frm, text="Cadastrar", command=self.tela_cadastrar)
        self.btn_cad.pack(side=tk.LEFT)

        self.btn_del = tk.Button(self.btn_frm, text="Deletar", command=self.deletar_selecionar)
        self.btn_del.pack(side=tk.LEFT)

        self.btn_deltds = tk.Button(self.btn_frm, text="Deletar todos", command=self.deletar_todos)
        self.btn_deltds.pack(side=tk.LEFT)
        self.btn_delsel = tk.Button(self.btn_frm, text="Deletar selecionados", command=self.deletar_selecionados)
        self.btn_delsel.pack(side=tk.LEFT)

        self.btn_att = tk.Button(self.btn_frm, text="Atualizar", command=self.tela_atualizar)
        self.btn_att.pack(side=tk.RIGHT)

    def tela_atualizar(self):
        # ---------jogando tudo num ifelse apos pegar info de qntos estão selecionados
        selecionado = self.tvw.selection()
        cont = 0
        cont += len(selecionado)

        if cont > 1:
            messagebox.showwarning('ERRO!', 'Selecione apenas um usuario!')
        elif cont == 1:
            self.top_atualizar = tk.Toplevel(self.janela)
            self.top_atualizar.title("cadastro")
            self.top_atualizar.geometry("300x120")
            lista = self.tvw.item(selecionado, 'values')
            self.janela.withdraw()
            # self.top_cadastro.grab_set()

            self.lbl_nam = tk.Label(self.top_atualizar, text="Nome:")
            self.lbl_nam.grid(row=0, column=0)

            self.ent_nam = tk.Entry(self.top_atualizar)
            self.ent_nam.grid(row=0, column=1)
            self.ent_nam.insert(0, lista[0])

            self.lbl_cpf = tk.Label(self.top_atualizar, text="CPF:")
            self.lbl_cpf.grid(row=1, column=0)
            self.ent_cpf = tk.Entry(self.top_atualizar)
            self.ent_cpf.grid(row=1, column=1)
            self.ent_cpf.insert(0, lista[1])

            self.lbl_ema = tk.Label(self.top_atualizar, text="Email:")
            self.lbl_ema.grid(row=2, column=0)
            self.ent_ema = tk.Entry(self.top_atualizar)
            self.ent_ema.grid(row=2, column=1)
            self.ent_ema.insert(0, lista[2])

            self.btn_cnf = tk.Button(self.top_atualizar, text="Confirmar", command=self.confirmar_atualiza)
            self.btn_cnf.grid(row=3, column=0)
        else:
            messagebox.showwarning('ERRO!', 'Nenhum usuario foi selecionado')

    def confirmar_atualiza(self):
        nome = self.ent_nam.get()
        cpf = self.ent_cpf.get()
        email = self.ent_ema.get()

        selecionado = self.tvw.selection()
        lista = self.tvw.item(selecionado, 'values')

        if lista[0] == nome and lista[1] == cpf and lista[2] == email:
            messagebox.showwarning('Erro', 'Você não atualizou nada!')
        else:
            self.tvw.item(selecionado, values=(nome, cpf, email))
            self.top_atualizar.destroy()
            self.janela.deiconify()

    def deletar_todos(self):
        todos = self.tvw.get_children()
        ver = messagebox.askquestion('Cuidado', 'Você esta certo disso?')
        if ver == "yes":
            for t in todos:
                self.tvw.delete(t)

    def deletar_selecionados(self):
        lista = self.tvw.selection()
        for i in lista:
            self.tvw.delete(i)

    def deletar_selecionar(self):
        selecionado = self.tvw.selection()
        self.tvw.delete(selecionado)

    def tela_cadastrar(self):

        self.top_cadastro = tk.Toplevel(self.janela)
        self.top_cadastro.title("cadastro")
        self.top_cadastro.geometry("300x120")

        self.janela.withdraw()
        # self.top_cadastro.grab_set()

        self.lbl_nam = tk.Label(self.top_cadastro, text="Nome:")
        self.lbl_nam.grid(row=0, column=0)

        self.ent_nam = tk.Entry(self.top_cadastro)
        self.ent_nam.grid(row=0, column=1)

        self.lbl_cpf = tk.Label(self.top_cadastro, text="CPF:")
        self.lbl_cpf.grid(row=1, column=0)

        self.ent_cpf = tk.Entry(self.top_cadastro)
        self.ent_cpf.grid(row=1, column=1)

        self.lbl_ema = tk.Label(self.top_cadastro, text="Email:")
        self.lbl_ema.grid(row=2, column=0)

        self.ent_ema = tk.Entry(self.top_cadastro)
        self.ent_ema.grid(row=2, column=1)

        self.btn_cnf = tk.Button(self.top_cadastro, text="Confirmar", command=self.confirmar_cadastro)
        self.btn_cnf.grid(row=3, column=0)

    def confirmar_cadastro(self):
        # check = self.ent_nam.get() == '' or self.ent_cpf.get() == '' or self.ent_ema.get()==''
        nome = self.ent_nam.get()
        email = self.ent_ema.get()
        cpf = self.ent_cpf.get()
        # if check:
        if nome == '' or email == '' or cpf == "":
            messagebox.showwarning("ERRO!!!!!", "Nenhum dos campos pode ficar vazio!", parent=self.top_cadastro)
        else:
            self.tvw.insert("", "end", values=(nome, email, cpf))
            self.top_cadastro.destroy()
            self.janela.deiconify()


app = tk.Tk()
Tela(app)
app.mainloop()