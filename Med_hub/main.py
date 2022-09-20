import tkinter as tk




class Tela_loguin:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.geometry('350x500')

        self.frame = tk.Frame(self.janela)
        self.frame.configure(background='grey20')
        self.lbl_img = tk.Label(self.frame, bg='pale green', width=23, height=10)
        self.lbl_img.place(rely=.1, relx=.28)
        self.btn_user = tk.Button(self.frame, text='Sou gerente',  font=("calibre",10,'bold') ,width=15, height=2, command=self.manager)
        self.btn_user.place(rely=.5, relx=.33)
        self.btn_user = tk.Button(self.frame, text='Sou cliente',  font=("calibre",10,'bold'), width=15, height=2)
        self.btn_user.place(rely=.6, relx=.33)
        



        self.janela.mainloop()
    
    def manager(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        #self.top_login = tk.Toplevel(self.janela)
        #self.top_login.geometry('200x130')
        #elf.top_login.configure(background='grey')
        #self.top_login.grab_set()
        self.lbl_img = tk.Label(self.frame, bg='pale green', width=23, height=10)
        self.lbl_img.place(rely=.1, relx=.28)
        self.lbl = tk.Label(self.frame, text='Senha de administrador:', font=("calibre",10,'bold'), bg='grey')
        self.lbl.place(relx=.27, rely=.45)
        self.ent = tk.Entry(self.frame, width=24, show='*')
        self.ent.place(relx=.29,rely=.5)
        self.btn = tk.Button(self.frame, text='Login',width=10, font=("calibre",10,'bold'))
        self.btn.place(relx=.38,rely=.55)


Tela_loguin()