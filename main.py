import os
import tkinter as tk
from tkinter import ttk, PhotoImage
import sqlite3
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
        cursor.execute(f"INSERT INTO banco VALUES('{any}', 0, 0)")

banco.commit()

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("820x520")
        #self.janela.minsize(720,420)
        #self.janela.maxsize(720,420)
        self.janela.title("Registrador de vitorias DeadByDaylight")
#-----------TEMA -- EDIÇÃO DOS STYLES
        s = ttk.Style()
        s.theme_use('clam')
#---------pra ficar GROSSO
        s.configure('Treeview', rowheight=40)

        self.img = Image.open('icons/wallpp.jpg')
        self.imagem = ImageTk.PhotoImage(self.img)
        self.lbl_img = tk.Label(self.janela, image=self.imagem)
        self.image = self.imagem
        self.lbl_img.place(relx=-0.2,rely=-0.2) 

        colunas = ['Nomes', 'Vitorias', 'Derrotas']
        self.frm = tk.Frame(self.janela)
        self.frm.place(relx=0.1, rely=0)

        self.frm_btn = tk.Frame(self.janela)
        self.frm_btn.place(relx=0.4,rely=0.83)    

        self.tvw = ttk.Treeview(self.frm, columns=colunas, height=10)
        self.tvw.pack(side=tk.LEFT)

        self.tvw.heading('Nomes', text='Nome')
        self.tvw.heading('Vitorias', text='Vitorias')
        self.tvw.heading('Derrotas', text='Derrotas')
        
        self.tvw.column('Nomes', minwidth=0, width=200)
        self.tvw.column('Vitorias', minwidth=0, width=80)
        self.tvw.column('Derrotas', minwidth=0, width=80)
        self.scr = tk.Scrollbar(self.frm, command=self.tvw.yview).pack(side=tk.RIGHT, fill=tk.Y)

        self.att_tabela() #atualizando a tabela
        

#--------------BUTTONS E LABELS
        self.btn_vic = tk.Button(self.frm_btn, text="Vitoria +", bg="dodger blue", height=2, width=10, command=self.incrementar_vic)
        self.btn_vic.grid(row=0, column=0)
        self.btn_der = tk.Button(self.frm_btn, text="Derrota +", bg="dodger blue", height=2, width=10, command=self.incrementar_der)
        self.btn_der.grid(row=0, column=1)

        self.btn_vic_min = tk.Button(self.frm_btn, text="Vitoria -", bg="pale violet red", height=1, width=10, command=self.decrementar_vic)
        self.btn_vic_min.grid(row=1, column=0)
        self.btn_der_min = tk.Button(self.frm_btn, text="Derrota -", bg="pale violet red", height=1, width=10, command=self.decrementar_der)
        self.btn_der_min.grid(row=1, column=1)
        
    def att_tabela(self):
        cursor.execute("SELECT * FROM banco")
        dados = cursor.fetchall()
        lista=[]
        nomes = ['trapper', 'wraith', 'nurse','myers','hag','doctor','huntress','cannibal','pig', 'clown','nightmare', 'spirit', 'legion', 'plage', 'oni', 'ghostface','demogorgon','executioner','blight','deathslingher','twins','trickster','nemesis','onryo','cenobite','artist','dredge','mastermind']
        lista_enderecos = []
        for any in nomes:
            lista_enderecos.append(f'icons/{any}.png')

        for k in range(28):
            exec(f'self.img_{k} = ImageTk.PhotoImage(Image.open(f"{lista_enderecos[k]}"))')
            exec(f'lista.append(self.img_{k})')

        cont = 0
        for any in dados:
            self.tvw.insert('','end', image=lista[cont] ,values=(any))
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

app = tk.Tk()
Tela(app)
app.mainloop()
