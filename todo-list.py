import tkinter as tk
from tkinter import messagebox
from customtkinter import CTk, CTkButton


def adicionar_tarefa():
    """
    This function adicionar_tarefa takes no parameters and does not return anything.
    It gets the input from the variable entrada, checks if there is a value, inserts the value at the end of lista_tarefas, and then deletes the input value in entrada.
    """
    tarefa = entrada.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada.delete(0, tk.END)


def remover_tarefa():
    """
    A function to remove a task from the list of tasks.
    """
    try:
        index = lista_tarefas.curselection()[0]
        lista_tarefas.delete(index)
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para remover.")


def editar_tarefa():
    """
    Save the tasks to a file named 'tarefas.txt'.
    """
    try:
        index = lista_tarefas.curselection()[0]
        tarefa_atual = lista_tarefas.get(index)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, tarefa_atual)
        lista_tarefas.delete(index)
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para editar.")

    def limpar_tarefas():
        """
        Clear all tasks from the listbox.
        """
        lista_tarefas.delete(0, tk.END)


root = CTk()
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

botao_adicionar = CTkButton(
    master=root,
    text="Adicionar Tarefa",
    command=adicionar_tarefa,
    bg_color=cor_botao,
    fg_color="white",
    font=("Roboto", 12, "bold"),
)
botao_adicionar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

botao_remover = CTkButton(
    master=root,
    text="Remover Tarefa",
    command=remover_tarefa,
    bg_color=cor_botao,
    fg_color="white",
    font=("Roboto", 12, "bold"),
)
botao_remover.pack(side=tk.LEFT, padx=5)

botao_editar = CTkButton(
    master=root,
    text="Editar Tarefa",
    command=editar_tarefa,
    bg_color=cor_botao,
    fg_color="white",
    font=("Roboto", 12, "bold"),
)
botao_editar.pack(side=tk.LEFT, padx=5)

root.mainloop()
