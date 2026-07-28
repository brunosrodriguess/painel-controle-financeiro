import customtkinter as ctk
from tkinter import messagebox, ttk
import banco_dados
from datetime import datetime

# CONFIGURAÇÕES

ctk.set_appearance_mode ("system")
ctk.set_default_color_theme ("blue")

# FUNÇÕES DE INTERFACE PARA BANCO DE DADOS

def salvar_lancamento():
    descricao = entry_descricao.get()
    categoria = combobox_categoria.get()
    subcategoria = combobox_subcategoria.get()
    metodo_pagamento = combobox_metodo_pagamento.get()
    conta_bancaria = combobox_conta_bancaria.get()
    data = entry_data.get()
    valor = entry_valor.get()

    banco_dados.adicionar_lancamento(
        descricao,
        categoria,
        subcategoria,
        metodo_pagamento,
        conta_bancaria,
        data,
        valor
    )

## CAIXA DE MENSAGEM SUCESSO

    messagebox.showinfo (
        "Sucesso",
        "Lançamento salvo com sucesso!"
    )

    limpar_campos()

    atualizar_historico()

## LIMPAR CAMPOS

def limpar_campos():
    entry_descricao.delete(0, "end")
    combobox_categoria.set(TEXTO_PADRAO_CATEGORIA)
    combobox_subcategoria.set(TEXTO_PADRAO_SUBCATEGORIA)
    combobox_metodo_pagamento.set(TEXTO_PADRAO_METODO_PAGAMENTO)
    combobox_conta_bancaria.set(TEXTO_PADRAO_CONTA_BANCARIA)
    entry_data.delete(0, "end")
    entry_valor.delete(0, "end")

## ATUALIZAR HISTÓRICO

def atualizar_historico():
    for item in historico.get_children():
        historico.delete(item)

    lancamentos = banco_dados.listar_lancamentos()

    for lancamento in lancamentos:
        historico.insert("", "end", iid = lancamento[0], values = lancamento[1:])

## FUNÇÃO SELCIONAR NO HISTÓRICO

def selecionar_lancamento(event):
    global id_lancamento_selecionado
    item = historico.selection()[0]
    id_lancamento_selecionado = item
    valores = historico.item(item)["values"]

    entry_descricao.delete(0, "end")
    entry_descricao.insert(0, valores[0])
    combobox_categoria.set(valores[1])
    combobox_subcategoria.set(valores[2])
    combobox_metodo_pagamento.set(valores[3])
    combobox_conta_bancaria.set(valores[4])
    entry_data.delete(0, "end")
    entry_data.insert(0, valores[5])
    entry_valor.delete(0, "end")
    entry_valor.insert(0, valores[6])

    entrar_modo_edicao()

# FUNÇÃO ENTRAR MODO EDIÇÃO

def entrar_modo_edicao():
    botao_lancar_dados.configure(
        text = "Salvar Alterações",
        command = editar_lancamento)
    botao_limpar_dados.configure(
        text = "Excluir Lançamento",
        command = excluir_lancamento)
    
    botao_cancelar_edicao.grid()

## FUNÇÃO EDITAR LANÇAMENTO

def editar_lancamento():
    descricao = entry_descricao.get()
    categoria = combobox_categoria.get()
    subcategoria = combobox_subcategoria.get()
    metodo_pagamento = combobox_metodo_pagamento.get()
    conta_bancaria = combobox_conta_bancaria.get()
    data = entry_data.get()
    valor = entry_valor.get()

    banco_dados.editar_lancamento(
        id_lancamento_selecionado,
        descricao,
        categoria,
        subcategoria,
        metodo_pagamento,
        conta_bancaria,
        data,
        valor
    )

    atualizar_historico()

    limpar_campos()

    sair_modo_edicao()

## FUNÇÃO EXCLUIR LANÇAMENTO

def excluir_lancamento():
    banco_dados.excluir_lancamento(
        id_lancamento_selecionado,
    )

    atualizar_historico()

    limpar_campos()

    sair_modo_edicao()

# FUNÇÃO SAIR MODO EDIÇÃO

def sair_modo_edicao():
    botao_lancar_dados.configure(
        text = "Lançar Dados",
        command = salvar_lancamento)
    botao_limpar_dados.configure(
        text = "Limpar Dados",
        command = limpar_campos)
    
    global id_lancamento_selecionado
    id_lancamento_selecionado = None

    botao_cancelar_edicao.grid_remove()

# FUNÇÃO CANCELAR DO MODO DE EDIÇÃO

def cancelar_edicao():
    limpar_campos()
    sair_modo_edicao()

# FUNÇÃO BOTÕES FRAME SUPERIOR

def mostrar_janela_lancamento():
    janela_botao_lancamento.tkraise()

def mostrar_janela_graficos():
    janela_botao_graficos.tkraise()

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
    apenas_numeros = ""
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

# FUNÇÃO ABRIR CALENDÁRIO JANELA GRÁFICOS

def abrir_calendario(entry):
    global toplevel_calendario

    if toplevel_calendario is not None:
        toplevel_calendario.destroy()

    toplevel_calendario = ctk.CTkToplevel()
    toplevel_calendario.geometry ("280x240")
    toplevel_calendario.resizable (False, False)
    toplevel_calendario.title ("Calendário")

    hoje = datetime.today()
    mes_atual = hoje.month
    ano_atual = hoje.year
    nome_mes = MESES[mes_atual - 1]

    frame_cabecalho_calendario = ctk.CTkFrame (toplevel_calendario,
        width = 280,
        height = 40,
        fg_color = "#577B54")

    frame_cabecalho_calendario.pack (fill = "x")

    frame_cabecalho_calendario.pack_propagate (False)

    botao_cabecalho_retornar = ctk.CTkButton (frame_cabecalho_calendario,
        text = "<",
        text_color = COR_BOTAO_CABECALHO_CALENDARIO,
        width = LARGURA_BOTAO_CALENDARIO_RETORNAR,
        height = ALTURA_BOTAO_CALENDARIO_RETORNAR,
        hover = False,
        fg_color = "transparent")

    botao_cabecalho_retornar.pack (side = "left", padx = (50,20))

    label_cabecalho = ctk.CTkLabel (frame_cabecalho_calendario,
        text = f"{nome_mes} {ano_atual}",
        text_color = "#000000",
        font = ("Roboto", 12, "bold"))

    label_cabecalho.pack (side = "left")

    botao_cabecalho_avancar = ctk.CTkButton (frame_cabecalho_calendario,
            text = ">",
            text_color = COR_BOTAO_CABECALHO_CALENDARIO,
            width = LARGURA_BOTAO_CALENDARIO_RETORNAR,
            height = ALTURA_BOTAO_CALENDARIO_RETORNAR,
            hover = False,
            fg_color = "transparent")
    
    botao_cabecalho_avancar.pack (side = "left", padx = (20,50))

    frame_calendario = ctk.CTkFrame (toplevel_calendario,
        width = 280,
        height = 160,
        fg_color = COR_FUNDO)

    frame_calendario.pack (fill = "both", expand = True)

    frame_calendario.pack_propagate (False)

    frame_rodape_calendario = ctk.CTkFrame (toplevel_calendario,
        width = 280,
        height = 40,
        fg_color = "#577B54")

    frame_rodape_calendario.pack (fill = "x")

    frame_rodape_calendario.pack_propagate (False)

# PALETA DE CORES

COR_FUNDO = "#D2D2D2"
COR_TITULO =  "#FFFFFF"
COR_MENU = "#577B54"
COR_TEXTO =  "#000000"
COR_TEXTO_LANCAR = "#FFFFFF"
COR_TEXTO_LIMPAR = "#FFFFFF"
COR_TEXTO_CANCELAR = "#FFFFFF"
COR_TEXTO_JANELA = "#000000"
COR_CAMPOS = "#E8E8E8"
COR_BOTAO_CANCELAR =  "#A12626"
COR_BOTAO_LANCAR = "#3A7B34"
COR_BOTAO_LIMPAR = "#616774"
COR_BOTAO_CABECALHO_CALENDARIO = "#000000"
COR_INTERACAO_LANCAR = "#30672A"
COR_INTERACAO_LIMPAR = "#393D44"
COR_INTERACAO_CANCELAR =  "#611111"

# CONSTANTES DE INTERFACE

LARGURA_CAMPOS_LANCAMENTO = 280
ALTURA_CAMPOS_LANCAMENTO = 46
LARGURA_ENTRY_FILTRO = 100
ALTURA_ENTRY_FILTRO = 30
LARGURA_BOTAO_CALENDARIO_FILTRO = 50
ALTURA_BOTAO_CALENDARIO_FILTRO = 10
LARGURA_BOTAO_CALENDARIO_RETORNAR = 25
ALTURA_BOTAO_CALENDARIO_RETORNAR = 10
LARGURA_BOTAO_CALENDARIO_AVANCAR = 25
ALTURA_BOTAO_CALENDARIO_AVANCAR = 10
MARGEM_Y_TOPO = (50,11)
MARGEM_Y =  11
MARGEM_X = 87
FONTE = "Roboto"
FONTE_LABEL = ("Roboto", 24, "normal")
FONTE_ENTRY = ("Roboto", 17, "normal")
FONTE_LABEL_FILTRO = ("Roboto", 15, "bold")
FONTE_ENTRY_FILTRO = ("Roboto", 15, "normal")
FONTE_COMBOBOX = ("Roboto", 15, "normal")
FONTE_BOTAO_LANCAR = ("Roboto", 17, "bold")
FONTE_BOTAO_LIMPAR = ("Roboto", 17, "bold")
FONTE_BOTAO_CANCELAR = ("Roboto", 17, "bold")
ALINHAMENTO = "w"
ARREDONDAMENTO_CAMPOS_LANCAMENTOS = 15
ARREDONDAMENTO_CAMPOS_FILTRO = 8

## CONSTANTES LISTA SUSPENSA JANELA LANCAMENTO

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

## CONSTANTES JANELA GRÁFICOS

MESES = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
]

## VÁRIAVEIS DE ESTADO

id_lancamento_selecionado = None
toplevel_calendario = None

# JANELA PRINCIPAL

janela_principal = ctk.CTk()
janela_principal.title ("Painel de Controle Financeiro")
janela_principal.geometry ("1300x700")
janela_principal.resizable (False, False)
janela_principal.configure (fg_color = COR_FUNDO)

# FRAME SUPERIOR

frame_superior = ctk.CTkFrame (janela_principal,
    width = 1300,
    height = 110,
    fg_color = COR_MENU)

frame_superior.pack (fill = "x", side = "top")

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

## BOTÃO GRÁFICOS

botao_graficos = ctk.CTkButton (frame_superior,
    text = "Gráficos",
    width = 156,
    height = 51,
    corner_radius = 15,
    fg_color = COR_FUNDO,
    text_color = COR_TEXTO,
    hover_color = COR_TITULO,
    command = mostrar_janela_graficos,
    font = ("Roboto", 18, "normal"))

botao_graficos.pack (side = "right", padx = 20)

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
    corner_radius = ARREDONDAMENTO_CAMPOS_LANCAMENTOS)

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
    corner_radius = ARREDONDAMENTO_CAMPOS_LANCAMENTOS,
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
    corner_radius = ARREDONDAMENTO_CAMPOS_LANCAMENTOS,
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
    corner_radius = ARREDONDAMENTO_CAMPOS_LANCAMENTOS,
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
    corner_radius = ARREDONDAMENTO_CAMPOS_LANCAMENTOS,
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
    corner_radius = ARREDONDAMENTO_CAMPOS_LANCAMENTOS)

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
    corner_radius = ARREDONDAMENTO_CAMPOS_LANCAMENTOS)

entry_valor.grid (row = 1, column = 5, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y)

entry_valor.bind ("<KeyRelease>", aplicar_mascara_valor)

botao_lancar_dados = ctk.CTkButton (janela_botao_lancamento,
    text = "Lançar Dados",
    width = LARGURA_CAMPOS_LANCAMENTO,
    height = ALTURA_CAMPOS_LANCAMENTO,
    corner_radius = ARREDONDAMENTO_CAMPOS_LANCAMENTOS,
    fg_color = COR_BOTAO_LANCAR,
    text_color = COR_TEXTO_LANCAR,
    hover_color = COR_INTERACAO_LANCAR,
    font = FONTE_BOTAO_LANCAR,
    command = salvar_lancamento)

botao_lancar_dados.grid (row = 3, column = 5, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y)

botao_limpar_dados = ctk.CTkButton (janela_botao_lancamento,
    text = "Limpar Dados",
    width = LARGURA_CAMPOS_LANCAMENTO,
    height = ALTURA_CAMPOS_LANCAMENTO,
    corner_radius = ARREDONDAMENTO_CAMPOS_LANCAMENTOS,
    fg_color = COR_BOTAO_LIMPAR,
    text_color = COR_TEXTO_LIMPAR,
    hover_color = COR_INTERACAO_LIMPAR,
    command= limpar_campos,
    font = FONTE_BOTAO_LIMPAR)

botao_limpar_dados.grid (row = 5, column = 5, sticky = ALINHAMENTO, padx = MARGEM_X, pady = MARGEM_Y)

## JANELA LANCAMENTO MODO EDIÇÃO

botao_cancelar_edicao = ctk.CTkButton (janela_botao_lancamento,
    text = "Cancelar",
    width = 180,
    height = 46,
    corner_radius = ARREDONDAMENTO_CAMPOS_LANCAMENTOS,
    fg_color = COR_BOTAO_CANCELAR,
    text_color = COR_TEXTO_CANCELAR,
    hover_color = COR_INTERACAO_CANCELAR,
    command = cancelar_edicao,
    font = FONTE_BOTAO_CANCELAR)

botao_cancelar_edicao.grid (row = 6, column = 5, sticky = "e", padx = MARGEM_X, pady = MARGEM_Y_TOPO)

botao_cancelar_edicao.grid_remove()

# JANELA GRÁFICOS

janela_botao_graficos = ctk.CTkFrame (janela_botoes,
    fg_color = COR_FUNDO)


## FILTROS

frame_filtros = ctk.CTkFrame (janela_botao_graficos,
    width = 1300,
    height = 60,
    fg_color = COR_FUNDO)

frame_filtros.grid (row = 0, column = 0, sticky = "n")

frame_filtros.grid_propagate(False)

label_data_inicio = ctk.CTkLabel (frame_filtros,
    text = "Data inicial:",
    font = FONTE_LABEL_FILTRO,
    text_color = COR_TEXTO)

label_data_inicio.grid (row = 0, column = 0, padx = (150,5), pady = 20)

entry_data_inicio = ctk.CTkEntry (frame_filtros,
    fg_color = COR_FUNDO,
    font = FONTE_ENTRY_FILTRO,
    text_color = COR_TEXTO,
    corner_radius = ARREDONDAMENTO_CAMPOS_FILTRO,
    height = ALTURA_ENTRY_FILTRO,
    width = LARGURA_ENTRY_FILTRO,
)

entry_data_inicio.grid (row = 0, column = 1, padx = (5,2), pady = 20)

botao_calendario_inicio = ctk.CTkButton (frame_filtros,
   text = "📆",
   width = ALTURA_BOTAO_CALENDARIO_FILTRO,
   height = LARGURA_BOTAO_CALENDARIO_FILTRO,
   corner_radius = ARREDONDAMENTO_CAMPOS_FILTRO,
   fg_color = "transparent",
   hover = False,
   command = lambda: abrir_calendario(entry_data_inicio)
)

botao_calendario_inicio.grid (row = 0, column = 2, padx = (5,50), pady = 20)

label_data_fim = ctk.CTkLabel (frame_filtros,
    text = "Data final:",
    font = FONTE_LABEL_FILTRO,
    text_color = COR_TEXTO)

label_data_fim.grid (row = 0, column = 3, padx = (40,5), pady = 20)

entry_data_final = ctk.CTkEntry (frame_filtros,
    fg_color = COR_FUNDO,
    font = FONTE_ENTRY_FILTRO,
    text_color = COR_TEXTO,
    height = ALTURA_ENTRY_FILTRO,
    width = LARGURA_ENTRY_FILTRO,
)

entry_data_final.grid (row = 0, column = 4, padx = (5,2), pady = 20)

botao_calendario_final = ctk.CTkButton (frame_filtros,
   text = "📆",
   width = ALTURA_BOTAO_CALENDARIO_FILTRO,
   height = LARGURA_BOTAO_CALENDARIO_FILTRO,
   corner_radius = ARREDONDAMENTO_CAMPOS_FILTRO,
   fg_color = "transparent",
   hover = False,
   command = lambda: abrir_calendario(entry_data_final)
)

botao_calendario_final.grid (row = 0, column = 5, padx = (5,50), pady = 20)

## INDICADORES

## GRÁFICOS


# JANELA HISTÓRICO

janela_botao_historico = ctk.CTkFrame (janela_botoes,
    fg_color = COR_FUNDO)

historico = ttk.Treeview (janela_botao_historico,
    columns = (
        "descricao",
        "categoria",
        "subcategoria",
        "metodo_pagamento",
        "conta_bancaria",
        "data",
        "valor"),
    show = "headings"
)

historico.heading ("descricao", text = "Descrição")
historico.heading ("categoria", text = "Categoria")
historico.heading ("subcategoria", text = "Subcategoria")
historico.heading ("metodo_pagamento", text = "Método de Pagamento")
historico.heading ("conta_bancaria", text = "Conta Bancária")
historico.heading ("data", text = "Data")
historico.heading ("valor", text = "Valor")

historico.column ("descricao", width = 150, anchor = "w")
historico.column ("categoria", width = 150, anchor = "w")
historico.column ("subcategoria", width = 150, anchor = "w")
historico.column ("metodo_pagamento", width = 150, anchor = "w")
historico.column ("conta_bancaria", width = 100, anchor = "w")
historico.column ("valor", width = 100, anchor = "w")
historico.column ("data", width = 100, anchor = "w")

scroll_historico = ttk.Scrollbar (janela_botao_historico, orient = "vertical")

scroll_historico.pack (side = "right", fill = "y")

historico.pack (fill = "both", expand = True, padx = 10, pady = 10)

scroll_historico.configure (command = historico.yview)

historico.configure (yscrollcommand = scroll_historico.set)

historico.bind ("<<TreeviewSelect>>", selecionar_lancamento)

## AJUSTE DIMENSÃO JANELA DOS BOTÕES

janela_botao_lancamento.place ( relwidth = 1, relheight = 1)

janela_botao_graficos.place ( relwidth = 1, relheight = 1)

janela_botao_historico.place ( relwidth = 1, relheight = 1)

banco_dados.criar_banco()
mostrar_janela_lancamento()
atualizar_historico()
janela_principal.mainloop()