import sqlite3
try:
  con = sqlite3.connect("meu_banco.db")
  cur= con.cursor()
  #cur.execute("CREATE TABLE pessoa(id,nome,idade,cpf)")
  #cur.execute("INSERT INTO pessoa VALUES(1,'isabella',17,'xxx.xxx.xxx-xx')") 
  res = cur.execute("SELECT * FROM pessoa")
  pessoas = res.fetchone()

  print(pessoas)

  #cur.close()
  #con.commit ()

except ConnectionResetError as c:
 print ('Erro de conexão com o banco.')