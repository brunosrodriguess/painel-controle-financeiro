import sqlite3
import os

CAMINHO_BANCO = os.path.join(
    os.path.dirname(__file__),
    "sistema_financas_historico.db"
)

def criar_banco():

    conexao = sqlite3.connect(CAMINHO_BANCO)
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

def adicionar_lancamento(
    descricao,
    categoria,
    subcategoria,
    metodo_pagamento,
    conta_bancaria,
    data,
    valor
):

    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()
    
    cursor.execute("""
    INSERT INTO lancamentos (    
        descricao,
        categoria,
        subcategoria,
        metodo_pagamento,
        conta_bancaria,
        data,
        valor
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)    
    """,
    (
        descricao,
        categoria,
        subcategoria,
        metodo_pagamento,
        conta_bancaria,
        data,
        valor
    )
)
    conexao.commit()
    conexao.close()