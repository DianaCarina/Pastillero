# En este programa se hacen todas las modificaciones en la Base de datos Pastillero
import psycopg2

# En esta clase se guardara el nombre del medicamento en la base de datos
class CONEXION:
    def __init__(self):        
        try:
            self.conexion = psycopg2.connect(
                user = 'postgres', 
                password = '18228871', 
                host =  '127.0.0.1', 
                database = 'Pastillero')
           # print("Conexion exitosa con base de datos pastillero")
        except Exception:
            print(f"Ha ocurrido un error con la conexion a la base de datos")

class Medicamento(CONEXION):
    def __init__(self, medicamento, id_medicamento = ""):
        super().__init__()
        self._idMedicamento = id_medicamento
        self._medicamento = medicamento
    
    def registroMedicamento(self):
        try:
            with self.conexion:
                with self.conexion.cursor() as self.cursor:
                    self.consulta = "INSERT INTO \"Medicamentos\"(id_medicamento, nombre_medicamento) VALUES(%s, %s)"
                    self.valores = self._idMedicamento, self._medicamento
                    self.cursor.execute(self.consulta, self.valores)
                    self.reg_afectados = self.cursor.rowcount
                    return f"Medicamentos agregados {self.reg_afectados}"      
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
                    self.consulta = f"SELECT * FROM \"Medicamentos\" ORDER BY nombre_medicamento ASC"
                    self.cursor.execute(self.consulta)
                    self.registros  = self.cursor.fetchall()
                    return self.registros        
        except:
            print("Ha ocurrido un error en la consulta de los medicamentos")
        finally:
           self.cursor.close()
    
    def medQuery2(self):
        try:
            with self.conexion:
                with self.conexion.cursor() as self.cursor:
                    self.consulta = f'SELECT id_medicamento FROM \"Medicamentos\" WHERE nombre_medicamento = \'{self._medicamento}\''
                    self.cursor.execute(self.consulta)
                    self.registros  = self.cursor.fetchone()
                    return self.registros[0]        
        except:
            print("Ha ocurrido un error en la consulta del id medicamentos")
        finally:
           self.cursor.close()

# Clase para registrar al paciente
class Paciente(CONEXION):
    def __init__(self, nombre = "val1", enfermedad = "val2", edad = "val3", NoSS = "val4", User = "val5", password = "val6"):
        super().__init__()
        self._nombre = nombre
        self._enfermedad = enfermedad
        self._edad = edad
        self._SeguroSocial = NoSS
        self._usuario = User
        self._password = password
        
    def registroPX(self):
        try:
            with self.conexion:
                with self.conexion.cursor() as self.cursor:
                    self.consulta = "INSERT INTO public.\"DATOS_PX\"(\"NOMBRE\", \"Enfermedad\", \"Edad\", \"NoSS\", \"Usuario\", \"Contra\") VALUES (%s, %s, %s, %s, %s, %s)"
                    self.values  =  (self._nombre, self._enfermedad, self._edad, self._SeguroSocial, self._usuario, self._password)
                    self.cursor.execute(self.consulta, self.values)
                    self.regafectados = self.cursor.rowcount
                    print(f"Pacientes agregados {self.regafectados}")
        except:
            print(f"Ha ocurrido un error con el registro del paciente")
        finally:
            self.cursor.close()

    def consultaIdPX(self):
        try:
            with self.conexion:
                with self.conexion.cursor() as self.cursor:
                    self.consulta = f'SELECT \"ID_PX\" FROM public.\"DATOS_PX\" WHERE \"Usuario\" = \'{self._usuario}\''
                    self.cursor.execute(self.consulta)
                    self.registros  = self.cursor.fetchone()
                    return self.registros 
        except:
            print("Ha ocurrido un error en la consulta del Id del paciente")       
        finally:
            self.cursor.close()   

class Tratamiento(CONEXION):
    def __init__(self, nombre_medicamento, id_usuario):
        super().__init__()
        self._nombre_medicamento = tuple(nombre_medicamento)
        self._numMedicamento = len(nombre_medicamento)
        self._id_usuario = id_usuario
    
        self.values = (self._id_usuario,) + self._nombre_medicamento
        print(self.values)
    def insertTrat(self):
        try:
            with self.conexion:
                with self.conexion.cursor() as self.cursor:
                    self.consulta = "INSERT INTO \"TRATAMIENTO\"(\"ID_PACIENTE\", \"ID_MED_1\", \"ID_MED_2\", \"ID_MED_3\", \"ID_MED_4\", \"ID_MED_5\") VALUES(%s, %s, %s, %s, %s, %s)"
                    self.cursor.execute(self.consulta, self.values)
                    self.registros_afectados = self.cursor.rowcount
                    print(f'Registros afectados {self.registros_afectados}')
        except:
            print("Fallo en la insersion de datos del tratamiento")
if __name__ == "__main__":
    a = Paciente('Diana', 'Ninguna', 23, 555, 'ponce', 'carinita')
    a.registroPX()