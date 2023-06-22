class Club():
    dic_clubes = dict()
    
    def __init__(self, nombre, id, liga, presupuesto = 100000, valor_del_club = 0):
        self.nombre = nombre
        self.id = id
        self.liga = liga
        self.presupuesto = presupuesto
        self.valor_del_club = valor_del_club
        self.dic_jugadores = dict()
    
    def agregar_jugador(self, jugador):
        self.dic_jugadores[jugador.dni] = jugador

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
            club_vendedor.dic_jugadores.pop(jugador.dni)
            club_vendedor.presupuesto += jugador.valor
            club_vendedor.valor_del_club -= jugador.valor
            self.dic_jugadores[jugador.dni] = jugador
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
        for key in self.dic_jugadores.keys():
            if self.dic_jugadores.get(key).posicion == "Arquero":
                print(key, "--->" , self.dic_jugadores.get(key).nombre, self.dic_jugadores.get(key).apellido)
        esta_a = "No"
        while esta_a == "No":   
            try:
                dni= int(input("Ingrese el dni del arquero que no recibió goles: "))
                for key in self.dic_jugadores.keys():
                    if dni == key:
                        arquero = self.dic_jugadores.get(dni)
                        arquero.tener_valla_invicta()
                        esta_a = "Sí"
                if esta_a == "No":
                    print("El jugador ingresado no existe.")
            except:
                print("Ingreso erroneamente el dato.")
        return arquero

    def buscar_arquero_recibio_gol(self):
        """
        Busca y registra que un arquero del club haya recibido un gol en un partido.
        Retorna:
        arquero (Jugador): Objeto Jugador del arquero que ha recibido un gol.
        """
        for key in self.dic_jugadores.keys():
            if self.dic_jugadores.get(key).posicion == "Arquero":
                print(key, "--->" , self.dic_jugadores.get(key).nombre, self.dic_jugadores.get(key).apellido)
        esta_a="No"
        while esta_a == "No":  
            try: 
                dni= int(input("Ingrese el dni del arquero que recibió goles: "))
                for key in self.dic_jugadores.keys():
                    if dni == key:
                        arquero = self.dic_jugadores.get(dni)
                        arquero.recibir_gol()
                        esta_a = "Sí"
                if esta_a == "No":
                    print("El jugador ingresado no existe.")
            except:
                print("Ingreso erroneamente el dato.")
        return arquero

    def buscar_goleador(self):
        """
        Busca y registra que un jugador del club ha metido un gol en un partido.
        Retorna:
        goleador (Jugador): Objeto Jugador del jugador que ha metido un gol.
        """
        for key in self.dic_jugadores.keys():
            print(key, "--->" , self.dic_jugadores.get(key).nombre, self.dic_jugadores.get(key).apellido)
        esta_g = "No"
        while esta_g == "No":
            try:
                dni = int(input("Ingrese el dni del jugador que metió gol: "))
                for key in self.dic_jugadores.keys():
                    if dni == key:
                        goleador = self.dic_jugadores.get(dni)
                        goleador.hacer_gol()
                        esta_g = "Sí"
                if esta_g == "No":
                    print("El jugador ingresado no existe.")
            except:
                print("Ingreso erroneamente el dato.")
        return goleador
    
    def buscar_asistidor(self):
        """
        Busca y registra que un jugador del club ha dado una asistencia en un partido.
        Retorna:
            asistidor (Jugador): Objeto Jugador del jugador que ha dado la asistencia.
        """
        for key in self.dic_jugadores.keys():
            print(key, "--->" , self.dic_jugadores.get(key).nombre, self.dic_jugadores.get(key).apellido)
        esta_as = "No"
        while esta_as == "No":
            try:
                dni = int(input("Ingrese el dni del jugador que metió gol: "))
                for key in self.dic_jugadores.keys():
                    if dni == key:
                        asistidor = self.dic_jugadores.get(dni)
                        asistidor.dar_asistencia()
                        esta_as = "Sí"
                if esta_as == "No":
                    print("El jugador ingresado no existe.")
            except:
                print("Ingreso erroneamente el dato.")
        return asistidor

    def buscar_jugador_tarjeta(self):
        """
        Busca y registra que a un jugador del club se le ha sacado una tarjeta en un partido.
        Returns:
            jugador (Jugador): Objeto Jugador del jugador al que se le ha sacado la tarjeta. 
        """
        for key in self.dic_jugadores.keys():
            print(key, "--->" , self.dic_jugadores.get(key).nombre, self.dic_jugadores.get(key).apellido)
        esta_j = "No"
        while esta_j == "No":
            try:
                dni = int(input("Ingrese el dni del jugador que metió gol: "))
                for key in self.dic_jugadores.keys():
                    if dni == key:
                        jugador = self.dic_jugadores.get(dni)
                        jugador.cantidad_tarjetas += 1
                        esta_j = "Sí"
                if esta_j == "No":
                    print("El jugador ingresado no existe.")
            except:
                print("Ingreso erroneamente el dato.")
        return jugador

    def __str__(self):
        return("El nombre del club es {}, cuyo ID es {}. El nombre de la liga a la que pertenece es {}, tiene {} de presupuesto y {} de valor. La lista de los jugadores que tiene el club es {}").format(self.nombre, self.id, self.liga, self.presupuesto, self.valor_del_club, self.dic_jugadores)