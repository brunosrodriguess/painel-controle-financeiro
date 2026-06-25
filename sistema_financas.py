import customtkinter as ctk
from tkinter import messagebox, ttk

# CONFIGURAÇÕES

ctk.set_appearance_mode ("system")
ctk.set_default_color_theme ("blue")

# PALETA DE CORES

COR_FUNDO = "#D2D2D2"
COR_TITULO =  "#FFFFFF"
COR_MENU = "#577B54"
COR_TEXTO =  "#000000"

# CONTAINER (JANELA) PRINCIPAL

janela = ctk.CTk ()
janela.title ("Painel de Controle Financeiro")
janela.geometry ("1300x700")
janela.resizable (False, False)
janela.configure (fg_color = COR_FUNDO)

# CONTAINER (FRAME) SUPERIOR

frame_superior = ctk.CTkFrame (janela,
    width = 1300,
    height = 110,
    fg_color = COR_MENU)

frame_superior.pack (padx = 0, pady = 0)

frame_superior.pack_propagate(False)

# BOTÕES CONTAINER SUPERIOR

botao_lancamento = ctk.CTkButton (frame_superior,
    text = "Lançamento",
    width = 156,
    height = 51,
    corner_radius = 15,
    fg_color = COR_FUNDO,
    text_color = COR_TEXTO,
    hover_color = COR_TITULO,
    font = ("Roboto", 18, "normal"))

botao_lancamento.pack (side = "right", padx = 20)

botao_resumo = ctk.CTkButton (frame_superior,
    text = "Resumo",
    width = 156,
    height = 51,
    corner_radius = 15,
    fg_color = COR_FUNDO,
    text_color = COR_TEXTO,
    hover_color = COR_TITULO,
    font = ("Roboto", 18, "normal"))

botao_resumo.pack (side = "right", padx = 20)

botao_historico = ctk.CTkButton (frame_superior,
    text = "Histórico",
    width = 156,
    height = 51,
    corner_radius = 15,
    fg_color = COR_FUNDO,
    text_color = COR_TEXTO,
    hover_color = COR_TITULO,
    font = ("Roboto", 18, "normal"))

botao_historico.pack (side = "right", padx = 20)

# TÍTULO (LABEL) CONTAINER SUPERIOR

titulo = ctk.CTkLabel (frame_superior,
    text = "PAINEL DE CONTROLE FINANCEIRO", 
    font = ("Roboto", 30, "bold"),
    text_color = COR_TITULO)

titulo.pack (side = "left", padx = 40)

janela.mainloop()