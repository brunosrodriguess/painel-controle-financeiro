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

def editar_lancamento(
    id_lancamento_selecionado,
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
    UPDATE lancamentos
    SET
        descricao = ?,
        categoria = ?,
        subcategoria = ?,
        metodo_pagamento = ?,
        conta_bancaria = ?,
        data = ?,
        valor = ?
    WHERE id = ?
    """,
    (
        descricao,
        categoria,
        subcategoria,
        metodo_pagamento,
        conta_bancaria,
        data,
        valor,
        id_lancamento_selecionado
    )
)   
    conexao.commit()
    conexao.close()

def excluir_lancamento(
    id_lancamento_selecionado
):

    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM lancamentos
    WHERE id = ?
    """,
    (
        id_lancamento_selecionado,
    )
)
    conexao.commit()
    conexao.close()

def listar_lancamentos():

    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM lancamentos
""")

    lancamentos = cursor.fetchall()

    conexao.close()

    return lancamentos