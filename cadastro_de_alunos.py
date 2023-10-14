import tkinter as tk

def cadastrar_aluno():
    nome = entry_nome.get()
    idade = entry_idade.get()
    nota = entry_nota.get()
    
    if nome and idade and nota:
        # Exibe os dados no terminal
        print(f"Nome: {nome}, Idade: {idade}, Nota: {nota}")
        
        # Limpa os campos de entrada após o cadastro
        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)
        entry_nota.delete(0, tk.END)

# Cria a janela principal
root = tk.Tk()
root.title("Cadastro de Alunos")

# Cria rótulos e caixas de entrada para nome, idade e nota
label_nome = tk.Label(root, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

label_idade = tk.Label(root, text="Idade:")
label_idade.pack()
entry_idade = tk.Entry(root)
entry_idade.pack()

label_nota = tk.Label(root, text="Nota:")
label_nota.pack()
entry_nota = tk.Entry(root)
entry_nota.pack()

# Cria o botão de cadastro
button_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_aluno)
button_cadastrar.pack()

# Inicia a interface gráfica
root.mainloop()
