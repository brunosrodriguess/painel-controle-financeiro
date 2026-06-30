import customtkinter as ctk
from tkinter import messagebox, ttk
import sqlite3

# CONFIGURAÇÕES

ctk.set_appearance_mode ("system")
ctk.set_default_color_theme ("blue")

# BANCO DE DADOS

def criar_banco():

    conexao = sqlite3.connect("sistema_financas_historico.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lancamentos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT,
            categoria TEXT,
            subcategoria TEXT,
            metodo_pagamento TEXT,
            conta_bancaria TEXT,
            data TEXT,
            valor REAL
    )         
    """)

    conexao.commit()
    conexao.close()

# PALETA DE CORES

COR_FUNDO = "#D2D2D2"
COR_TITULO =  "#FFFFFF"
COR_MENU = "#577B54"
COR_TEXTO =  "#000000"
COR_TEXTO_LANCAR = "#FFFFFF"
COR_TEXTO_LIMPAR = "#FFFFFF"
COR_TEXTO_JANELA = "#000000"
COR_CAMPOS = "#E8E8E8"
COR_BOTAO_LANCAR = "#3A7B34"
COR_BOTAO_LIMPAR = "#616774"
COR_INTERACAO_LANCAR = "#30672A"
COR_INTERACAO_LIMPAR = "#393D44"

# PADRÕES DE INTERFACE JANELA LANCAMENTO

LARGURA_CAMPOS_LANCAMENTO = 280
ALTURA_CAMPOS_LANCAMENTO = 46
MARGEM_Y_TOPO = (50,11)
MARGEM_Y =  11
MARGEM_X = 87
FONTE = "Roboto"
FONTE_LABEL = ("Roboto", 24, "normal")
FONTE_ENTRY = ("Roboto", 15, "normal")
FONTE_COMBOBOX = ("Roboto", 15, "normal")
FONTE_BOTAO_LANCAR = ("Roboto", 17, "bold")
FONTE_BOTAO_LIMPAR = ("Roboto", 17, "bold")
ALINHAMENTO = "w"
ARREDONDAMENTO = 15

## VARIÁVEIS LISTA SUSPENSA JANELA LANCAMENTO

TEXTO_PADRAO_CATEGORIA = "Selecione uma categoria"
TEXTO_PADRAO_SUBCATEGORIA = "Selecione uma subcategoria"
TEXTO_PADRAO_METODO_PAGAMENTO = "Selecione um método"
TEXTO_PADRAO_CONTA_BANCARIA = "Selecione uma conta"

CATEGORIAS = [
    "Alimentação",
    "Moradia",
    "Transporte",
    "Saúde",
    "Educação",
    "Lazer",
    "Compras",
    "Assinaturas",
]

SUBCATEGORIAS_ALIMENTACAO = [
    "Mercado",
    "Padaria",
    "Restaurante",
    "Lanche",
    "Delivery",
    "Feira",
]

SUBCATEGORIAS_MORADIA = [
    "Aluguel",
    "Condomínio",
    "Água",
    "Energia",
    "Internet",
    "IPTU",
    "Gás",
    "Manutenção",
]

SUBCATEGORIAS_TRANSPORTE = [
    "Gasolina",
    "Etanol",
    "Diesel",
    "Uber",
    "Táxi",
    "Ônibus",
    "Pedágio",
    "Estacionamento",
    "Manutenção",
    "Seguro",
]

SUBCATEGORIAS_SAUDE = [
    "Farmácia",
    "Médico",
    "Dentista",
    "Exames",
    "Plano de Saúde",
]

SUBCATEGORIAS_EDUCACAO = [
    "Faculdade",
    "Curso",
    "Livros",
    "Material Escolar",
]

SUBCATEGORIAS_LAZER = [
    "Cinema",
    "Viagem",
    "Jogos",
    "Streaming",
    "Eventos",
    "Passeios",
]

SUBCATEGORIAS_COMPRAS = [
    "Roupas",
    "Eletrônicos",
    "Casa",
    "Presentes",
    "Investimentos",
    "Ações",
    "Tesouro Direto",
    "CDB",
    "Criptomoedas",
    "Fundos",
]

SUBCATEGORIAS_ASSINATURAS = [
    "Netflix",
    "Amazon Prime Video",
    "Disney+",
    "HBO Max",
    "Apple TV+",
    "Paramount+",
    "Globoplay",
    "MUBI",
    "Crunchyroll",
    "Looke",
    "Telecine",
    "Spotify",
    "YouTube Music",
    "Apple Music",
    "Deezer",
    "Tidal",
    "Amazon Music",
    "Xbox Game Pass",
    "PlayStation Plus",
    "Nintendo Switch Online",
    "EA Play",
    "Ubisoft+",
    "GeForce NOW",
    "Google One",
    "iCloud",
    "Dropbox",
    "OneDrive",
    "MEGA",
    "ChatGPT",
    "Claude Pro",
    "Gemini Advanced",
    "Perplexity Pro",
    "GitHub Copilot",
    "Midjourney",
    "Microsoft 365",
    "Google Workspace",
    "Notion",
    "Canva Pro",
    "Adobe Creative Cloud",
    "Kindle Unlimited",
    "Audible",
    "Duolingo Super",
    "LinkedIn Premium",
    "Strava Premium",
]

SUBCATEGORIAS = {
    "Alimentação" : SUBCATEGORIAS_ALIMENTACAO,
    "Moradia" : SUBCATEGORIAS_MORADIA,
    "Transporte" : SUBCATEGORIAS_TRANSPORTE,
    "Saúde" : SUBCATEGORIAS_SAUDE,
    "Educação" : SUBCATEGORIAS_EDUCACAO,
    "Lazer" : SUBCATEGORIAS_LAZER,
    "Compras" : SUBCATEGORIAS_COMPRAS,
    "Assinaturas" : SUBCATEGORIAS_ASSINATURAS
}

METODO_PAGAMENTO = [
    "Dinheiro",
    "PIX",
    "Cartão de Débito",
    "Cartão de Crédito",
    "Boleto Bancário",
    "Transferência Bancária (TED/DOC)",
    "Saldo em Conta",
    "Carteira Digital",
    "Vale-Alimentação",
    "Vale-Refeição"
]

CONTA_BANCARIA = [
    "Nubank",
    "Inter",
    "Itaú",
    "Santander",
    "Banco do Brasil",
    "Caixa",
    "Bradesco",
    "C6 Bank",
    "Mercado Pago",
    "PicPay",
]

# FUNÇÃO BOTÕES FRAME SUPERIOR

def mostrar_janela_lancamento():
    janela_botao_lancamento.tkraise()

def mostrar_janela_resumo():
    janela_botao_resumo.tkraise()

def mostrar_janela_historico():
    janela_botao_historico.tkraise()

# FUNÇÃO BOTÃO SUBCATEGORIA JANELA LANCAMENTO

def carregar_subcategoria(categoria):
    subcategorias = SUBCATEGORIAS[categoria]
    combobox_subcategoria.configure (values = subcategorias)
    combobox_subcategoria.set (TEXTO_PADRAO_SUBCATEGORIA)

# FUNÇÃO DIGITAÇÃO DATA JANELA LANCAMENTO

def aplicar_mascara_data (event):
    data_digitada = entry_data.get()
    for caractere in data_digitada:
        if caractere.isdigit ():
            apenas_numeros += caractere
    apenas_numeros = apenas_numeros [:8]
    if len(apenas_numeros) == 0:
        data_formatada = ""
    elif len(apenas_numeros) == 1:
        data_formatada = f"{apenas_numeros[:2]}"
    elif len(apenas_numeros) == 2:
        data_formatada = f"{apenas_numeros[:2]}/"
    elif len(apenas_numeros) == 3:
        data_formatada = f"{apenas_numeros[:2]}/{apenas_numeros[2:4]}"
    elif len(apenas_numeros) == 4:
        data_formatada = f"{apenas_numeros[:2]}/{apenas_numeros[2:4]}/"
    else:
        data_formatada = f"{apenas_numeros[:2]}/{apenas_numeros[2:4]}/{apenas_numeros[4:8]}"

    entry_data.delete(0, "end")
    entry_data.insert(0, data_formatada)

# FUNÇÃO DIGITAÇÃO VALOR JANELA LANCAMENTO

def aplicar_mascara_valor (event):
    valor_digitado = entry_valor.get()
    apenas_numeros = ""
    for caractere in valor_digitado:
        if caractere.isdigit ():
            apenas_numeros += caractere
    apenas_numeros = apenas_numeros [:8]
    if len(apenas_numeros) == 0:
        valor_formatado = ""
    elif len(apenas_numeros) == 1:
        valor_formatado = f"R$ 0,0{apenas_numeros}"
    elif len(apenas_numeros) == 2:
        valor_formatado = f"R$ 0,{apenas_numeros}"
    else:
        inteiro = int(apenas_numeros [:-2])
        decimal = apenas_numeros [-2:]
        inteiro = f"{inteiro:,}".replace(",", ".")
        valor_formatado = f"R$ {inteiro},{decimal}"

    entry_valor.delete(0, "end")
    entry_valor.insert(0, valor_formatado)

# JANELA PRINCIPAL

janela_principal = ctk.CTk ()
janela_principal.title ("Painel de Controle Financeiro")
janela_principal.geometry ("1300x700")
janela_principal.resizable (False, False)
janela_principal.configure (fg_color = COR_FUNDO)

# FRAME SUPERIOR

frame_superior = ctk.CTkFrame (janela_principal,
    width = 1300,
    height = 110,
    fg_color = COR_MENU)

frame_superior.pack (padx = 0, pady = 0)

frame_superior.pack_propagate(False)

## TÍTULO FRAME SUPERIOR

titulo_frame_superior = ctk.CTkLabel (frame_superior,
    text = "PAINEL DE CONTROLE FINANCEIRO", 
    font = ("Roboto", 30, "bold"),
    text_color = COR_TITULO)

titulo_frame_superior.pack (side = "left", padx = 40)

## BOTÃO HISTÓRICO

botao_historico = ctk.CTkButton (frame_superior,
    text = "Histórico",
    width = 156,
    height = 51,
    corner_radius = 15,
    fg_color = COR_FUNDO,
    text_color = COR_TEXTO,
    hover_color = COR_TITULO,
    command = mostrar_janela_historico,
    font = ("Roboto", 18, "normal"))

botao_historico.pack (side = "right", padx = 20)

## BOTÃO RESUMO

botao_resumo = ctk.CTkButton (frame_superior,
    text = "Resumo",
    width = 156,
    height = 51,
    corner_radius = 15,
    fg_color = COR_FUNDO,
    text_color = COR_TEXTO,
    hover_color = COR_TITULO,
    command = mostrar_janela_resumo,
    font = ("Roboto", 18, "normal"))

botao_resumo.pack (side = "right", padx = 20)

## BOTÃO LANCAMENTO

botao_lancamento = ctk.CTkButton (frame_superior,
    text = "Lançamento",
    width = 156,
    height = 51,
    corner_radius = 15,
    fg_color = COR_FUNDO,
    text_color = COR_TEXTO,
    hover_color = COR_TITULO,
    command = mostrar_janela_lancamento,
    font = ("Roboto", 18, "normal"))

botao_lancamento.pack (side = "right", padx = 20)

# JANELA DOS BOTÕES

janela_botoes = ctk.CTkFrame (janela_principal,
   fg_color = COR_FUNDO) 

janela_botoes.pack (fill = "both", expand = True)

## JANELA LANCAMENTO

janela_botao_lancamento = ctk.CTkFrame (janela_botoes,
    fg_color = COR_FUNDO)

titulo_descricao = ctk.CTkLabel (janela_botao_lancamento,
    text = "Descrição",
    text_color = COR_TEXTO_JANELA,
    font = FONTE_LABEL)

titulo_descricao.grid (row = 0, column = 1, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y_TOPO)

entry_descricao = ctk.CTkEntry (janela_botao_lancamento,
    placeholder_text = "Ex: Supermercado Tauste",
    fg_color = COR_CAMPOS,
    font = FONTE_ENTRY,
    text_color = COR_TEXTO_JANELA,
    height = ALTURA_CAMPOS_LANCAMENTO,
    width = LARGURA_CAMPOS_LANCAMENTO,
    corner_radius = ARREDONDAMENTO)

entry_descricao.grid (row = 1, column = 1, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y)

titulo_categoria = ctk.CTkLabel (janela_botao_lancamento,
    text = "Categoria",
    text_color = COR_TEXTO_JANELA,
    font = FONTE_LABEL)

titulo_categoria.grid (row = 2, column = 1, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y_TOPO)

combobox_categoria = ctk.CTkComboBox (janela_botao_lancamento,
    fg_color = COR_CAMPOS,
    font = FONTE_COMBOBOX,
    text_color = COR_TEXTO_JANELA,
    height = ALTURA_CAMPOS_LANCAMENTO,
    width = LARGURA_CAMPOS_LANCAMENTO,
    corner_radius = ARREDONDAMENTO,
    command = carregar_subcategoria,
    values = CATEGORIAS)

combobox_categoria.set (TEXTO_PADRAO_CATEGORIA)

combobox_categoria.grid (row = 3, column = 1, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y)

titulo_subcategoria = ctk.CTkLabel (janela_botao_lancamento,
    text = "Subcategoria",
    text_color = COR_TEXTO_JANELA,
    font = FONTE_LABEL)

titulo_subcategoria.grid (row = 4, column = 1, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y_TOPO)

combobox_subcategoria = ctk.CTkComboBox (janela_botao_lancamento,
    fg_color = COR_CAMPOS,
    font = FONTE_COMBOBOX,
    text_color = COR_TEXTO_JANELA,
    height = ALTURA_CAMPOS_LANCAMENTO,
    width = LARGURA_CAMPOS_LANCAMENTO,
    corner_radius = ARREDONDAMENTO,
    values = [])

combobox_subcategoria.set (TEXTO_PADRAO_SUBCATEGORIA)

combobox_subcategoria.grid (row = 5, column = 1, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y)

titulo_metodo_pagamento = ctk.CTkLabel (janela_botao_lancamento,
    text = "Método de pagamento",
    text_color = COR_TEXTO_JANELA,
    font = FONTE_LABEL)

titulo_metodo_pagamento.grid (row = 0, column = 3, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y_TOPO)

combobox_metodo_pagamento = ctk.CTkComboBox (janela_botao_lancamento,
    fg_color = COR_CAMPOS,
    font = FONTE_COMBOBOX,
    text_color = COR_TEXTO_JANELA,
    height = ALTURA_CAMPOS_LANCAMENTO,
    width = LARGURA_CAMPOS_LANCAMENTO,
    corner_radius = ARREDONDAMENTO,
    values = METODO_PAGAMENTO)

combobox_metodo_pagamento.set (TEXTO_PADRAO_METODO_PAGAMENTO)

combobox_metodo_pagamento.grid (row = 1, column = 3, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y)

titulo_conta_bancaria = ctk.CTkLabel (janela_botao_lancamento,
    text = "Conta bancária",
    text_color = COR_TEXTO_JANELA,
    font = FONTE_LABEL)

titulo_conta_bancaria.grid (row = 2, column = 3, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y_TOPO)

combobox_conta_bancaria = ctk.CTkComboBox (janela_botao_lancamento,
    fg_color = COR_CAMPOS,
    font = FONTE_COMBOBOX,
    text_color = COR_TEXTO_JANELA,
    height = ALTURA_CAMPOS_LANCAMENTO,
    width = LARGURA_CAMPOS_LANCAMENTO,
    corner_radius = ARREDONDAMENTO,
    values = CONTA_BANCARIA)

combobox_conta_bancaria.set (TEXTO_PADRAO_CONTA_BANCARIA)

combobox_conta_bancaria.grid (row = 3, column = 3, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y)

titulo_data = ctk.CTkLabel (janela_botao_lancamento,
    text = "Data",
    text_color = COR_TEXTO_JANELA,
    font = FONTE_LABEL)

titulo_data.grid (row = 4, column = 3, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y_TOPO)

entry_data = ctk.CTkEntry (janela_botao_lancamento,
    placeholder_text = "Ex: 26/03/2026",
    fg_color = COR_CAMPOS,
    font = FONTE_ENTRY,
    text_color = COR_TEXTO_JANELA,
    height = ALTURA_CAMPOS_LANCAMENTO,
    width = LARGURA_CAMPOS_LANCAMENTO,
    corner_radius = ARREDONDAMENTO)

entry_data.grid (row = 5, column = 3, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y)

entry_data.bind ("<KeyRelease>", aplicar_mascara_data)

titulo_valor = ctk.CTkLabel (janela_botao_lancamento,
    text = "Valor",
    text_color = COR_TEXTO_JANELA,
    font = FONTE_LABEL)

titulo_valor.grid (row = 0, column = 5, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y_TOPO)

entry_valor = ctk.CTkEntry (janela_botao_lancamento,
    placeholder_text = "Ex: R$150,00",
    fg_color = COR_CAMPOS,
    font = FONTE_ENTRY,
    text_color = COR_TEXTO_JANELA,
    height = ALTURA_CAMPOS_LANCAMENTO,
    width = LARGURA_CAMPOS_LANCAMENTO,
    corner_radius = ARREDONDAMENTO)

entry_valor.grid (row = 1, column = 5, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y)

entry_valor.bind ("<KeyRelease>", aplicar_mascara_valor)

botao_lancar_dados = ctk.CTkButton (janela_botao_lancamento,
    text = "Lançar Dados",
    width = LARGURA_CAMPOS_LANCAMENTO,
    height = ALTURA_CAMPOS_LANCAMENTO,
    corner_radius = ARREDONDAMENTO,
    fg_color = COR_BOTAO_LANCAR,
    text_color = COR_TEXTO_LANCAR,
    hover_color = COR_INTERACAO_LANCAR,
    font = FONTE_BOTAO_LANCAR)

botao_lancar_dados.grid (row = 3, column = 5, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y)

botao_limpar_dados = ctk.CTkButton (janela_botao_lancamento,
    text = "Limpar Dados",
    width = LARGURA_CAMPOS_LANCAMENTO,
    height = ALTURA_CAMPOS_LANCAMENTO,
    corner_radius = ARREDONDAMENTO,
    fg_color = COR_BOTAO_LIMPAR,
    text_color = COR_TEXTO_LIMPAR,
    hover_color = COR_INTERACAO_LIMPAR,
    font = FONTE_BOTAO_LIMPAR)

botao_limpar_dados.grid (row = 5, column = 5, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y)

# JANELA RESUMO

janela_botao_resumo = ctk.CTkFrame (janela_botoes,
    fg_color = COR_FUNDO)

label_botao_resumo = ctk.CTkLabel (janela_botao_resumo,
    text = "RESUMO",
    text_color = COR_TEXTO,
    font = ("Roboto", 30, "bold"))

label_botao_resumo.pack (pady = 30)

# JANELA HISTÓRICO

janela_botao_historico = ctk.CTkFrame (janela_botoes,
    fg_color = COR_FUNDO)

label_botao_historico = ctk.CTkLabel (janela_botao_historico,
    text = "HISTORICO",
    text_color = COR_TEXTO,
    font = ("Roboto", 30, "bold"))

label_botao_historico.pack (pady = 30)

## AJUSTE DIMENSÃO JANELA DOS BOTÕES

janela_botao_lancamento.place ( relwidth = 1, relheight = 1)

janela_botao_resumo.place ( relwidth = 1, relheight = 1)

janela_botao_historico.place ( relwidth = 1, relheight = 1)

mostrar_janela_lancamento()
janela_principal.mainloop()