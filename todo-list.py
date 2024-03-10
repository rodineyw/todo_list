import tkinter as tk
from tkinter import messagebox


def adicionar_tarefa():
    tarefa = entrada.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada.delete(0, tk.END)


def remover_tarefa():
    try:
        index = lista_tarefas.curselection()[0]
        lista_tarefas.delete(index)
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para remover.")


def editar_tarefa():
    try:
        index = lista_tarefas.curselection()[0]
        tarefa_atual = lista_tarefas.get(index)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, tarefa_atual)
        lista_tarefas.delete(index)
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para editar.")


root = tk.Tk()
root.title("To-Do List")

# Paleta de cores
cor_principal = "#3498db"
cor_secundaria = "#acf0f1"
cor_botao = "#2ecc71"

frame = tk.Frame(root, bg=cor_secundaria)
frame.pack(pady=10)

lista_tarefas = tk.Listbox(
    frame,
    width=40,
    height=10,
    bg="lightgrey",
    bd=0,
    selectbackground=cor_principal,
    font=("Roboto", 12),
    highlightthickness=0,
)
lista_tarefas.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

lista_tarefas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_tarefas.yview)

entrada = tk.Entry(root, width=40, font=("Roboto", 12))
entrada.pack(pady=10)

botao_adicionar = tk.Button(
    root,
    text="Adicionar Tarefa",
    command=adicionar_tarefa,
    bg=cor_botao,
    fg="white",
    font=("Roboto", 12, "bold"),
    relief=tk.FLAT,
)
botao_adicionar.pack(side=tk.LEFT, padx=5)

botao_remover = tk.Button(
    root,
    text="Remover Tarefa",
    command=remover_tarefa,
    bg=cor_botao,
    fg="white",
    font=("Roboto", 12, "bold"),
    relief=tk.FLAT,
)
botao_remover.pack(side=tk.LEFT, padx=5)

botao_editar = tk.Button(
    root,
    text="Editar Tarefa",
    command=editar_tarefa,
    bg=cor_botao,
    fg="white",
    font=("Roboto", 12, "bold"),
    relief=tk.FLAT,
)
botao_editar.pack(side=tk.LEFT, padx=5)

root.mainloop()
