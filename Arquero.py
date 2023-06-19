from Jugador import Jugador

class Arquero(Jugador):

    dic_arqueros = dict()

    def __init__(self, nombre, apellido, dni, edad, nacionalidad, estatura, peso, valor, club, estado, cantidad_tarjetas, posicion, vallas_invictas, goles_recibidos):
        Jugador.__init__(self, nombre, apellido, dni, edad, nacionalidad, estatura, peso, valor, club, estado, cantidad_tarjetas, posicion)
        self.vallas_invictas = vallas_invictas
        self.goles_recibidos = goles_recibidos

    def tener_valla_invicta(self):
        """
        Incrementa el contador de vallas invictas del arquero.
        """
        self.vallas_invictas += 1

    def recibir_gol(self):
        """
        Incrementa el contador de goles recibidos del arquero.
        """
        self.goles_recibidos += 1
    
    def __str__(self):
        return("El nombre del jugador es {} {}, cuyo DNI es {}, tiene {} años, y cuya nacionalidad es {}. Su estatura es {} metros, su peso es {} kg. Su valor es {}, pertenece al club {}. Su estado actual es {}, tiene {} vallas invictas, y tiene {} goles recibidos. ").format(self.nombre, self.apellido, self.dni, self.edad, self.nacionalidad, self.estatura, self.peso, self.valor, self.club, self.estado, self.vallas_invictas, self.goles_recibidos)