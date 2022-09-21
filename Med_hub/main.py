import tkinter as tk




class Tela_loguin:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.geometry('350x500')
        self.janela.configure(background='grey20')

            
        self.lbl_img = tk.Label(self.janela, bg='pale green', width=23, height=10)
        self.lbl_img.place(rely=.1, relx=.28)
        self.btn_gen = tk.Button(self.janela, text='Sou gerente',  font=("calibre",10,'bold') ,width=15, height=2, command=self.manager)
        self.btn_gen.place(rely=.5, relx=.33)
        self.btn_user = tk.Button(self.janela, text='Sou cliente',  font=("calibre",10,'bold'), width=15, height=2)
        self.btn_user.place(rely=.6, relx=.33)
        



        self.janela.mainloop()
    
    def manager(self):
        for widget in self.janela.winfo_children():
            widget.destroy()
        #self.top_login = tk.Toplevel(self.janela)
        #self.top_login.geometry('200x130')
        #elf.top_login.configure(background='grey')
        #self.top_login.grab_set()
        self.lbl_img = tk.Label(self.janela, bg='pale green', width=23, height=10)
        self.lbl_img.place(rely=.1, relx=.28)
        self.btn_voltar = tk.Button(self.janela, text='Voltar',command=self.voltar_janela).place(relx=.05, rely=.02)
        self.lbl = tk.Label(self.janela, text='Senha de administrador:', font=("calibre",10,'bold'), bg='grey')
        self.lbl.place(relx=.27, rely=.45)
        self.ent = tk.Entry(self.janela, width=24, show='*')
        self.ent.place(relx=.29,rely=.5)
        self.btn = tk.Button(self.janela, text='Login',width=10, font=("calibre",10,'bold'))
        self.btn.place(relx=.38,rely=.55)
    
    def voltar_janela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()
        self.lbl_img = tk.Label(self.janela, bg='pale green', width=23, height=10)
        self.lbl_img.place(rely=.1, relx=.28)
        self.btn_gen = tk.Button(self.janela, text='Sou gerente',  font=("calibre",10,'bold') ,width=15, height=2, command=self.manager)
        self.btn_gen.place(rely=.5, relx=.33)
        self.btn_user = tk.Button(self.janela, text='Sou cliente',  font=("calibre",10,'bold'), width=15, height=2)
        self.btn_user.place(rely=.6, relx=.33)

Tela_loguin()
