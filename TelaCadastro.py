import tkinter as tk
from tkinter import ttk
from Cachorro import Cachorro
from Gato import Gato

animais = []

def cadastrar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    tipo = tipo_var.get()

    if tipo == "Cachorro":
        porte = entry_porte.get()
        animal = Cachorro(nome, idade, porte)
    elif tipo == "Gato":
        raca = entry_raca.get()
        animal = Gato(nome, idade, raca)

    animais.append(animal)
    atualizar_lista()

def atualizar_lista():
    lista_animais.delete(0, tk.END)
    for animal in animais:
        lista_animais.insert(tk.END, animal.mostrar())

janela = tk.Tk()
janela.title("Cadastro de Animais")
janela.geometry("500x400")

notebook = ttk.Notebook(janela)
notebook.pack(expand=True, fill="both")

tab_cadastro = ttk.Frame(notebook)
notebook.add(tab_cadastro, text="Cadastro")

tab_lista = ttk.Frame(notebook)
notebook.add(tab_lista, text="Lista")

tk.Label(tab_cadastro, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(tab_cadastro)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(tab_cadastro, text="Idade:").grid(row=1, column=0, padx=10, pady=5)
entry_idade = tk.Entry(tab_cadastro)
entry_idade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(tab_cadastro, text="Tipo:").grid(row=2, column=0, padx=10, pady=5)
tipo_var = tk.StringVar(value="Cachorro")
tk.Radiobutton(tab_cadastro, text="Cachorro", variable=tipo_var, value="Cachorro").grid(row=2, column=1, sticky="w")
tk.Radiobutton(tab_cadastro, text="Gato", variable=tipo_var, value="Gato").grid(row=2, column=1, sticky="e")

tk.Label(tab_cadastro, text="Porte (Cachorro):").grid(row=3, column=0, padx=10, pady=5)
entry_porte = tk.Entry(tab_cadastro)
entry_porte.grid(row=3, column=1, padx=10, pady=5)

tk.Label(tab_cadastro, text="Raça (Gato):").grid(row=4, column=0, padx=10, pady=5)
entry_raca = tk.Entry(tab_cadastro)
entry_raca.grid(row=4, column=1, padx=10, pady=5)

tk.Button(tab_cadastro, text="Cadastrar", command=cadastrar).grid(row=5, columnspan=2, pady=10)

lista_animais = tk.Listbox(tab_lista)
lista_animais.pack(expand=True, fill="both", padx=10, pady=10)

janela.mainloop()
