# En este programa se hacen todas las modificaciones en la Base de datos Pastillero
import psycopg2

# En esta clase se guardara el nombre del medicamento en la base de datos
class Medicamento:
    def __init__(self, id_medicamento, medicamento):
        self._idMedicamento = id_medicamento
        self._medicamento = medicamento
        try:
            self.conexion = psycopg2.connect(
                user = 'postgres', 
                password = '18228871', 
                host =  '127.0.0.1', 
                database = 'Pastillero')
            print("Conexion exitosa con base de datos pastillero")
        except Exception:
            print(f"Ha ocurrido un error con la conexion a la base de datos")
    
    def registroMedicamento(self):
        try:
            with self.conexion:
                with self.conexion.cursor() as self.cursor:
                    self.consulta = "INSERT INTO \"Medicamentos\"(id_medicamento, nombre_medicamento) VALUES(%s, %s)"
                    self.valores = self._idMedicamento, self._medicamento
                    self.cursor.execute(self.consulta,self.valores)
                    self.regafectados = self.cursor.rowcount
                    return f"Medicamentos agregados {self.regafectados}"      
        except psycopg2.errors.UniqueViolation:
            return "¡El medicamento que ya esta registrado!"
        except Exception:
            return "Ha ocurrido un error, favor de reintentar"
        finally:
           self.cursor.close()

    def medQuery(self):
        try:
            with self.conexion:
                with self.conexion.cursor() as self.cursor:
                    self.consulta = "SELECT * FROM \"Medicamentos\" ORDER BY id_medicamento"
                    self.cursor.execute(self.consulta)
                    self.registros  = self.cursor.fetchall()
                    return self.registros
        
        except:
            print("Ha ocurrido un error en la consulta")

# Clase para registrar al paciente
class Paciente:
    def __init__(self, nombre, enfermedad, edad, NoSS, User, password):
        self._nombre = nombre
        self._enfermedad = enfermedad
        self._edad = edad
        self._SeguroSocial = NoSS
        self._usuario = User
        self._password = password
        try:
            self.conexion = psycopg2.connect(
                user = 'postgres',
                password = '18228871',
                host = "127.0.0.1",
                database = 'Pastillero'
            )
        except:
            print("Conexion incorrecta")
        
    def registroPX(self):
        try:
            with self.conexion:
                with self.conexion.cursor() as self.cursor:
                    self.consulta = "INSERT INTO public.\"DATOS_PX\"(\"NOMBRE\", \"Enfermedad\", \"Edad\", \"NoSS\", \"Usuario\", \"Contra\") VALUES (%s, %s, %s, %s, %s, %s)"
                    self.values  =  (self._nombre, self._enfermedad, self._edad, self._SeguroSocial, self._usuario, self._password)
                    self.cursor.execute(self.consulta,self.values)
                    self.regafectados = self.cursor.rowcount
                    print(f"Pacientes agregados {self.regafectados}")
        except:
            print(f"Ha ocurrido un error con el registro del paciente")
        finally:
            self.cursor.close()

    def consultaPX(self):
        pass       

if __name__ == "__main__":
    a = Paciente('Diana', 'Ninguna', 23, 555, 'ponce', 'carinita')
    a.registroPX()