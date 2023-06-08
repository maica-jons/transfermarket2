class Jugador():

    lista_dni_jugadores = []

    def __init__(self, nombre, apellido, dni, edad, nacionalidad, estatura, peso, valor, club, estado, cantidad_tarjetas, posicion):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.estatura = estatura
        self.peso = peso
        self.valor = valor
        self.club = club
        self.estado = estado   # (Estado físico)
        self.cantidad_tarjetas = cantidad_tarjetas 
        self.posicion=posicion

    def retirar_jugador(self, club): 
        """
        Retira al jugador del club y establece su estado como "Retirado".
        Parámetros:
            club: El objeto Club del cual se retirará al jugador.
        """
        self.estado = "Retirado"
        self.club = ""
        for i in range(len(club.lista_jugadores)):
            if self.dni == club.lista_jugadores[i].dni:
                club.lista_jugadores.remove(club.lista_jugadores[i])
        print("Jugador retirado.")

    def modificar_valor(self):
        """
        Modifica el valor del jugador según el monto ingresado.
        Solicita al usuario ingresar el monto en el que varió el valor del jugador.
        Si el monto es positivo, aumenta el valor del jugador.
        Si el monto es negativo (precedido por un signo '-'), disminuye el valor del jugador.
        """
        monto = float(input("Ingrese el monto en el que varió el valor del jugador (Si es negativo ponga un '-' antes del número): "))
        self.valor += monto
        print("El nuevo valor del jugador es", self.valor)
        
    def modificar_estado(self): 
        """
        Modifica el estado del jugador.
        Si el estado actual del jugador es 'Activo', cambia su estado a 'Lesionado'.
        Si el estado actual del jugador es 'Lesionado', cambia su estado a 'Activo'.
        """
        if self.estado == "Activo":
            self.estado = "Lesionado"
        else:
            self.estado = "Activo"
        print("El nuevo estado del jugador es", self.estado)