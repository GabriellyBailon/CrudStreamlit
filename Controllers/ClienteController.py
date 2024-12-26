import services.database as db

def IncluirCliente(cliente):
        db.cursor.execute("""
        INSERT INTO Cliente (Nome, Idade, Profissao)
        VALUES (?,?,?)""",
        cliente.nome, cliente.idade, cliente.profissao).rowcount
        db.conn.commit()
        

def ObterCliente():
    db.cursor.execute("""
    SELECT * FROM Cliente """)