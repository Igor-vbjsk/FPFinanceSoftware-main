"""
Pra facilitar a compilacao do projeto em um arquivo .exe,
vamos realizar todo o projeto em um unico arquivo, assim a gente
garante um executável único sem dependência de arquivos solto
"""

###########################################

# IMPORTS
import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tempfile
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
import json
import gdown
from tkinter import messagebox
from tkinter import Toplevel, Label, Frame
from matplotlib.figure import Figure



import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils import validar_entrada_data, validar_entrada_numerica
from plot import plot_monthly_balance, plot_spends_by_category, plot_revenue_by_category
from datetime import datetime
from ast import literal_eval
import os

# APPLICATIONS

# criacao do appdata
global appdatafolder
global data_path
appdata = os.getenv('LOCALAPPDATA')
appdatafolder = appdata + "\\NoVerde"
data_path = appdatafolder + "\\data.txt"
if not os.path.exists(appdatafolder):
    os.makedirs(appdatafolder)
    
# Download dos arquivos necessários ao AppData
icon_ico_url = "https://drive.google.com/file/d/1I6XgDbEMmfk7slzFgFUhckzb2Hh68ZAy/view?usp=sharing"
icon_png_url = "https://drive.google.com/file/d/1lu68-uMr4Vla6oyxhks1adOpkjHhoiId/view?usp=sharing"
icon_ico_path = appdatafolder + "\\icon.ico"
icon_png_path = appdatafolder + "\\icon.png"
gdown.download(icon_ico_url, icon_ico_path, quiet=False, fuzzy=True)
gdown.download(icon_png_url, icon_png_path, quiet=False, fuzzy=True)

# Handling

def on_closing():
    with open(data_path, "w", encoding='utf-8') as data_file:
        datas = [reservas, receitas, despesas]
        for dados in datas:
            dados = str(dados) + "\n"
            data_file.write(dados)
    if 'temp_dir' in globals():
        tempfile.tempdir.cleanup() # Um Handling ativado quando a janela fechar, fazendo com que a pasta temporaria seja limpa e deletada
    janela.destroy() # fecha a janela
    exit(0) # garante o fim do projeto



# DESIGN UI/UX

#------------ TELA PARA O USUÁRIO INSERIR SEUS GASTOS INICIO --------------------------------------------------------------------------------------#

#Essa é a tela seguindo o modelo que a Lu fez no Figma

def receita_botao():
    
    janela_mensagem = ctk.CTk()
    janela_mensagem.title("")
    
    largura_janela = 300
    altura_janela = 100
    # Obtém a largura e a altura da tela e centraliza a janela
    largura_tela = janela_mensagem.winfo_screenwidth()
    altura_tela = janela_mensagem.winfo_screenheight()
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2
    janela_mensagem.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")


    mensagem = tk.Label(janela_mensagem, bg="green", text="VOCÊ INSERIU UMA NOVA RECEITA", font=ctk.CTkFont(size=20,
                                            weight="bold")).grid(row=2, column=0, padx=10, pady=10)
    janela_mensagem.mainloop()

def despesa_botao():
    janela_mensagem = ctk.CTk()
    janela_mensagem.title("")
    
    largura_janela = 300
    altura_janela = 100
    # Obtém a largura e a altura da tela e centraliza a janela
    largura_tela = janela_mensagem.winfo_screenwidth()
    altura_tela = janela_mensagem.winfo_screenheight()
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2
    janela_mensagem.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")


    mensagem = tk.Label(janela_mensagem, bg="red", text="VOCÊ INSERIU UMA NOVA DESPESA", font=ctk.CTkFont(size=20,
                                            weight="bold")).grid(row=2, column=0, padx=10, pady=10)
    janela_mensagem.mainloop()




def mostrar_receitas_despesas():
    limpar_frame(conteudo_frame)
    # widgets da tela de receitas e despesas
    label_titulo = ctk.CTkLabel(conteudo_frame, text="Receitas e Despesas", font=ctk.CTkFont(size=20, weight="bold"))
    label_titulo.grid(row=0, column=0, pady=20, padx=20)
    

    # Listas globais para armazenar receitas e despesas
receitas = []
despesas = []


# adicionar uma nova receita
def receita_botao():
    descricao = receita_descricao_entry.get()
    categoria = receita_categoria_combobox.get()
    valor = receita_valor_entry.get()

    if descricao and categoria and valor:
        receitas.append({"descricao": descricao, "categoria": categoria, "valor": valor})
        atualizar_combobox()
        messagebox.showinfo("Sucesso", "Receita adicionada com sucesso!")
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos para adicionar uma receita.")

#  adicionar uma nova despesa
def despesa_botao():
    descricao = despesa_descricao_entry.get()
    categoria = despesa_categoria_combobox.get()
    valor = despesa_valor_entry.get()

    if descricao and categoria and valor:
        despesas.append({"descricao": descricao, "categoria": categoria, "valor": valor})
        atualizar_combobox()
        messagebox.showinfo("Sucesso", "Despesa adicionada com sucesso!")
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos para adicionar uma despesa.")

#excluir receita ou despesa
def excluir_botao():
    tipo = excluir_tipo_combobox.get()
    descricao = excluir_descricao_combobox.get()

    if tipo == "Receita":
        receitas[:] = [r for r in receitas if r["descricao"] != descricao]
    elif tipo == "Despesa":
        despesas[:] = [d for d in despesas if d["descricao"] != descricao]
    
    atualizar_combobox()
    messagebox.showinfo("Sucesso", f"{tipo} excluída com sucesso!")

#opções das descrições nas combobox de exclusão
def atualizar_combobox():
    receitas_descricoes = [r["descricao"] for r in receitas]
    despesas_descricoes = [d["descricao"] for d in despesas]
    
    excluir_descricao_combobox.configure(values=receitas_descricoes + despesas_descricoes)

#criar a tela de receitas e despesas
def mostrar_receitas_despesas():
    global receita_descricao_entry, receita_categoria_combobox, receita_valor_entry
    global despesa_descricao_entry, despesa_categoria_combobox, despesa_valor_entry
    global excluir_tipo_combobox, excluir_descricao_combobox
    
    limpar_frame(conteudo_frame)

    # Título
    label_titulo = ctk.CTkLabel(conteudo_frame, text="Receitas e Despesas", font=ctk.CTkFont(size=20, weight="bold"))
    label_titulo.grid(row=0, column=0, pady=20, padx=20)

    # Nova receita
    ctk.CTkLabel(conteudo_frame, text="Nova receita:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
    receita_descricao_entry = ctk.CTkEntry(conteudo_frame, width=200, placeholder_text="Descrição")
    receita_descricao_entry.grid(row=1, column=1, padx=10)
    receita_categoria_combobox = ctk.CTkComboBox(conteudo_frame, values=["Salário", "Venda", "Outro"])
    receita_categoria_combobox.grid(row=1, column=2, padx=10)
    ctk.CTkLabel(conteudo_frame, text="R$").grid(row=1, column=3, padx=10, pady=10, sticky='w')
    receita_valor_entry = ctk.CTkEntry(conteudo_frame, width=100, placeholder_text="Valor")
    receita_valor_entry.grid(row=1, column=3, padx=5)
    ctk.CTkButton(conteudo_frame, fg_color="#2D4C48", hover_color="#2C6961", text="Adicionar", command=receita_botao).grid(row=1, column=4, padx=10)

    # Nova despesa
    ctk.CTkLabel(conteudo_frame, text="Nova despesa:").grid(row=2, column=0, padx=10, pady=10, sticky='w')
    despesa_descricao_entry = ctk.CTkEntry(conteudo_frame, width=200, placeholder_text="Descrição")
    despesa_descricao_entry.grid(row=2, column=1, padx=10)
    despesa_categoria_combobox = ctk.CTkComboBox(conteudo_frame, values=["Alimentação", "Transporte", "Lazer"])
    despesa_categoria_combobox.grid(row=2, column=2, padx=10)
    ctk.CTkLabel(conteudo_frame, text="R$").grid(row=2, column=3, padx=10, pady=10, sticky='w')
    despesa_valor_entry = ctk.CTkEntry(conteudo_frame, width=100, placeholder_text="Valor")
    despesa_valor_entry.grid(row=2, column=3, padx=10)
    ctk.CTkButton(conteudo_frame, fg_color="#2D4C48", hover_color="#2C6961", text="Adicionar", command=despesa_botao).grid(row=2, column=4, padx=10)

    # Excluir
    ctk.CTkLabel(conteudo_frame, text="Excluir:").grid(row=3, column=0, padx=10, pady=10, sticky='w')
    excluir_tipo_combobox = ctk.CTkComboBox(conteudo_frame, values=["Receita", "Despesa"])
    excluir_tipo_combobox.grid(row=3, column=1, padx=10)
    excluir_descricao_combobox = ctk.CTkComboBox(conteudo_frame, values=[])
    excluir_descricao_combobox.grid(row=3, column=2, padx=10)
    ctk.CTkButton(conteudo_frame, fg_color="#4D2D2D", hover_color="#702E2E", text="Excluir", command=excluir_botao).grid(row=3, column=3, padx=10)

    # Atualizar combobox de exclusão com as descrições de receitas e despesas
    atualizar_combobox()   

# limpar  frame principal
def limpar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# Reservas
reservas = {}

# gráfico de pizza
def desenhar_grafico():
    # Limpa o gráfico anterior antes de desenhar um novo
    for widget in conteudo_frame.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()
  # cor de fundo
    cor_de_fundo = "#2b2b2b"

    # cor de fundo
    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(aspect="equal"), facecolor=cor_de_fundo)

    if reservas:
        # Dados do gráfico
        data = list(reservas.values())  # Usa os valores atualizados
        labels = list(reservas.keys())

        # Gráfico de pizza
        wedges, texts, autotexts = ax.pie(data, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

        # Ajuste de cores do texto para branco
        plt.setp(autotexts, color="white")
        plt.setp(texts, color="white")

    else:
        # Caso não haja reservas, exibir um gráfico vazio
        ax.text(0, 0, '', horizontalalignment='center', verticalalignment='center', fontsize=14, color='white')

    # Cor de fundo do gráfico (Axes)
    ax.set_facecolor(cor_de_fundo)

    # Adiciona o gráfico no canvas do tkinter
    canvas = FigureCanvasTkAgg(fig, master=conteudo_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=5, rowspan=5, padx=20, pady=10)

# atualizar os comboboxes quando criar uma nova reserva
def atualizar_comboboxes():
    combo_reserva['values'] = list(reservas.keys())
    combo_resgatar['values'] = list(reservas.keys())
    combo_excluir['values'] = list(reservas.keys())

# criar uma nova reserva
def criar_nova_reserva():
    nome = entry_nome.get()
    try:
        valor_inicial = float(entry_valor_inicial.get())
        if nome and nome not in reservas:
            reservas[nome] = valor_inicial
            atualizar_comboboxes()  # Atualiza os comboboxes
            atualizar_grafico()  # Atualiza o gráfico
        else:
            print("Nome inválido ou reserva já existente.")
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

# Função para adicionar valor à reserva
def adicionar_reserva():
    nome = combo_reserva.get()
    try:
        valor = float(entry_valor_adicionar.get())
        if nome in reservas:
            reservas[nome] += valor
        atualizar_grafico()
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

# Função para resgatar valor da reserva
def resgatar_reserva():
    nome = combo_resgatar.get()
    try:
        valor = float(entry_valor_resgatar.get())
        if nome in reservas and reservas[nome] >= valor:
            reservas[nome] -= valor
        else:
            print("Reserva não encontrada.")
        atualizar_grafico()
    except ValueError:
        print("Valor numérico invalido.")

# Função para adicionar valor à reserva
def adicionar_reserva():
    nome = combo_reserva.get()
    try:
        valor = float(entry_valor_adicionar.get())
        if nome in reservas:
            reservas[nome] += valor
        atualizar_grafico()
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

# Função para resgatar valor da reserva
def resgatar_reserva():
    nome = combo_resgatar.get()
    try:
        valor = float(entry_valor_resgatar.get())
        if nome in reservas and reservas[nome] >= valor:
            reservas[nome] -= valor
        else:
            print("Reserva não encontrada.")
        atualizar_grafico()
    except ValueError:
        print("Valor numérico invalido.")

#atualizar o gráfico
def atualizar_grafico():
    desenhar_grafico()
    
    #confirmar exclusão

def ver_reservas():
     #Cria a janela principal
    reservas_menu = ctk.CTk()
    reservas_menu.title("VALORES EM RESERVA")
    largura_janela = 200
    altura_janela = 400
    reservas_menu.geometry(f"{largura_janela}x{altura_janela}+{(reservas_menu.winfo_screenwidth() - largura_janela) // 2}+{(reservas_menu.winfo_screenheight() - altura_janela) // 2}")


    # Exibe o conteúdo do dicionário em uma Label
    texto_reservas = ""
    for reserva, detalhes in reservas.items():
        texto_reservas += f"{reserva}: {detalhes}\n\n"

    label_reservas = ctk.CTkLabel(reservas_menu, text=texto_reservas, font=ctk.CTkFont(size=15, weight="bold"))
    label_reservas.pack(padx=20, pady=20)

    reservas_menu.mainloop()



def confirmar_exclusao():
    nome = combo_excluir.get()
    if nome in reservas:
        valor_reserva = reservas[nome]
        # Criação da janela de confirmação
        janela_confirmacao = tk.Toplevel(conteudo_frame)
        janela_confirmacao.title("Confirmar Exclusão")
        janela_confirmacao.configure(bg="#333")

        # Label de confirmação com o valor da reserva
        lbl_confirmacao = tk.Label(janela_confirmacao, text=f"Você tem um valor de {valor_reserva} armazenado na reserva '{nome}'.\nTem certeza de que deseja excluí-la?", fg="white", bg="#333", padx=20, pady=10)
        lbl_confirmacao.pack()

        # Botões de cancelar e excluir
        frame_botoes = tk.Frame(janela_confirmacao, bg="#333")
        frame_botoes.pack(pady=10)

        btn_cancelar = tk.Button(frame_botoes, text="Cancelar", bg="#333", fg="white", command=janela_confirmacao.destroy)
        btn_cancelar.grid(row=0, column=0, padx=10)

        btn_excluir_confirmado = tk.Button(frame_botoes, text="Excluir", bg="#a33c38", fg="white", command=lambda: excluir_reserva(nome, janela_confirmacao))
        btn_excluir_confirmado.grid(row=0, column=1, padx=10)

def show_explicação():
    messagebox.showinfo("Crie o nome de uma nova reserva, ex:'Despesas de emergencia',"
    "e o valor a qual inicialmente terá na reserva")

#excluir a reserva após confirmação
def excluir_reserva(nome, janela):
    if nome in reservas:
        del reservas[nome]
        atualizar_comboboxes()
        atualizar_grafico()
    janela.destroy()


#criar a tela de "Reservas"
def mostrar_reservas():
    # Apaga o frame atual e cria um novo frame
    for widget in conteudo_frame.winfo_children():
        widget.destroy()

    # Elementos na tela de reservas
    lbl_titulo = ctk.CTkLabel(conteudo_frame, text="Reservas", font=('Arial', 16), )
    lbl_titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    info_button = ctk.CTkButton(conteudo_frame, text="?", width=2, command=show_explicação)
    info_button.grid(row=0, column=3)

    # "Nova reserva"
    lbl_nova = ctk.CTkLabel(conteudo_frame, text="Nova reserva:",)
    lbl_nova.grid(row=1, column=0, sticky="e", padx=5)
    global entry_nome
    entry_nome = ctk.CTkEntry(conteudo_frame, placeholder_text="DESCRIÇÃO")
    entry_nome.grid(row=1, column=1, padx=5)
    global entry_valor_inicial
    entry_valor_inicial = ctk.CTkEntry(conteudo_frame, placeholder_text="VALOR")
    entry_valor_inicial.grid(row=1, column=2, padx=5)
    btn_adicionar = ctk.CTkButton(conteudo_frame, text="Adicionar", command=criar_nova_reserva)
    btn_adicionar.grid(row=1, column=3, padx=5)

    #"Adicionar à reserva"
    lbl_adicionar = ctk.CTkLabel(conteudo_frame, text="Adicionar à reserva:",)
    lbl_adicionar.grid(row=2, column=0, sticky="e", padx=5)
    global combo_reserva
    combo_reserva = ttk.Combobox(conteudo_frame)
    combo_reserva.grid(row=2, column=1, padx=5)
    global entry_valor_adicionar
    entry_valor_adicionar = ctk.CTkEntry(conteudo_frame)
    entry_valor_adicionar.grid(row=2, column=2, padx=5)
    btn_adicionar_valor = ctk.CTkButton(conteudo_frame, text="Adicionar", command=adicionar_reserva)
    btn_adicionar_valor.grid(row=2, column=3, padx=5)

    #"Resgatar da reserva"
    lbl_resgatar = ctk.CTkLabel(conteudo_frame, text="Resgatar da reserva:",)
    lbl_resgatar.grid(row=3, column=0, sticky="e", padx=5)
    global combo_resgatar
    combo_resgatar = ttk.Combobox(conteudo_frame)
    combo_resgatar.grid(row=3, column=1, padx=5)
    global entry_valor_resgatar
    entry_valor_resgatar = ctk.CTkEntry(conteudo_frame)
    entry_valor_resgatar.grid(row=3, column=2, padx=5)
    btn_resgatar = ctk.CTkButton(conteudo_frame, text="Resgatar", command=resgatar_reserva)
    btn_resgatar.grid(row=3, column=3, padx=5)


    #"Excluir reserva"
    lbl_excluir = ctk.CTkLabel(conteudo_frame, text="Excluir reserva:",)
    lbl_excluir.grid(row=4, column=0, sticky="e", padx=5)
    global combo_excluir
    combo_excluir = ttk.Combobox(conteudo_frame)
    combo_excluir.grid(row=4, column=1, padx=5)
    btn_excluir = ctk.CTkButton(conteudo_frame, text="Excluir", command=confirmar_exclusao)
    btn_excluir.grid(row=4, column=3, padx=5)



    # mostrar reserva
    btn_mostrarRes = ctk.CTkButton(conteudo_frame, text="MOSTRAR RESERVAS", command=ver_reservas)
    btn_mostrarRes.grid(row=6, column=2, padx=5)

    

    # Frame para as informações e botões
    frame_informacoes = tk.Frame(conteudo_frame, bg="#333")
    frame_informacoes.grid(row=0, column=0, padx=20, pady=20, sticky="n")

    # Frame para o gráfico (ou quadrado branco)
    frame_grafico = tk.Frame(conteudo_frame, bg="#333")
    frame_grafico.grid(row=0, column=1, padx=20, pady=20, sticky="n")

    desenhar_grafico()

# Cotações
def mostrar_cotacoes():
    # a partir daqui é a parte da visualização das cotações

    limpar_frame(conteudo_frame)
    #label = ctk.CTkLabel(conteudo_frame, text="Cotações de Moedas", font=ctk.CTkFont(size=20, weight="bold"))
    #label.pack(pady=20, padx=20)

    # Label para mostrar a data e hora atual
    label_data_hora = ctk.CTkLabel(conteudo_frame, text="--/--/---- --:--:--", font=("Arial", 30, "bold"))
    label_data_hora.pack(pady=10)
    # Labels para mostrar as cotações com espaçamento entre elas
    label_usd = ctk.CTkLabel(conteudo_frame, text="Dólar -> 1 USD = R$ --", font=("Arial", 14, "bold"), 
    fg_color="dimgray",text_color="green", width= 200, corner_radius=8, padx=10, pady=5)
    label_usd.pack(pady=10)

    label_btc = ctk.CTkLabel(conteudo_frame, text="Bitcoin -> 1 BTC = R$ --", font=("Arial", 14, "bold"), 
      fg_color="dimgray", text_color="gold", width= 200, corner_radius=8, padx=10, pady=5)
    label_btc.pack(pady=10)

    label_eur = ctk.CTkLabel(conteudo_frame, text="Euro -> 1 EUR = R$ --", font=("Arial", 14, "bold"), 
            fg_color="dimgray", text_color="blue", width= 200, corner_radius=8, padx=10, pady=5)
    label_eur.pack(pady=10)

    # icone de atualizar
    icon_path = appdatafolder + "\\icon.png"
    icone_atualizar = ctk.CTkImage(light_image=Image.open(icon_path), size=(20, 20))
    
    # Botão para atualizar as cotações com o ícone de imagem
    botao_atualizar = ctk.CTkButton(conteudo_frame, text="", command=atualizar, 
                                image=icone_atualizar, width=70, height=70, fg_color="transparent")
    botao_atualizar.pack(pady=20)

    # faz a requisição da cotação na API
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacao = requisicao.json()
    cotacao_usd = cotacao['USDBRL']['bid']
    cotacao_btc = cotacao['BTCBRL']['bid']
    cotacao_eur = cotacao['EURBRL']['bid']
        
        
    label_usd.configure(text=f"1 DÓLAR = R$ {cotacao_usd}")
    label_btc.configure(text=f"1 BITCOIN = R$ {cotacao_btc}")
    label_eur.configure(text=f"1 EURO = R$ {cotacao_eur}")
        
      
    data_hora_atual = datetime.now()
    data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y - %H:%M:%S")
    label_data_hora.configure(text=f"{data_hora_formatada}")

def atualizar():
    mostrar_cotacoes()
    
    

# Janela principal
janela = ctk.CTk()
janela.title("NoVerde Finanças")
janela.geometry("1400x900")
janela.iconbitmap(appdatafolder + '\\Icon.ico')

#Insercao de valores armazeados ao iniciar
if os.path.isfile(data_path):
    with open(data_path, "r") as data_file:
        for i, line in enumerate(data_file):
            if i == 0:
                if line != "{}" and line != "":
                    reservas = eval(line.strip())
            elif i == 1:
                if line != "[]" and line != "":
                    receitas = literal_eval(line.strip())
            elif i == 2:
                if line != "[]" and line != "":
                    despesas = literal_eval(line.strip())

# Frame da navegação lateral
nav_frame = ctk.CTkFrame(janela, width=200)
nav_frame.grid(row=0, column=0, sticky="ns")

#barra lateral esquerda
btn_dashboard = ctk.CTkButton(nav_frame, text="Dashboard",fg_color="#2b2b2b",hover_color="#2D4C48", anchor="w", width=180, height=40)
btn_dashboard.grid(row=0, column=0, padx=20, pady=(20, 5))

btn_receitas_despesas = ctk.CTkButton(nav_frame, text="Receitas e Despesas",fg_color="#2b2b2b",hover_color="#2D4C48", anchor="w", width=180, height=40, command=mostrar_receitas_despesas)
btn_receitas_despesas.grid(row=1, column=0, padx=20, pady=5)


btn_reservas = ctk.CTkButton(nav_frame, text="Reservas",fg_color="#2b2b2b",hover_color="#2D4C48", anchor="w", width=180, height=40, command=mostrar_reservas)
btn_reservas.grid(row=2, column=0, padx=20, pady=5)

btn_cotacoes = ctk.CTkButton(nav_frame, text="Cotações",fg_color="#2b2b2b",hover_color="#2D4C48", anchor="w", width=180, height=40, command=mostrar_cotacoes)
btn_cotacoes.grid(row=3, column=0, padx=20, pady=5)

# Frame do conteúdo principal
conteudo_frame = ctk.CTkFrame(janela)
conteudo_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

# Formatação da dela
janela.grid_columnconfigure(1, weight=1)
janela.grid_rowconfigure(0, weight=1)

janela.protocol("WM_DELETE_WINDOW", on_closing)
janela.mainloop()