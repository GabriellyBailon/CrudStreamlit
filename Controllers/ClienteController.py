import services.database as db
import streamlit as st
from models import ClienteModel as clienteModel

def IncluirCliente(cliente):
        db.cursor.execute("""
        INSERT INTO Cliente (Id, Nome, Idade, Profissao)
        VALUES (?,?,?,?)""",
        cliente.id, cliente.nome, cliente.idade, cliente.profissao).rowcount
        db.conn.commit()
        

def SelecionarTodos():
    db.cursor.execute("""
    SELECT * FROM Cliente """)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(clienteModel.Cliente(row[0], row[1], row[2], row[3]))
        
    return costumerList

def SelecionarPorId(id):
    db.cursor.execute("""
    SELECT * FROM Cliente 
    WHERE ID = ? """, id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(clienteModel.Cliente(row[0], row[1], row[2], row[3]))
        
    return costumerList

def DeletarPorId(id):
    db.cursor.execute("""
    Delete FROM Cliente 
    WHERE ID = ? """, id)

    db.cursor.commit()

def AlterarCliente(cliente):
    query = """
    UPDATE Cliente
    SET Nome = ?, Idade = ?, Profissao = ?
    WHERE Id = ?;
    """

    try:
        # Executar o comando com os parâmetros
        db.cursor.execute(query, (cliente[1], cliente[2], cliente[3], cliente[0]))
        db.conn.commit()
        st.success("Dados atualizados com sucesso! Atualize a página.")
    except Exception as e:
        st.error(f"Erro ao atualizar os dados: {e}")