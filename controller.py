import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class ReceitasDespesasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Receitas e Despesas")
        self.root.geometry("400x300")
        self.root.configure(bg='#2D2D2D')  # Cor de fundo escura

        # Configurando os estilos
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 10), padding=6)

        # Chama os métodos para configurar a interface
        self.criar_interface()

    def criar_interface(self):
        # Seção: Nova receita
        ttk.Label(self.root, text="Nova receita:", foreground="white", background="#2D2D2D", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.entry_desc_receita = ttk.Entry(self.root, width=20)
        self.entry_desc_receita.grid(row=0, column=1, padx=10)
        self.combo_cat_receita = ttk.Combobox(self.root, values=["Salário", "Venda", "Outro"], width=15)
        self.combo_cat_receita.grid(row=0, column=2, padx=10)
        self.entry_val_receita = ttk.Entry(self.root, width=10)
        self.entry_val_receita.grid(row=0, column=3, padx=10)
        ttk.Button(self.root, text="Adicionar", command=self.adicionar_receita).grid(row=0, column=4, padx=10)

        # Seção: Nova despesa
        ttk.Label(self.root, text="Nova despesa:", foreground="white", background="#2D2D2D", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.entry_desc_despesa = ttk.Entry(self.root, width=20)
        self.entry_desc_despesa.grid(row=1, column=1, padx=10)
        self.combo_cat_despesa = ttk.Combobox(self.root, values=["Alimentação", "Transporte", "Lazer"], width=15)
        self.combo_cat_despesa.grid(row=1, column=2, padx=10)
        self.entry_val_despesa = ttk.Entry(self.root, width=10)
        self.entry_val_despesa.grid(row=1, column=3, padx=10)
        ttk.Button(self.root, text="Adicionar", command=self.adicionar_despesa).grid(row=1, column=4, padx=10)

        # Seção: Excluir
        ttk.Label(self.root, text="Excluir", foreground="white", background="#2D2D2D", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.combo_excluir_tipo = ttk.Combobox(self.root, values=["Receita", "Despesa"], width=10)
        self.combo_excluir_tipo.grid(row=2, column=1, padx=10)
        self.combo_excluir_desc = ttk.Combobox(self.root, values=["Descrição 1", "Descrição 2"], width=15)  # Esses valores podem ser dinâmicos
        self.combo_excluir_desc.grid(row=2, column=2, padx=10)
        ttk.Button(self.root, text="Excluir", command=self.excluir).grid(row=2, column=3, padx=10)

    def adicionar_receita(self):
        descricao = self.entry_desc_receita.get()
        categoria = self.combo_cat_receita.get()
        valor = self.entry_val_receita.get()
        print(f"Receita adicionada: {descricao}, {categoria}, R$ {valor}")

    def adicionar_despesa(self):
        descricao = self.entry_desc_despesa.get()
        categoria = self.combo_cat_despesa.get()
        valor = self.entry_val_despesa.get()
        print(f"Despesa adicionada: {descricao}, {categoria}, R$ {valor}")

    def excluir(self):
        tipo = self.combo_excluir_tipo.get()
        descricao = self.combo_excluir_desc.get()
        print(f"{tipo} excluída: {descricao}")

# Função para abrir a nova janela com a tela de Receitas e Despesas
def abrir_receitas_despesas():
    # Criar uma nova janela
    nova_janela = tk.Toplevel()
    app = ReceitasDespesasApp(nova_janela)

# Inicializando a janela principal com customtkinter
root = ctk.CTk()

# Configurando o frame e o botão
frame_nav = ctk.CTkFrame(root)
frame_nav.grid(row=0, column=0, padx=20, pady=20)

button_receitas = ctk.CTkButton(frame_nav, text="Receitas e Despesas", width=180, height=40, fg_color="#2b2b2b", anchor="w", command=abrir_receitas_despesas)
button_receitas.grid(row=2, column=0, padx=20, pady=(5, 5))

# Executar a aplicação principal
root.mainloop()