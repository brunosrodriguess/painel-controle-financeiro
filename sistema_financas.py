import customtkinter as ctk
from tkinter import messagebox, ttk

# CONFIGURAÇÕES

ctk.set_appearance_mode ("system")
ctk.set_default_color_theme ("blue")

# PALETA DE CORES

COR_FUNDO = "#B1B1B1"
COR_TITULO =  "#238B1C"

# CONTAINER (JANELA) PRINCIPAL

janela = ctk.CTk ()
janela.title ("Painel de Controle Financeiro")
janela.geometry ("1200x600")
janela.resizable (False, False)
janela.configure (fg_color = COR_FUNDO)

# TÍTULO (LABEL) CONTAINER PRINCIPAL

titulo = ctk.CTkLabel (janela, 
    text = "PAINEL DE CONTROLE FINANCEIRO", 
    font = ("Roboto", 34, "bold"),
    text_color = COR_TITULO)

titulo.pack (pady = (50, 10))

janela.mainloop()