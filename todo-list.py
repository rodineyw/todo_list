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

frame = tk.Frame(root)
frame.pack(pady=10)

lista_tarefas = tk.Listbox(frame, width=40, height=10, bg="lightgrey")
lista_tarefas.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

lista_tarefas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_tarefas.yview)

entrada = tk.Entry(root, width=40)
entrada.pack(pady=10)

botao_adicionar = tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(side=tk.LEFT, padx=5)

botao_remover = tk.Button(root, text="Remover Tarefa", command=remover_tarefa)
botao_remover.pack(side=tk.LEFT, padx=5)

botao_editar = tk.Button(root, text="Editar Tarefa", command=editar_tarefa)
botao_editar.pack(side=tk.LEFT, padx=5)

root.mainloop()
