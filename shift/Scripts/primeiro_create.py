import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='root',
                                         password='Shift2022')

    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("A tabela LAPTOP foi criada com sucesso ")

except mysql.connector.Error as error:
    print("Falha ao criar tabela no MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("A conexão com o MySQL foi encerrada.")