class Club():
    dic_clubes = dict()
    
    def __init__(self, nombre, id, liga, presupuesto = 100000, valor_del_club = 0, lista_jugadores = []):
        self.nombre = nombre
        self.id = id
        self.liga = liga
        self.presupuesto = presupuesto
        self.valor_del_club = valor_del_club
        self.lista_jugadores = lista_jugadores
    
    def comprar_jugador(self, club_vendedor, jugador):
        """
        Compra un jugador de otro club, siempre y cuando el club comprador tenga suficiente presupuesto.
        Actualiza los atributos correspondientes de los clubes involucrados y del jugador.
        Parámetros:
            club_vendedor (Club): Club del cual se compra el jugador.
            jugador (Jugador): Jugador a comprar.
        Retorna:
            None
        """
        if jugador.valor <= self.presupuesto:
            club_vendedor.lista_jugadores.remove(jugador)
            club_vendedor.presupuesto += jugador.valor
            club_vendedor.valor_del_club -= jugador.valor
            self.lista_jugadores.append(jugador)
            jugador.club = self.nombre
            self.presupuesto -= jugador.valor
            self.valor_del_club += jugador.valor
            print("Jugador comprado correctamente.")
        else:
            print("No hay presupuesto suficiente para comprar ese jugador.")

    def modificar_presupuesto(self, monto):
        """
        Modifica el presupuesto del club sumando el monto especificado.
        Parámetros:
            monto (int): Monto a sumar al presupuesto del club.
        Retorna:
            None
        """
        self.presupuesto += monto
        print("El nuevo presupuesto del club es", self.presupuesto)
    
    def buscar_arquero_valla_invicta(self):
        """
        Busca y registra que un arquero del club haya mantenido su valla invicta en un partido.
        Retorna:
        arquero (Jugador): Objeto Jugador del arquero que ha mantenido su valla invicta.
        """
        for i in range(len(self.lista_jugadores)):
            if self.lista_jugadores[i].posicion == "Arquero":
                print(self.lista_jugadores[i].dni, self.lista_jugadores[i].nombre, self.lista_jugadores[i].apellido)
        esta_a = "No"
        while esta_a == "No":   
            arquero= int(input("Ingrese el dni del arquero que no recibió goles: "))
            for i in range(len(self.lista_jugadores)):
                if arquero == self.lista_jugadores[i].dni:
                    arquero = self.lista_jugadores[i]
                    arquero.tener_valla_invicta()
                    esta_a = "Sí"
            if esta_a == "No":
                print("El jugador ingresado no existe.")
        return arquero

    def buscar_arquero_recibio_gol(self):
        """
        Busca y registra que un arquero del club haya recibido un gol en un partido.
        Retorna:
        arquero (Jugador): Objeto Jugador del arquero que ha recibido un gol.
        """
        for i in range(len(self.lista_jugadores)):
            if self.lista_jugadores[i].posicion == "Arquero":
                print(self.lista_jugadores[i].dni, self.lista_jugadores[i].nombre, self.lista_jugadores[i].apellido)
        esta_a="No"
        while esta_a == "No":   
            arquero = int(input("Ingrese el dni del arquero al que le metieron gol: "))
            for i in range(len(self.lista_jugadores)):
                if arquero == self.lista_jugadores[i].dni:
                    arquero = self.lista_jugadores[i]
                    arquero.recibir_gol()
                    esta_a = "Sí"
            if esta_a == "No":
                print("El jugador ingresado no existe.")
        return arquero

    def buscar_goleador(self):
        """
        Busca y registra que un jugador del club ha metido un gol en un partido.
        Retorna:
        goleador (Jugador): Objeto Jugador del jugador que ha metido un gol.
        """
        for i in range(len(self.lista_jugadores)):
            print(self.lista_jugadores[i].dni, self.lista_jugadores[i].nombre, self.lista_jugadores[i].apellido)
        esta_g = "No"
        while esta_g == "No":
            goleador = int(input("Ingrese el dni del jugador que metió gol: "))
            for i in range(len(self.lista_jugadores)):
                if goleador == self.lista_jugadores[i].dni:
                    goleador = self.lista_jugadores[i]
                    goleador.hacer_gol()
                    esta_g = "Sí"
            if esta_g == "No":
                print("El jugador ingresado no existe.")
        return goleador
    
    def buscar_asistidor(self):
        """
        Busca y registra que un jugador del club ha dado una asistencia en un partido.
        Retorna:
            asistidor (Jugador): Objeto Jugador del jugador que ha dado la asistencia.
        """
        for i in range(len(self.lista_jugadores)):
            print(self.lista_jugadores[i].dni, self.lista_jugadores[i].nombre, self.lista_jugadores[i].apellido)
        esta_as = "No"
        while esta_as == "No":
            asistidor = int(input("Ingrese el dni del jugador que dió la asistencia: "))
            for i in range(len(self.lista_jugadores)):
                if asistidor == self.lista_jugadores[i].dni:
                    asistidor = self.lista_jugadores[i]
                    asistidor.dar_asistencia()
                    esta_as = "Sí"
            if esta_as == "No":
                print("El jugador ingresado no existe.")
        return asistidor

    def buscar_jugador_tarjeta(self):
        """
        Busca y registra que a un jugador del club se le ha sacado una tarjeta en un partido.
        Returns:
            jugador (Jugador): Objeto Jugador del jugador al que se le ha sacado la tarjeta. 
        """
        for i in range(len(self.lista_jugadores)):
            print(self.lista_jugadores[i].dni, self.lista_jugadores[i].nombre, self.lista_jugadores[i].apellido)
        esta_j = "No"
        while esta_j == "No":
            jugador = int(input("Ingrese el dni del jugador al que le sacaron alguna tarjeta: "))
            for i in range(len(self.lista_jugadores)):
                if jugador == self.lista_jugadores[i].dni:
                    jugador = self.lista_jugadores[i]
                    jugador.cantidad_tarjetas += 1
                    esta_j = "Sí"
            if esta_j == "No":
                print("El jugador ingresado no existe.")
        return jugador

    def __str__(self):
        return("El nombre del club es {}, cuyo ID es {}. El nombre de la liga a la que pertenece es {}, tiene {} de presupuesto y {} de valor. La lista de los jugadores que tiene el club es {}").format(self.nombre, self.id, self.liga, self.presupuesto, self.valor_del_club, self.lista_jugadores)