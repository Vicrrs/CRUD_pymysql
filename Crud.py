import pymysql.cursors
import pymysql
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.Connect(
        host='127.0.0.1',
        user='root',
        password='',
        charset='utf8mb4',
        db='clientes',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        print('Conexão fechada')
        conexao.close()

    # Vizualizando as modificações no banco
    # with conecta() as conexao:
    #     with conexao.cursor() as cursor:
    #         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
    #         cursor.execute(sql, ('João', 'Sena', 24, 69))
    #         conexao.commit()


# inserindo vários clientes
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#         dados = [
#             ('Nikola', 'tesla', '29', '70'),
#             ('Isaac', 'Newton', '24', '69'),
#             ('Albert', 'Eisntein', '33', '80')
#         ]
#         # varios valores
#         cursor.executemany(sql, dados)
#         conexao.commit()

# deletando um cliente
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         conexao.commit()

# # deletando vários clientes
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         conexao.commit()

# deletando varios valores /2
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (10, 12))
#         conexao.commit()

# Atualizando alguns valores


# fechando a conexao
with conecta() as conexao:
    # fechando o cursor
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY ID ASC LIMIT 100 ')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
