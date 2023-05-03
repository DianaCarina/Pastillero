import psycopg2

# En esta clase se guardara el nombre del medicamento en la base de datos
class Medicamento:
    def __init__(self, id_medicamento, medicamento):
        self._idMedicamento = id_medicamento
        self._medicamento = medicamento
        print(self._medicamento)
        try:
            self.conexion = psycopg2.connect(
                user = 'postgres', 
                password = '18228871', 
                host =  '127.0.0.1', 
                database = 'Pastillero')
            print("Conexion exitosa con base de datos pastillero")
        except Exception:
            print(f"Ha ocurrido un error")
    
    def registroMedicamento(self):
        try:
            with self.conexion:
                with self.conexion.cursor() as self.cursor:
                    self.consulta = "INSERT INTO \"Medicamentos\"(id_medicamento, nombre_medicamento) VALUES(%s, %s)"
                    self.valores = self._idMedicamento, self._medicamento
                    self.cursor.execute(self.consulta,self.valores)
                    self.regafectados = self.cursor.rowcount
                    print(f"Registros afectados {self.regafectados}")        
        except:
            print(f"Ha ocurrido un error {e}")
        finally:
            self.cursor.close()

    def __str__(self):
        return "El registro se realizado correctamente"

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
                    print(f"Registros afectados {self.regafectados}")

        except Exception as e:
            print(f"Ha ocurrido un error {e}")

        finally:
            self.cursor.close()       
    
    def __str__(self):
        return "El registro se realizado correctamente"

if __name__ == "__main__":
    a = Paciente('Diana', 'Ninguna', 23, 555, 'ponce', 'carinita')
    a.registroPX()()