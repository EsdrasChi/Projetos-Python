import tkinter as tk

def converter():
    try:
        cm = float(entry_cm.get())
        metros = cm / 100
        resultado_label.config(text=f"{cm} centímetros equivalem a {metros} metros")
    except ValueError:
        resultado_label.config(text="Por favor, insira um valor válido em centímetros.")

# Configuração da janela
janela = tk.Tk()
janela.title("Conversor de Centímetros para Metros")

# Rótulo e entrada para os centímetros
label_cm = tk.Label(janela, text="Centímetros:")
label_cm.pack()
entry_cm = tk.Entry(janela)
entry_cm.pack()

# Botão para fazer a conversão
converter_button = tk.Button(janela, text="Converter", command=converter)
converter_button.pack()

# Rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Loop principal
janela.mainloop()
