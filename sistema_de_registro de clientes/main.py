import pymysql
import os
class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='negocio_de_pulgas'
        )
        
        self.cursor = self.connection.cursor()
        print("connecion realizada exitosamente")
    def select_user(self, id):
        sql = 'SELECT Cedula, nombre, apodo FROM Clientes WHERE id = {}'.format(id)

        try:
            self.cursor.execute(sql)
            Usuarios = self.cursor.fetchone()

            print("id:", Usuarios[0])
            print("nombre:", Usuarios[1])
            print("apellido:", Usuarios[2])
            print("---------------")

        except ValueError:
            pass
    def select_all_Users(self):
        sql = 'SELECT cedula, nombre, apodo, Saldo_a_deber FROM Clientes'
        try:
            self.cursor.execute(sql)
            Usuarios = self.cursor.fetchall()

            for Usuario in Usuarios:
                print("cedula:", Usuario[0])
                print("nombre:", Usuario[1])
                print("apodo:", Usuario[2])
                print("Saldo a deber:", Usuario[3])
                print("-------------------------\n")

        except ValueError:
            pass  
    def Delete_register(self):
        sql = 'TRUNCATE Clientes'
        try:
            self.cursor.execute(sql)
            print("usuarios eliminados correctamente")
        except ValueError:
            pass
    def Update_Empleados(self, cedula, nombre):
        sql = "UPDATE Empleados SET nombre = '{}' WHERE cedula = {}".format(nombre,cedula)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except ValueError:
            pass  
    def Insert_Users(self,nombre, apodo, Cedula):
        sql = "INSERT INTO Clientes(nombre, apodo, Cedula) VALUES('{}', '{}', '{}')".format(nombre, apodo, Cedula)
        
        try:
            self.cursor.execute(sql)
            
        except ValueError:
            pass
    def Insert_Products(self, _key, fabricante, modelo, precio):
        sql = "INSERT INTO productos(_key, fabricante, modelo, precio) VALUES('{}', '{}', '{}', '{}' )".format(_key, fabricante, modelo, precio)
        try:
            self.cursor.execute(sql)
            self.cursor.execute(sql)
        except ValueError:
            pass  
    def Mostrar_Productos(self):
        sql = "SELECT * FROM productos"

        try:
            self.cursor.execute(sql)
            Productos = self.cursor.fetchall()
            for productos in Productos:
                print("_key", productos[0])
                print("fabricante:", productos[1])
                print("modelo:", productos[2])
                print("precio:", productos[3])
                print("-------------------------\n")
        except ValueError:
            pass 
    def Insertar_Empleados(self, cedula, nombre, apellido, rango, fecha_de_nacimiento):
        sql = "INSERT INTO Empleados(cedula, nombre, apellido, rango, fecha_de_nacimiento) VALUES('{}', '{}','{}','{}','{}')".format(cedula,nombre,apellido,rango,fecha_de_nacimiento)
        try:
            self.cursor.execute(sql)
        except ValueError:
            pass
    def close(self):
        self.connection.close()
        print("conexion termida.")

database = Database() 

encargado = str(input("Bienvedido a negocio de pulgas, ¿en que te podemos servir? \n"))

while True:

    if encargado == "M":
        database.select_all_Users()
        encargado = str(input("Bienvedido a negocio de pulgas, ¿en que te podemos servir? \n"))

    elif encargado == "I":
        cliente_o_empleado = str(input("desea introducir un nuevo empleado o Cliente: \n"))
        if cliente_o_empleado == "cliente":

            nombre = str(input("introducir nombre: "))
            apodo = str(input("introducir apodo: "))
            cedula = int((input("introducir su cedula: ")))

            database.Insert_Users(nombre,apodo,cedula)
            encargado = str(input("Bienvedido a negocio de pulgas, ¿en que te podemos servir? \n"))

        elif cliente_o_empleado == "empleado":
            cedula = int(input("introducir cedula: "))
            nombre = str(input("introducir nombre: "))
            apellido = str(input("introducir apellido: "))
            rango = str(input("introducir el rango: "))
            fecha_de_nacimiento = str(input("introducir fecha de nacimiento: "))

            database.Insertar_Empleados(cedula,nombre,apellido, rango, fecha_de_nacimiento)

            encargado = str(input("Bienvedido a negocio de pulgas, ¿en que te podemos servir? \n"))
        else:
            print("nesecita ayuda")
            encargado = str(input("Bienvedido a negocio de pulgas, ¿en que te podemos servir? \n"))

    elif encargado == "IP":
        _key = str(input("Introducir la key: "))
        fabricante = str(input("Introducir la marca: "))
        modelo = str(input("Introducir el modelo: "))
        precio = str(input("Introducir el precio: "))

        database.Insert_Products(_key,fabricante,modelo, precio)
        encargado = str(input("Bienvedido a negocio de pulgas, ¿en que te podemos servir? \n"))

    elif encargado == "P":
        database.Mostrar_Productos()
        encargado = str(input("Bienvedido a negocio de pulgas, ¿en que te podemos servir? \n"))

    elif encargado == "exit":
        os.close(exit())
        database.close()