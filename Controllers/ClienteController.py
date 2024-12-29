import services.database as db
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