
import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='root',
                                         password='Shift2022')

    mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES 
                           (15, 'Lenovo ThinkPad P71', 6459, '2019-08-14') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Registro inserido com sucesso!")
    cursor.close()

except mysql.connector.Error as error:
    print("Falha ao inserir registro na tabela {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("Conexão com o MySQL foi encerrada.")