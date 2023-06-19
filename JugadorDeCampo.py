from Jugador import Jugador

class JugadorDeCampo(Jugador):

    dic_jugadorescampo = dict()

    def __init__(self, nombre, apellido, dni, edad, nacionalidad, estatura, peso, valor, club, estado, cantidad_tarjetas, posicion, goles, asistencias):
        Jugador.__init__(self, nombre, apellido, dni, edad, nacionalidad, estatura, peso, valor, club, estado, cantidad_tarjetas, posicion)
        self.goles = goles
        self.asistencias = asistencias

    def hacer_gol(self):
        """
        Registra un gol realizado por el jugador.
        Aumenta en 1 el contador de goles del jugador.
        """
        self.goles += 1
        
    def dar_asistencia(self):
        """
        Registra una asistencia realizada por el jugador.
        Aumenta en 1 el contador de asistencias del jugador.
        """
        self.asistencias += 1
    
    def __str__(self):
        return("El nombre del jugador es {} {}, cuyo DNI es {}, tiene {} años, y cuya nacionalidad es {}. Su estatura es {} metros, su peso es {} kg. Su valor es {}, pertenece al club {}. Su estado actual es {}, hizo {} goles, y tiene {} asistencias. ").format(self.nombre, self.apellido, self.dni, self.edad, self.nacionalidad, self.estatura, self.peso, self.valor, self.club, self.estado, self.goles, self.asistencias)