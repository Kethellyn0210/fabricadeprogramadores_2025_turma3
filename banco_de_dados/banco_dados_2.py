import sqlite3
try:
    con = sqlite3.connect("segundo_banco.db")
    cur = con.cursor()

    cur.execute("DROP TABLE pessoa")

    cur.execute("CREATE TABLE pessoa(id_pessoa  INTEGER PRIMARY KEY ASC AUTOINCREMENT,"+
                "nome VARCHAR(400),"+
                "idade INTEGER,"+
                "cpf VARCHAR(15))")

    cur.execute("CREATE TABLE consulta(id PRIMARY KEY ASC AUTOINCREMENT,"+
                "data_consulta DATETIME,"+
                "horario DATETIME,"+
                "id_pessoa INTEGER"+
                "FOREING KEY (id_pessoa) REFERENCES pessoa(id))")

except ConnectionRefusedError as c:
    print('Erro de Conexão:', c)