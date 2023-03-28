import psycopg2

# En esta clase se guardara el nombre del medicamento en la base de datos
class Medicamento:
    def __init__(self, medicamento):
        self._medicamento = medicamento
        print(self._medicamento)
        """ self.conexion = psycopg2.connect(
            user = 'postgres', 
            password = '18228871', 
            host = '127.0.0.1', 
            database = 'Personas')

        self.cursor = self.conexion.cursor()
        self.cursor.execute(f"INSERT INTO MEDICAMENTO VALUE {self._medicamento}")
        """
    def __str__(self):
        return "El registro se realizado correctamente"

class Paciente:
    def __init__(self, nombre, edad, padecimiento, NoSS, User, password):
        self._nombre = nombre
        self._edad = edad
        self._padecimiento = padecimiento
        self._SeguroSocial = NoSS
        self._usuario = User
        self.password = password
    
    def __str__(self):
        return "El registro se realizado correctamente"