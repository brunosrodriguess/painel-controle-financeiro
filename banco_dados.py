import sqlite3

def adicionar_lancamento(
    descricao,
    categoria,
    subcategoria,
    metodo_pagamento,
    conta_bancaria,
    data,
    valor
):

    conexao = sqlite3.connect("sistema_financas_historico.db")
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