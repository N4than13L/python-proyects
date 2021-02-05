import pymysql
import os
import crypt

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db=''
        )
        
        self.cursor = self.connection.cursor()
        print("connecion realizada exitosamente")