import sqlite3
import os

CAMINHO_BANCO = os.path.join(
    os.path.dirname(__file__),
    "sistema_financas_historico.db"
)

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