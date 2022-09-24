# importando conecto do MySQL 
import mysql.connector

# Importando separadamente o módulo de erros do conector
from mysql.connector import Error


try:
    # Iniciar conexão com o banco local, utilizando nome da conxão, nome do banco, usuário e senha
    # connection é uma variável que receberá essas credenciais
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='root',
                                         password='Shift2022')
    # utiliza a variável connection criada anteriormente para verificar se a conexão foi estabelecida                                    
    if connection.is_connected():
        # a variável db_info revebe informações sobre a versão do MySQL utilizada
        db_Info = connection.get_server_info()
        # Imprime no console a versão do MySQL
        print("Conectado com sucesso ao MySQL versão ", db_Info)
        # a variável cursor acessa a conexão estabelecida e utiliza um cursor para acessar os comandos do banco
        cursor = connection.cursor()
        # o cursos utilizado seleciona o banco criado
        cursor.execute("select database();")
        record = cursor.fetchone()
        # caso sucesso, será impressa uma mensagem de sucesso, contendo o nome do banco
        print("Você está conectado à database: ", record)

# caso encontre algum erro, o console retornará esse erro, utilizando o módulo Error importado no início
except Error as e:
    print("Erro ao conectar com o MySQL", e)
# o bloc finally é semrpe executado    
finally:
    #caso esteja conectado
    if connection.is_connected():
        #conexão com o cursor encerrada
        cursor.close()
        #conexão com o banco encerrada
        connection.close()
        # confirma no console o encerramento da sessão
        print("A conexão com o MySQL foi encerrada.")