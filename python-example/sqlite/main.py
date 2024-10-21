import sqlite3

conexao =  sqlite3.connect('agenda.db')
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS contatos(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL
    );
""")

cursor.execute("""
    INSERT INTO contatos
        (nome, telefone) VALUES
        ("Maicon", 47958965841
    );
    """)

conexao.commit()