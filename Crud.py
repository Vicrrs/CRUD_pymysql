import pymysql.cursors
import pymysql

conexao = pymysql.Connect(
    host='127.0.0.1',
    user='root',
    password='',
    charset='utf8mb4',
    db='clientes',
    cursorclass=pymysql.cursors.DictCursor
)

with conexao.cursor() as cursor:
    cursor.execute('SELECT * FROM clientes')
    resultado = cursor.fetchall()

    print(resultado)

conexao.close()
