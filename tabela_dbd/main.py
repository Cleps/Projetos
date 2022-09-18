import os
import tkinter as tk
from tkinter import ttk, PhotoImage
import sqlite3
from turtle import back, width
from PIL import Image, ImageTk
#----------database
try:
    os.mkdir('./Data') 
except:
    pass
banco = sqlite3.connect('Data/Data.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE if not exists banco (nome text, vitorias integer, derrotas integer)")
cursor.execute("SELECT * FROM banco")
killers = cursor.fetchall()
lista_killers = ['Trapper', 'Wraith','Nurse','Shape,Myers','Hag','Doctor','Huntress','Cannibal','Pig','Clown','Nightmare','Spirit','Legion','Plage','Oni','Ghost Face','Demogorgon','Executioner','Blight','Deathslinger','Twins','Trickster','Nemesis','Onryō','Cenobite','Artist','Dredge','Mastermind']
if (len(killers)) <= 0:
    for any in lista_killers:
        cursor.execute(f"INSERT INTO banco VALUES('{any}', '0', '0')")

banco.commit()

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("650x520")
        #self.janela.minsize(720,420)
        #self.janela.maxsize(720,420)
        self.janela.title("Registrador de vitorias DeadByDaylight")
#-----------TEMA -- EDIÇÃO DOS STYLES
        s = ttk.Style()
        s.theme_use('clam')
#---------pra ficar GROSSO
        s.configure('Treeview', rowheight=53)

        self.img = Image.open('icons/wallpp.jpg')
        self.imagem = ImageTk.PhotoImage(self.img)
        self.lbl_img = tk.Label(self.janela, image=self.imagem)
        self.image = self.imagem
        self.lbl_img.place(relx=-0.2,rely=-0.2) 

        colunas = ['Nomes', 'Vitorias', 'Derrotas']

        self.frm = tk.Frame(self.janela) # --------- frame twv
        self.frm.place(relx=0.15, rely=0.)

        self.frm_btn = tk.Frame(self.janela) #  -----frame butons
        self.frm_btn.place(relx=0.4,rely=0.87)    

        self.tvw = ttk.Treeview(self.frm, columns=colunas, height=8)
        self.tvw.tag_configure('bold', font=('Roboto Light',12), foreground='grey30') # ---- CONFIGURANDO ESTILO
        self.tvw.pack(side=tk.LEFT)
        

        self.tvw.heading('Nomes', text='Nome')
        self.tvw.heading('Vitorias', text='Vitorias')
        self.tvw.heading('Derrotas', text='Derrotas')
        
        self.tvw.column('#0', width=90)
        self.tvw.column('Nomes', minwidth=0, width=200, anchor=tk.W)
        self.tvw.column('Vitorias', minwidth=0, width=80)
        self.tvw.column('Derrotas', minwidth=0, width=80)

        self.scr = tk.Scrollbar(self.frm, command=self.tvw.yview, orient ="vertical")
        self.scr.pack(side=tk.RIGHT, fill=tk.Y)
        self.tvw.configure(yscrollcommand = self.scr.set)

        self.att_tabela() #atualizando a tabela
        
        

#--------------BUTTONS E LABELS

        self.btn_vic = tk.Button(self.frm_btn, text="Vitoria +", bg="gray60", height=2, width=10, command=self.incrementar_vic)
        self.btn_vic.grid(row=0, column=0)
        self.btn_der = tk.Button(self.frm_btn, text="Derrota +", bg="gray60", height=2, width=10, command=self.incrementar_der)
        self.btn_der.grid(row=0, column=1)

        self.btn_vic_min = tk.Button(self.frm_btn, text="Vitoria -", bg="grey80", height=1, width=10, command=self.decrementar_vic)
        self.btn_vic_min.grid(row=1, column=0)
        self.btn_der_min = tk.Button(self.frm_btn, text="Derrota -", bg="grey80", height=1, width=10, command=self.decrementar_der)
        self.btn_der_min.grid(row=1, column=1)

        self.att_lbl()
        
    def att_lbl(self):
        cursor.execute("SELECT vitorias FROM banco")
        dados = cursor.fetchall()
        vic = 0
        for any in dados:
            vic += any[0]

        cursor.execute("SELECT derrotas FROM banco")
        dados = cursor.fetchall()
        der = 0
        for any in dados:
            der += any[0]
        
        self.lbl_vic = tk.Label(self.frm_btn, text=f"vitorias: {vic}", height=1, width=10)
        self.lbl_vic.grid(row=0, column=2)
        self.lbl_der = tk.Label(self.frm_btn, text=f"Derrotas: {der}", height=1, width=10)
        self.lbl_der.grid(row=1, column=2)
        
    def att_tabela(self):
        cursor.execute("SELECT * FROM banco")
        dados = cursor.fetchall()
        lista=[]
        nomes = ['trapper', 'wraith', 'nurse','myers','hag','doctor','huntress','cannibal','pig', 'clown','nightmare', 'spirit', 'legion', 'plage', 'oni', 'ghostface','demogorgon','executioner','blight','deathslingher','twins','trickster','nemesis','onryo','cenobite','artist','dredge','mastermind']
        lista_enderecos = []
        for any in nomes:
            lista_enderecos.append(f'icons/{any}.png')

        for k in range(28):
            exec(f'self.img_{k} = ImageTk.PhotoImage(Image.open(f"{lista_enderecos[k]}").resize((70,70)))')
            exec(f'lista.append(self.img_{k})')

        cont = 0
        for any in dados:
            self.tvw.insert('','end', image=lista[cont] ,values=(any), tags='bold')
            if cont<27:
                cont+=1
        


    def incrementar_vic(self):
        selecionado = self.tvw.selection()
        itens = self.tvw.item(selecionado, 'values')
        vic = int(itens[1])
        vic += 1
        nome = itens[0]
        derrotas = itens[2]
        cursor.execute(f"UPDATE banco SET vitorias = '{str(vic)}' WHERE nome = '{nome}'")
        banco.commit()
        self.tvw.item(selecionado, values=[nome,vic,derrotas]) 
        self.att_lbl()

    def decrementar_vic(self):
        selecionado = self.tvw.selection()
        itens = self.tvw.item(selecionado, 'values')
        vic = int(itens[1])
        vic -= 1
        nome = itens[0]
        derrotas = itens[2]
        cursor.execute("UPDATE banco SET vitorias = '"+str(vic)+"' WHERE nome = '"+nome+"'")
        banco.commit()
        self.tvw.item(selecionado, values=[nome, vic, derrotas])
        self.att_lbl()

    def incrementar_der(self):
        selecionado = self.tvw.selection()
        itens = self.tvw.item(selecionado, 'values')
        vic = itens[1]
        nome = itens[0]
        derrotas = int(itens[2])
        derrotas += 1
        cursor.execute("UPDATE banco SET derrotas = '"+str(derrotas)+"' WHERE nome = '"+nome+"'")
        banco.commit()
        self.tvw.item(selecionado, values=[nome, vic, derrotas])
        self.att_lbl()

    def decrementar_der(self):
        selecionado = self.tvw.selection()
        itens = self.tvw.item(selecionado, 'values')
        vic = itens[1]
        nome = itens[0]
        derrotas = int(itens[2])
        derrotas -= 1
        cursor.execute("UPDATE banco SET derrotas = '"+str(derrotas)+"' WHERE nome = '"+nome+"'")
        banco.commit()
        self.tvw.item(selecionado, values=[nome, vic, derrotas])
        self.att_lbl()

app = tk.Tk()
Tela(app)
app.mainloop()