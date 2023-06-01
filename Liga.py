class Liga():
    lista_ligas = [] #Total de ligas
    lista_nombre_ligas = []
    lista_paises_ligas = [] #Cada país tiene máximo 1 liga (si creo una liga en un pais que ya tiene, no me deja)

    def __init__(self, nombre, pais, lista_clubes = [], cant_clubes = 0 ):
        self.nombre = nombre
        self.pais = pais
        self.lista_clubes = lista_clubes  #Clubes de cada liga
        self.cant_clubes =  cant_clubes


    def jugar_partido(self, club1, club2): #Club1 es local y club2 es vistante
        print("Arrancó el partido!")
        goles = input("Ingrese 's' si HUBO goles y 'n' si NO HUBO goles: ")
        while goles != "s" and goles != "n":
            goles = input("No ingreso una opcion valida. Ingrese 's' si HUBO goles y 'n' si NO HUBO goles: ")
        if goles == "s":
            cant_goles = int(input("Cuántos goles totales hubo en el partido? "))
            while cant_goles <=0:
                cant_goles = int(input("El numero tiene que se mayor a 0. Cuantos goles totales hubo en el partido? "))
            cont = 0
            cont_l = 0
            cont_v = 0
            while cont < cant_goles:
                que_club = input("Qué club hizo gol? Para local ingrese 'l', para visitante ingrese 'v': ")
                while que_club != "l" and que_club != "v":
                    que_club = input("No ingreso una opcion valida. Para local ingrese 'l', para visitante ingrese 'v': ")
                if que_club == "l":
                    club1.buscar_goleador()
                    asistencia = input("El gol tuvo asistencia? Ingrese 's' si el gol TUVO asistencia y 'n' si el gol NO TUVO asistencia: ")
                    while asistencia != "s" and asistencia != "n":
                        asistencia = input("Ingrese una respuesta válida. Ingrese 's' si el gol TUVO asistencia y 'n' si el gol NO TUVO asistencia: ")
                    if asistencia == 's':
                        club1.buscar_asistidor()
                    club2.buscar_arquero_recibio_gol()
                    cont_l += 1
                    cont += 1 
                else: #club visitante
                    club2.buscar_goleador()
                    asistencia = input("El gol tuvo asistencia? Ingrese 's' si el gol TUVO asistencia y 'n' si el gol NO TUVO asistencia:")
                    while asistencia != "s" and asistencia != "n":
                        asistencia = input("Ingrese una respuesta válida. Ingrese 's' si el gol TUVO asistencia y 'n' si el gol NO TUVO asistencia: ")
                    if asistencia == 's':
                        club2.buscar_asistidor()
                    club1.buscar_arquero_recibio_gol()
                    cont_v += 1
                    cont += 1
            if cont_l == 0:
                club2.buscar_arquero_valla_invicta()
            if cont_v == 0:
                club1.buscar_arquero_valla_invicta()
        else:
            club1.buscar_arquero_valla_invicta()
            club2.buscar_arquero_valla_invicta()
        tarjetas = input("Ingrese 's' si HUBO tarjetas y 'n' si NO HUBO tarjetas: ")
        while tarjetas != "s" and tarjetas != "n":
            tarjetas = input("No ingreso una opcion valida. Ingrese 's' si HUBO tarjetas y 'n' si NO HUBO tarjetas: ")
        if tarjetas == "s":
            cant_tarjetas = int(input("Cuántas tarjetas totales hubo en el partido? "))
            while cant_tarjetas <= 0:
                cant_tarjetas = int(input("El numero tiene que se mayor a 0. Cuantas tarjetas totales hubo en el partido? "))
            cont_t = 0
            while cont_t < cant_tarjetas:
                club_amonestado = input("Qué club recibio la tarjeta? Para local ingrese 'l', para visitante ingrese 'v': ")
                while club_amonestado != "l" and club_amonestado != "v":
                    club_amonestado = input("No ingreso una opcion valida. Para local ingrese 'l', para visitante ingrese 'v': ")
                if club_amonestado == "l":
                    club1.buscar_jugador_tarjeta()
                    cont_t += 1
                else:
                    club2.buscar_jugador_tarjeta()
                    cont_t += 1
        print("Partido terminado!")
        
    def __str__(self):
        return("La liga del país '{}' se llama '{}' y está conformada por los siguientes {} clubes: {}").format(self.pais, self.nombre, self.cant_clubes, self.lista_clubes)