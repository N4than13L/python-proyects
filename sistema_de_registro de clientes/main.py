import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='prueba'
        )
        self.cursor = self.connection.cursor()
        print("connecion realizada exitosamente")

    def select_user(self, id):
        sql = 'SELECT id, nombre, apellido FROM Usuarios WHERE id = {}'.format(id)

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
        sql = 'SELECT id, nombre, apellido FROM Usuarios'
        try:
            self.cursor.execute(sql)
            Usuarios = self.cursor.fetchall()

            for Usuario in Usuarios:
                print("id:", Usuario[0])
                print("nombre:", Usuario[1])
                print("apellido:", Usuario[2])
                print("___________\n")

        except ValueError:
            pass
    
    def Delete_register(self):
        sql = 'TRUNCATE Usuarios'
        try:
            self.cursor.execute(sql)
            print("usuarios eliminados correctamente")
        except ValueError:
            pass

    def Update_user(self, id, nombre):
        sql = "UPDATE Usuarios SET nombre = '{}' WHERE id = {}".format(nombre,id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except ValueError:
            pass
    
    def Insert_Users(self, id, nombre, apellido):
        sql = "INSERT INTO Usuarios(id, nombre, apellido) VALUES('{}', '{}', '{}')".format(id,nombre,apellido)
        
        try:
            self.cursor.execute(sql)
            
        except ValueError:
            pass


    def close(self):
        self.connection.close()
        print("conexion termida.")

database = Database() 

persona = str(input("¿En que le podemos servir? \n"))

if persona == "M":
    database.select_all_Users()

elif persona == "C":
    Cambio_de_dato = str(input("valor a introducir: "))
    database.Update_user(1, Cambio_de_dato)

elif persona == "P":
    database.select_user(1)

elif persona == "B":
    database.Delete_register()
    
elif persona == "I":
    id = int(input("inserte ID"))
    nombre = str(input("inserte Nombre"))
    apellido = str(input("inserte Apellido"))
    database.Insert_Users(id,nombre, apellido)

    print("usuario agragado con exito", "\n",
    "Id:", id, "\n", "Nombre:", nombre, "\n" "Apellido:", apellido, "\n")
    print("------------------------")
elif persona == "C":
    database.close()

elif persona == "A":
    print("I para insertar, B para borrar, para P mostrar el primer valor, M para mostrar todo")
