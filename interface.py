import teste as test
import tkinter as tk

def func_btn(dados):
    print(dados)

# Cria a janela principal
window = tk.Tk()
window.geometry('200x100')
window.title("Gerador de imagens")

# Cria a caixa de texto para o prompt
prompt_entry = tk.Entry(window)
prompt_entry.pack()

# Cria o botao
generate_button = tk.Button(window, text="Gerar", command=lambda: test.gerar(prompt_entry.get()))
generate_button.pack()

# Inicia a janela
window.mainloop()
