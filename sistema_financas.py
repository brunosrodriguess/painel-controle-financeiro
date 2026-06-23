import customtkinter as ctk
from tkinter import messagebox, ttk

# CONFIGURAÇÕES

ctk.set_appearance_mode ("system")
ctk.set_default_color_theme ("blue")

# PALETA DE CORES

COR_FUNDO = "#D2D2D2"
COR_TITULO =  "#238B1C"
COR_MENU = "#B1B1B1"
COR_BORDA =  "#196513"

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

# TÍTULO (LABEL) CONTAINER PRINCIPAL

titulo = ctk.CTkLabel (frame_superior,
    text = "PAINEL DE CONTROLE FINANCEIRO", 
    font = ("Roboto", 30, "bold"),
    text_color = COR_TITULO)

titulo.pack (side = "left", padx = 40)

janela.mainloop()