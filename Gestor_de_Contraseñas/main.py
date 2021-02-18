import pymysql
import os

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='user'
        )
        
        self.cursor = self.connection.cursor()
        print("connecion realizada exitosamente")

    def Mostrar(self):
        sql = "SELECT * FROM user"
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchall()

            print(user[0], user[1])
            print("-----------------\n")

        except ValueError:
            print("error")

    def Insertar_a_tabla(self, nombre, contrasena):
        sql = "INSERT INTO Usuarios(nombre, contrasena) VALUES('{}', '{}')".format(nombre,contrasena)       
        try:
            self.cursor.execute(sql)
        except ValueError:
            print("error")

database = Database()

nombre = str(input())
contrasena = str(input())
database.Mostrar(1)
