from Persona import Persona
from Jugador import Jugador
from Arquero import Arquero
from JugadorDeCampo import JugadorDeCampo
from Club import Club
from Liga import Liga
from Usuario import *
import datetime
import math

def validar_longitud_dni(dni):
    """
    Valida la longitud de un número de DNI.
    Solicita al usuario que ingrese un nuevo DNI válido si el número ingresado es menor que 10000000 o mayor que 99999999.
    Devuelve el DNI validado.
    Parámetros:
        dni (int): Número de DNI a validar.
    Retorna:
        int: DNI validado.
    """
    while dni <= 10000000 or dni >= 99999999:
        dni = int(input("Ingrese nuevamente un DNI valido: "))
    return dni

def validar_fecha_nacimiento(fecha_nacimiento):
    """
    Valida si una fecha de nacimiento está en el formato correcto.
    Parámetros:
        fecha_nacimiento (str): La fecha de nacimiento en formato dd/mm/aaaa.
    Retorna:
        str: La fecha de nacimiento válida si cumple con el formato.
    Raises:
        ValueError: Si la fecha de nacimiento no está en el formato correcto.
    """
    try:
        datetime.datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
        return fecha_nacimiento
    except ValueError:
        raise ValueError("La fecha de nacimiento debe estar en formato dd/mm/aaaa")

def calcular_edad(fecha_nacimiento):
    """
    Calcula la edad en años a partir de una fecha de nacimiento.
    Parámetros:
        fecha_nacimiento (str): La fecha de nacimiento en formato dd/mm/aaaa.
    Retorna:
        int: La edad calculada en años.
    Raises:
        ValueError: Si la fecha de nacimiento no está en el formato correcto.
    """
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
    fecha_actual = datetime.date.today()
    diferencia = fecha_actual - fecha_nacimiento
    edad = math.floor(diferencia.days / 365)
    return edad

def validar_estatura(estatura):
    """
    Valida que una estatura esté dentro del rango válido y solicita una nueva entrada en caso contrario.
    Parámetros:
        estatura (float): La estatura en metros a validar.
    Retorna:
        float: La estatura validada dentro del rango permitido.
    """
    while estatura <= 1 or estatura >= 2.5:
        estatura = float(input("Ingrese nuevamente una estatura en metros valida: "))
    return estatura

def validar_peso(peso):
    """
    Valida que un peso esté dentro del rango válido y solicita una nueva entrada en caso contrario.
    Parámetros:
        peso (float): El peso en kilogramos a validar.
    Retorna:
        float: El peso validado dentro del rango permitido.
    """
    while peso <= 30 or peso >= 200:
        peso = float(input("Ingrese el peso nuevamente, en kilogramos. "))
    return peso

def validar_valor(valor):
    """
    Valida que un valor del jugador esté dentro del rango válido y solicita una nueva entrada en caso contrario.
    Parámetros:
        valor (float): El valor del jugador a validar.
    Retorna:
        float: El valor del jugador validado dentro del rango permitido.
    """
    while valor <= 0 or valor >= 2000000:
        valor = float(input("Ingrese nuevamente un valor del jugador válido: "))
    return valor

def validar_estado(estado):
    """
    Valida que un estado físico del jugador esté correctamente ingresado y solicita una nueva entrada en caso contrario.
    Parámetros:
        estado (str): El estado físico del jugador a validar.
    Retorna:
        str: El estado físico del jugador validado correctamente.
    """

    while estado != "Activo" and estado != "activo" and estado != "Lesionado" and estado != "lesionado":
        estado = input("Ingrese nuevamente un estado físico del jugador correctamente: ")
    return estado

def validar_cantidad_tarjetas(cantidad_tarjetas):
    """
    Valida y devuelve la cantidad de tarjetas ingresada por el usuario.
    Solicita al usuario que ingrese un número entero igual o mayor a cero,
    representando la cantidad de tarjetas que le sacaron a un jugador.
    Parámetros:
    - cantidad_tarjetas (int): La cantidad de tarjetas del jugador.
    Retorna:
    - cantidad_tarjetas (int): La cantidad de tarjetas validada por el usuario.
    """
    while cantidad_tarjetas < 0:
        cantidad_tarjetas = int(input("Ingrese 0 o la cantidad de tarjetas que le sacaron al jugador correctamente: "))
    return cantidad_tarjetas

def validar_goles(goles):
    """
    Valida y devuelve la cantidad de goles ingresada por el usuario.
    Solicita al usuario que ingrese un número entero igual o mayor a cero,
    representando la cantidad de goles marcados por un jugador.
    Parámetros:
    - goles (int): La cantidad de goles del jugador.
    Retorna:
    - goles (int): La cantidad de goles validada por el usuario.
    """
    while goles < 0:
        goles = int(input("Ingrese nuevamente una cantidad de goles válida: "))
    return goles

def validar_asistencia(asistencia):
    """
    Valida y devuelve la cantidad de asistencias ingresada por el usuario.
    Solicita al usuario que ingrese un número entero igual o mayor a cero,
    representando la cantidad de asistencias realizadas por un jugador.
    Parámetros:
    - asistencia (int): La cantidad de asistencias del jugador.
    Retorna:
    - asistencia (int): La cantidad de asistencias validada por el usuario.
    """
    while asistencia < 0:
        asistencia = int(input("Ingrese nuevamente una cantidad de asistencias válida: "))
    return asistencia

def validar_vallas_invictas(vallas_invictas):
    """
    Valida y devuelve el número de vallas invictas ingresado por el usuario.
    Solicita al usuario que ingrese un número entero igual o mayor a cero,
    representando la cantidad de vallas invictas logradas por un arquero.
    Parámetros:
    - vallas_invictas (int): El número de vallas invictas del arquero.
    Retorna:
    - vallas_invictas (int): El número de vallas invictas validado por el usuario.
    """
    while vallas_invictas < 0:
        vallas_invictas = int(input("Ingrese un numero válido de vallas invictas: "))
    return vallas_invictas

def validar_goles_recibidos(goles_recibidos):
    """
    Valida y devuelve la cantidad de goles recibidos ingresada por el usuario.
    Solicita al usuario que ingrese un número entero igual o mayor a cero,
    representando la cantidad de goles recibidos por un arquero.
    Parámetros:
    - goles_recibidos (int): La cantidad de goles recibidos por el arquero.
    Retorna:
    - goles_recibidos (int): La cantidad de goles recibidos validada por el usuario.
    """
    while goles_recibidos < 0:
        goles_recibidos = int(input("Ingrese una cantidad válida de goles recibidos: "))
    return goles_recibidos
    
def validar_presupuesto(presupuesto):
    """
    Valida y devuelve el monto de presupuesto ingresado por el usuario.
    Solicita al usuario que ingrese un número entero igual o mayor a cero,
    representando el monto de presupuesto del club.
    Parámetros:
    - presupuesto (int): El monto de presupuesto.
    Retorna:
    - presupuesto (int): El monto de presupuesto validado por el usuario.
    """
    while presupuesto < 0:
        presupuesto = int(input("Ingrese un monto de presupuesto válido: "))
    return presupuesto

def validar_valor_club(valor_del_club):
    """
    Valida y devuelve el valor del club ingresado por el usuario.
    Solicita al usuario que ingrese un número decimal igual o mayor a cero,
    representando el valor del club.
    Parámetros:
    - valor_del_club (float): El valor del club.
    Retorna:
    - valor_del_club (float): El valor del club validado por el usuario.
    """
    while valor_del_club < 0:
        valor_del_club = float(input("Ingrese un valor de club válido: "))
    return valor_del_club

def elegir_liga():
    """
    Permite al usuario elegir una liga de fútbol disponible.
    Muestra una lista de las ligas disponibles junto con sus respectivos países.
    Solicita al usuario que elija el país de la liga deseada y valida su selección.
    La función retorna la instancia de la clase Liga correspondiente a la liga seleccionada.
    Retorna:
    - liga (Liga): Instancia de la clase Liga correspondiente a la liga seleccionada por el usuario.
    """
    for key in Liga.dic_ligas.keys():
        print(key,"--->",Liga.dic_ligas.get(key).nombre)
    liga_pais = str(input("Elija el pais de la liga de las que están disponibles: "))
    while liga_pais not in Liga.dic_ligas.keys():
        liga_pais = str(input("Esa liga no existe. Elija la liga de las que están disponibles: "))
    liga = Liga.dic_ligas.get(liga_pais)
    return liga
    
def elegir_club(liga):
    """
    Permite al usuario elegir un club de fútbol de una liga específica.
    Muestra una lista de los clubes disponibles en la liga proporcionada.
    Solicita al usuario que ingrese el ID del club deseado y valida su selección.
    La función retorna la instancia de la clase Club correspondiente al club seleccionado.
    Parámetros:
    - liga (Liga): Instancia de la clase Liga que representa la liga en la que se elige el club.
    Retorna:
    - club (Club): Instancia de la clase Club correspondiente al club seleccionado por el usuario.
    """
    for i in range(len(liga.lista_clubes)):
        print(liga.lista_clubes[i].id, liga.lista_clubes[i].nombre)
    esta = "No"
    while esta == "No":
        idclub = int(input("Ingrese el id del club de los que están disponibles: "))
        for i in range(len(liga.lista_clubes)):
            if idclub == liga.lista_clubes[i].id:
                esta = "Sí"
    for i in range(len(liga.lista_clubes)):
        if idclub == liga.lista_clubes[i].id:
            club = liga.lista_clubes[i]
    return club

def elegir_jugador(club):
    """
    Permite al usuario elegir un jugador de fútbol de un club específico.
    Muestra una lista de los jugadores disponibles en el club proporcionado.
    Solicita al usuario que ingrese el DNI del jugador deseado y valida su selección.
    La función retorna la instancia de la clase Jugador correspondiente al jugador seleccionado.
    Parámetros:
    - club (Club): Instancia de la clase Club que representa el club en el que se elige el jugador.
    Retorna:
    - jugador (Jugador): Instancia de la clase Jugador correspondiente al jugador seleccionado por el usuario.
    """
    for i in range(len(club.lista_jugadores)):
        print(club.lista_jugadores[i].dni, club.lista_jugadores[i].nombre, club.lista_jugadores[i].apellido)   
    esta = "No"
    while esta == "No":
        dni = int(input("Ingrese el dni del jugador de los que están disponibles: "))
        for i in range(len(club.lista_jugadores)):
            if dni == club.lista_jugadores[i].dni:
                esta = "Sí"
        if dni == club.lista_jugadores[i].dni:
            jugador = club.lista_jugadores[i]
    return jugador

def guardar_usuario():
    """
    Guarda la información de los usuarios en un archivo de texto.
    Abre el archivo 'usuarios.txt' en modo escritura y guarda la información de los usuarios
    almacenada en la lista Usuario.lista_usuarios. Cada usuario se guarda en una línea del archivo,
    con el formato "nom_usuario,contra,nombre,apellido,dni,mail". Finalmente, cierra el archivo.
    """
    with open('./usuarios.txt','w') as archivo_usuarios:
        for key in Usuario.dic_usuarios.items():
            usuario = Usuario.dic_usuarios.get(key)
            archivo_usuarios.write(f"{usuario.nom_usuario},{usuario.contra},{usuario.nombre},{usuario.apellido},{usuario.dni},{usuario.mail}\n")
    archivo_usuarios.close()

def leer_usuarios():
    """
    Lee la información de los usuarios desde un archivo de texto.
    Intenta abrir el archivo 'usuarios.txt' en modo lectura y leer la información de los usuarios.
    Cada línea del archivo se separa por comas y se crea una instancia de la clase Usuario con los datos correspondientes.
    La instancia de Usuario se agrega a las listas Usuario.lista_usuarios, Usuario.lista_nom_usuarios y Usuario.lista_mail.
    Si ocurre una excepción durante el proceso de lectura, no se realiza ninguna acción.
    """
    try:
        with open('./usuarios.txt','r') as archivo_usuarios:
            for usuario in archivo_usuarios:
                datos_usuario = usuario.split(",")
                datos_usuario[5] = datos_usuario[5].rstrip("\n")
                obj_usuario = Usuario(datos_usuario[0], datos_usuario[1], datos_usuario[2], datos_usuario[3], datos_usuario[4], datos_usuario[5])
                Usuario.lista_usuarios.append(obj_usuario)
                Usuario.lista_nom_usuarios.append(obj_usuario.nom_usuario)
                Usuario.lista_mail.append(obj_usuario.mail)
        archivo_usuarios.close()
    except:
        print("")

def guardar_archivos():
    """
    Guarda la información de las ligas, clubes, arqueros y jugadores de campo en archivos de texto.
    Abre los archivos 'ligas.txt', 'clubes.txt', 'arqueros.txt' y 'jugadorescampo.txt' en modo escritura.
    Escribe la información correspondiente de cada entidad en los respectivos archivos.
    Finalmente, cierra los archivos.
    """
    with open('./ligas.txt','w') as archivo_ligas:
        with open('./clubes.txt','w') as archivo_clubes:
            with open('./arqueros.txt','w') as archivo_arqueros:
                with open('./jugadorescampo.txt','w') as archivo_jugadorescampo:
                    for key in Liga.dic_ligas.items():
                        liga = Liga.dic_ligas.get(key)
                        archivo_ligas.write(f"{liga.nombre},{liga.pais},{liga.lista_clubes},{liga.cant_clubes}\n")
                    for key in Club.dic_clubes.items():
                        club = Club.dic_clubes.get(key)
                        archivo_clubes.write(f"{club.nombre},{club.id},{club.liga},{club.presupuesto},{club.valor_del_club},{club.lista_jugadores}\n")
                    for key in Arquero.dic_arqueros.items():
                        arquero = Arquero.dic_arqueros.get(key)
                        archivo_arqueros.write(f"{arquero.nombre},{arquero.apellido},{arquero.dni},{arquero.edad},{arquero.nacionalidad},{arquero.estatura},{arquero.peso},{arquero.valor},{arquero.club},{arquero.estado},{arquero.cantidad_tarjetas},{arquero.posicion},{arquero.vallas_invictas},{arquero.goles_recibidos}\n")
                    for key in JugadorDeCampo.dic_jugadorescampo.items():
                        jugadorcampo = JugadorDeCampo.dic_jugadorescampo.get(key)
                        archivo_jugadorescampo.write(f"{jugadorcampo.nombre},{jugadorcampo.apellido},{jugadorcampo.dni},{jugadorcampo.edad},{jugadorcampo.nacionalidad},{jugadorcampo.estatura},{jugadorcampo.peso},{jugadorcampo.valor},{jugadorcampo.club},{jugadorcampo.estado},{jugadorcampo.cantidad_tarjetas},{jugadorcampo.posicion},{jugadorcampo.goles},{jugadorcampo.asistencias}\n")
    archivo_ligas.close()
    archivo_clubes.close()
    archivo_arqueros.close()
    archivo_jugadorescampo.close()

def leer_ligas():
    """
    Lee la información de las ligas desde un archivo de texto.
    Intenta abrir el archivo 'ligas.txt' en modo lectura y lee la información de las ligas.
    Cada línea del archivo se separa por comas y se crea una instancia de la clase Liga con los datos correspondientes.
    La instancia de Liga se agrega a las listas Liga.lista_ligas, Liga.lista_nombre_ligas y Liga.lista_paises_ligas.
    Si ocurre una excepción durante el proceso de lectura, no se realiza ninguna acción.
    """
    try:
        with open('./ligas.txt','r') as archivo_ligas:
            for liga in archivo_ligas:
                datos_liga = liga.split(',')
                datos_liga[3] = datos_liga[3].rstrip("\n")
                obj_liga = Liga(datos_liga[0],datos_liga[1],datos_liga[2],datos_liga[3])
                Liga.dic_ligas[obj_liga.pais] = obj_liga
                Liga.lista_nombre_ligas.append(obj_liga.nombre)
        archivo_ligas.close()
    except:
        print("")
    
def leer_clubes():
    """
    Lee la información de los clubes desde un archivo de texto.
    Intenta abrir el archivo 'clubes.txt' en modo lectura y lee la información de los clubes.
    Cada línea del archivo se separa por comas y se crea una instancia de la clase Club con los datos correspondientes.
    La instancia de Club se agrega a las listas Club.lista_clubes y Club.lista_id_clubes.
    Si ocurre una excepción durante el proceso de lectura, no se realiza ninguna acción.
    """
    try:
        with open('./clubes.txt','r') as archivo_clubes:
            for club in archivo_clubes:
                datos_club = club.split(',')
                datos_club[5] = datos_club[5].rstrip("\n")
                obj_club = Club(datos_club[0],datos_club[1],datos_club[2],datos_club[3],datos_club[4],datos_club[5])
                Club.dic_clubes[obj_club.id] = obj_club
        archivo_clubes.close()
    except:
        print("")

def leer_arqueros():
    """
    Lee la información de los arqueros desde un archivo de texto.
    Intenta abrir el archivo 'arqueros.txt' en modo lectura y lee la información de los arqueros.
    Cada línea del archivo se separa por comas y se crea una instancia de la clase Arquero con los datos correspondientes.
    La instancia de Arquero se agrega a la lista Arquero.lista_arqueros.
    Además, se agrega el DNI del arquero a la lista Persona.lista_dni_personas.
    Si ocurre una excepción durante el proceso de lectura, no se realiza ninguna acción.
    """
    try:
        with open('./arqueros.txt','r') as archivo_arqueros:
            for arquero in archivo_arqueros:
                datos_arquero = arquero.split(',')
                datos_arquero[14] = datos_arquero[14].rstrip("\n")
                obj_arquero = Arquero(datos_arquero[0],datos_arquero[1],datos_arquero[2],datos_arquero[3],datos_arquero[4],datos_arquero[5],datos_arquero[6],datos_arquero[7],datos_arquero[8],datos_arquero[9],datos_arquero[10],datos_arquero[11],datos_arquero[12],datos_arquero[13],datos_arquero[14])
                Arquero.dic_arqueros[obj_arquero.dni] = obj_arquero
                Persona.lista_dni_personas.append(obj_arquero.dni)
        archivo_arqueros.close()
    except:
        print("")

def leer_jugadorescampo():
    """
    Lee la información de los jugadores de campo desde un archivo de texto.
    Intenta abrir el archivo 'jugadorescampo.txt' en modo lectura y lee la información de los jugadores de campo.
    Cada línea del archivo se separa por comas y se crea una instancia de la clase JugadorDeCampo con los datos correspondientes.
    El DNI del jugador de campo se agrega a la lista Persona.lista_dni_personas.
    Si ocurre una excepción durante el proceso de lectura, no se realiza ninguna acción.
    """
    try:
        with open('./jugadorescampo.txt','r') as archivo_jugadorescampo:
            for jugadorcampo in archivo_jugadorescampo:
                dato_jugadorcampo = jugadorcampo.split(',')
                dato_jugadorcampo[14] = dato_jugadorcampo[14].rstrip("\n")
                obj_jugadorcampo = JugadorDeCampo(dato_jugadorcampo[0],dato_jugadorcampo[1],dato_jugadorcampo[2],dato_jugadorcampo[3],dato_jugadorcampo[4],dato_jugadorcampo[5],dato_jugadorcampo[6],dato_jugadorcampo[7],dato_jugadorcampo[8],dato_jugadorcampo[9],dato_jugadorcampo[10],dato_jugadorcampo[11],dato_jugadorcampo[12],dato_jugadorcampo[13],dato_jugadorcampo[14])
                JugadorDeCampo.dic_jugadorescampo[obj_jugadorcampo.dni] = obj_jugadorcampo
                Persona.lista_dni_personas.append(obj_jugadorcampo.dni)
        archivo_jugadorescampo.close()
    except:
        print("")

def menu():
    """
    Muestra un menú de opciones y devuelve la opción elegida por el usuario.
    Solicita al usuario que ingrese un número correspondiente a una opción del menú.
    Las opciones van del 1 al 10 e incluyen acciones como agregar una liga, agregar un club, agregar un jugador,
    modificar un club, modificar un jugador, jugar un partido, visualizar una liga, visualizar un club, visualizar un jugador
    y cerrar sesión (salir).
    El número ingresado por el usuario se devuelve como resultado de la función.
    """

    menu=int(input("""Elija una opción del menú (Ingrese el número):
1- Agregar Liga
2- Agregar Club
3- Agregar Jugador
4- Modificar Club 
5- Modificar Jugador 
6- Jugar partido
7- Visualizar Liga
8- Visualizar Club
9- Visualizar Jugador   
10- Cerrar sesión (Salir)   

"""))
    return menu

def menu_usuario():
    """
    Muestra un menú de opciones para usuarios y devuelve la opción elegida por el usuario.
    Solicita al usuario que ingrese un número correspondiente a una opción del menú.
    Las opciones van del 1 al 4 e incluyen acciones como iniciar sesión, registrarse,
    cambiar contraseña y salir.
    El número ingresado por el usuario se devuelve como resultado de la función.
    Si ocurre un error al leer la opción del menú, se muestra un mensaje de error.
    """
    try:
        menu=int(input("""Elija una opción del menú (Ingrese el número):
    1- Iniciar sesión
    2- Registrarse
    3- Cambiar contraseña
    4- Salir

    """))
        return menu
    except:
        print("Error. Ingrese el numero de la opcion que desea hacer.")

def menu_principal():
    #leer_archivo()
    # leer_ligas()
    # leer_clubes()
    # leer_arqueros()
    # leer_jugadorescampo()
    """
    Muestra un menú principal con diversas opciones y ejecuta las acciones correspondientes
    basadas en las opciones seleccionadas por el usuario.
    Las opciones del menú incluyen acciones como agregar una liga, agregar un club,
    agregar un jugador, comprar jugadores, modificar presupuesto, retirar jugador,
    jugar un partido, mostrar información de ligas, clubes y jugadores, y salir del programa.
    Cada opción ejecuta una serie de pasos para realizar la acción correspondiente.
    """
    while(menu != 10):
        guardo = menu()
        if guardo == 1:
            pais = str(input("Ingrese el país al que pertenece la liga: "))
            while pais in Liga.dic_ligas.keys():
                pais = str(input("Ya existe una liga para ese país, no puede existir más de 1 liga por país. Ingrese otro país: "))
            nombre = str(input("Ingrese el nombre de la liga que desea agregar: "))
            while nombre in Liga.lista_nombre_ligas:   #No puede haber dos ligas con el mismo nombre ni dos ligas por pais
                nombre = str(input("Ya existe una liga con ese nombre. Ingrese otro nombre para la liga: "))
            liga = Liga(nombre,pais)
            Liga.dic_ligas[pais] = liga
            Liga.lista_nombre_ligas.append(liga.nombre)
            guardar_archivos()
        
        elif guardo == 2:
            if len(Liga.dic_ligas) == 0:
                print("No hay ninguna liga creada. Primero vaya a crear una.")
            else:
                nombre = str(input("Ingrese el nombre del club que desea agregar: "))
                id_ok = False
                while id_ok == False:
                    try:
                        id = int(input("Ingrese un ID para el club (nro. o nros. enteros): "))
                        while id in Club.dic_clubes.keys(): 
                            id = int(input("El ID ingresado ya existe para otro club. Ingrese otro ID para el club: "))
                        id_ok = True
                    except: 
                        print("Ingreso erroneamente el id.")
                for key, in Liga.dic_ligas.items():
                    print(key,"--->",Liga.dic_ligas.get(key).nombre)
                liga = str(input("Elija la liga a la que va a agregar el club. Las ligas disponibles son las siguientes: "))
                while liga not in Liga.lista_nombre_ligas:
                    liga = str(input("La liga ingresada no existe. Elija una de la lista que se le presentó: "))
                presu_ok = False
                while presu_ok == False:
                    try:
                        presupuesto = int(input("Ingrese el presupuesto actual del club (ingrese solamente nros. a menos que sea un nro. decimal): "))
                        presupuesto = validar_presupuesto(presupuesto)
                        presu_ok = True
                    except:
                        print("Ingreso erroneamente el presupuesto.")
                club = Club(nombre,id,liga,presupuesto)    
                Club.dic_clubes[id] = club
                for key in Liga.dic_ligas.items():
                    if club.liga == Liga.dic_ligas.get(key).nombre:
                        Liga.dic_ligas.get(key).lista_clubes.append(club)
                        Liga.dic_ligas.get(key).cant_clubes+=1
                guardar_archivos()
        
        elif guardo == 3:
            if len(Club.dic_clubes) == 0:
                print("No hay ningun club creado. Primero vaya a crear uno.")
            else: 
                nombre = str(input("Ingrese el nombre del jugador que desea agregar: "))
                apellido = str(input("Ingrese el apellido del jugador que desea agregar: "))
                dni_ok = False
                while dni_ok == False:
                    try:
                        dni = int(input("Ingrese el DNI del jugador: "))
                        dni = validar_longitud_dni(dni)
                        while dni in Persona.lista_dni_personas: 
                            dni = int(input("El DNI ingresado ya existe para otro jugador. Intente de nuevo: "))
                            dni = validar_longitud_dni(dni)
                        dni_ok = True
                    except:
                        print("Ingreso erroneamente el dni.")
                Persona.lista_dni_personas.append(dni)
                fecha_nacimiento = input("Ingrese la fecha de nacimiento del jugador en formato dd/mm/aaaa: ")
                fecha_nacimiento = validar_fecha_nacimiento(fecha_nacimiento) 
                edad = calcular_edad(fecha_nacimiento)
                nacionalidad = input("Ingrese la nacionalidad del jugador: ")
                valor_ok = False
                while valor_ok == False:
                    try: 
                        estatura = float(input("Ingrese la estatura (en metros) del jugador: "))
                        estatura = validar_estatura(estatura)
                        peso = float(input("Ingrese el peso (en kilogramos) del jugador: "))
                        peso = validar_peso(peso)
                        valor = int(input("Ingrese el valor del jugador: "))
                        valor = validar_valor(valor)
                        valor_ok = True
                    except:
                        print("Ingreso erroneamente el dato.")
                for key in Club.dic_clubes:
                    print(key,"--->",Club.dic_clubes.get(key).nombre)
                idclub_ok = False
                while idclub_ok == False:
                    try:
                        idclub = int(input("Ingrese el ID del club al que desea agregar al jugador. Los clubes con sus respectivos IDs son los siguientes: "))
                        while idclub not in Club.dic_clubes.keys():
                            idclub = int(input("El ID club ingresado no corresponde a ningún club existente. Elija una de las opciones que se le mostraron: "))
                        idclub_ok = True
                    except:
                        print("Ingreso erroneamente el id del club.")
                for key in Club.dic_clubes.items():
                    if idclub == key:
                        club == Club.dic_clubes.get(key).nombre
                estado = input("Ingrese el estado físico del jugador ('Activo' o 'Lesionado'): ")
                estado = validar_estado(estado)
                tarjetas_ok = False
                while tarjetas_ok == False:
                    try:
                        cantidad_tarjetas = int(input("Ingrese la cantidad de tarjetas que recibió el jugador: "))
                        cantidad_tarjetas = validar_cantidad_tarjetas(cantidad_tarjetas)
                        tarjetas_ok = True
                    except:
                        print("Ingreso erroneamente la cantidad de tarjetas.")
                posicion_valida = "no"
                while posicion_valida == "no":
                    try:
                        posicion = int(input("En qué posición juega? Ingrese sólo el nro. correspondiente a la posición (1. Arquero o 2. Jugador de campo): "))
                        while posicion != 1 and posicion != 2:
                            posicion = int(input("Ingresó un nro. que no corresponde a una posición. Intente de nuevo: "))
                        posicion_valida = "si"
                    except:
                        print("Debe ingresar un nro, lea bien lo que le pide.")
                if posicion == 1:
                    posicion = "Arquero"
                    datos_ok = False
                    while datos_ok == False:
                        try:
                            vallas_invictas = int(input("Ingrese la cantidad de vallas invictas que tiene el arquero: "))
                            vallas_invictas = validar_vallas_invictas(vallas_invictas)
                            goles_recibidos = int(input("Ingrese la cantidad de goles que recibio el arquero: "))
                            goles_recibidos = validar_goles_recibidos(goles_recibidos)
                            datos_ok = True
                        except:
                            print("Ingrese erroneamente el dato.")
                    arquero=Arquero(nombre,apellido,dni,edad,nacionalidad,estatura,peso,valor,club,estado,cantidad_tarjetas, posicion, vallas_invictas, goles_recibidos)
                    Arquero.dic_arqueros[dni] = arquero
                    for key in Club.dic_clubes.items():
                        if arquero.club == Club.dic_clubes.get(key).nombre:
                            Club.dic_clubes.get(key).lista_jugadores.append(arquero)
                    guardar_archivos()

                else: 
                    posicion = "Jugador de campo"
                    datos_ok = False
                    while datos_ok == False:
                        try:
                            goles= int(input("Ingrese la cantidad de goles que marcó el jugador: "))
                            goles = validar_goles(goles)
                            asistencias = int(input("Ingrese la cantidad de asistencias que hizo el jugador: "))
                            asistencias = validar_asistencia(asistencias)
                            datos_ok = True
                        except:
                            print("Ingreso erroneamente el dato.")
                    jugador_de_campo = JugadorDeCampo(nombre,apellido,dni,edad,nacionalidad,estatura,peso,valor,club,estado,cantidad_tarjetas, posicion, goles, asistencias)
                    JugadorDeCampo.dic_jugadorescampo[dni] = jugador_de_campo
                    for key in Club.dic_clubes.items():
                        if jugador_de_campo.club == Club.dic_clubes.get(key).nombre:
                            Club.dic_clubes.get(key).lista_jugadores.append(jugador_de_campo)
                    guardar_archivos()
        
        elif guardo == 4:
            if len(Club.dic_clubes) == 0:
                print("No hay ningun club creado. Primero vaya a crear uno.")
            else:
                try:
                    sub_menu = int(input("""Elija la acción que desea:
                    1- Comprar Jugador
                    2- Cambiar Presupuesto"""))
                    while sub_menu != 1 and sub_menu != 2:
                        sub_menu=int(input("""Elija la acción que desea:
                    1- Comprar Jugador
                    2- Cambiar Presupuesto"""))
                except:
                    print("Error. Ingrese el numero de la opcion que desea hacer.")
                if sub_menu == 1: 
                    print("Primero hay que elegir el club que va a comprar.")
                    liga_comprador = elegir_liga()
                    club_comprador = elegir_club(liga_comprador)
                    print("Ahora hay que elegir el jugador a comprar y su club.")
                    liga_vendedor = elegir_liga()
                    club_vendedor = elegir_club(liga_vendedor)
                    jugador = elegir_jugador(club_vendedor)
                    club_comprador.comprar_jugador(club_vendedor,jugador)
                else:
                    liga = elegir_liga()
                    club = elegir_club(liga)
                    monto = int(input("Ingrese el monto que desea agregar o restar al presupuesto (si desea restar, ingrese un '-' antes del número): "))
                    club.modificar_presupuesto(monto)
                guardar_archivos()
        
        elif guardo == 5:
            if len(Persona.lista_dni_personas) == 0:
                print("No hay ningun jugador creado. Primero vaya a crear uno.")
            else:
                print("Primero elija el jugador a modificar.")
                liga = elegir_liga()
                club = elegir_club(liga)
                jugador = elegir_jugador(club)
                try:
                    sub_menu=int(input("""Elija la acción que desea:
                    1- Retirar Jugador
                    2- Cambiar Estado de un Jugador
                    3- Cambiar Valor de un Jugador
                    4- Salir"""))
                    while sub_menu != 1 and sub_menu != 2 and sub_menu!= 3 and sub_menu!= 4:
                        sub_menu=int(input("""Elija la acción que desea:
                    1- Retirar Jugador
                    2- Cambiar Estado de un Jugador
                    3- Cambiar Valor de un Jugador
                    4- Salir"""))
                except:
                    print("Error. Ingrese el numero de la opcion que desea hacer.")
                if sub_menu == 1:
                    jugador.retirar_jugador(club)
                elif sub_menu == 2:
                    jugador.modificar_estado()
                elif sub_menu == 3:
                    jugador.modificar_valor()
                elif sub_menu == 4:
                    break
                guardar_archivos()
       
        elif guardo == 6:
            if len(Liga.dic_ligas) == 0:
                print("No hay ninguna liga creada. Primero vaya a crear una.")
            else:
                liga = elegir_liga()
                if len(liga.lista_clubes) < 2:
                    print("Se necesita al menos 2 clubes en la misma liga para jugar un partido. Vaya a crearlos.")
                else:
                    print("Elija el club local que jugará el partido.")
                    club1 = elegir_club(liga)
                    print("Elija el club visitante que jugará el partido.")
                    club2 = elegir_club(liga)
                    liga.jugar_partido(club1, club2)
                guardar_archivos()

        elif guardo == 7:
            if len(Liga.dic_ligas) == 0:
                print("No hay ninguna liga creada. Primero vaya a crear una.")
            else:
                liga = elegir_liga()
                print(liga)

        elif guardo == 8:
            if len(Club.dic_clubes) == 0:
                print("No hay ningun club creado. Primero vaya a crear uno.")
            else:
                liga = elegir_liga()
                club = elegir_club(liga)
                print(club)

        elif guardo == 9:
            if len(Persona.lista_dni_personas) == 0:
                print("No hay ningun jugador creado. Primero vaya a crear uno.")
            else:
                liga = elegir_liga()
                club = elegir_club(liga)
                jugador = elegir_jugador(club)
                print(jugador)

        elif guardo < 1 or guardo >10 :
            print("Error al elegir acción. Intente de nuevo: ")
        
        elif guardo == 10:
            break

def guardo1():
    """
    Verifica si existen usuarios registrados y solicita al usuario que ingrese su nombre de usuario y contraseña.
    Si las credenciales son válidas, se muestra un mensaje de ingreso exitoso y se llama a la función `menu_principal`.
    Si el nombre de usuario no existe, se muestra un mensaje de error correspondiente.
    """
    if len(Usuario.dic_usuarios) == 0:
        print("No hay ningun usuario registrado. Primero vaya a registrarse.")
    else: 
        esta = "No"
        while esta == "No":
            nom_usuario = input("Ingrese su nombre de usuario: ")
            if Usuario.dic_usuarios.get(nom_usuario)!= None:
                esta = "Si"
                contrasena = input("Ingrese su contraseña: ")
                while contrasena != Usuario.dic_usuarios.get(nom_usuario).contra:
                    contrasena = input("La contraseña es incorrecta. Intente nuevamente: ")
                print("Ingresado correctamente.")
                menu_principal()
            if esta == "No":
                print("El nombre de usuario no existe.")

def guardo2():
    """
    Solicita al usuario que ingrese su información personal, como nombre, apellido, DNI, correo electrónico, nombre de usuario y contraseña.
    Verifica la validez de la información ingresada y crea un nuevo objeto de usuario con los datos proporcionados.
    Finalmente, guarda el nuevo usuario en la base de datos.
    """
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    dni_aprobado = "no"
    while dni_aprobado == "no":
        try:
            dni = int(input("Ingrese su dni: "))
            dni = validar_longitud_dni(dni)
            dni_aprobado = "si"
        except:
            print("El DNI está compuesto de números solamente. Ingreselo bien por favor: ")
    mail = input("Ingrese su mail: ")
    while mail in Usuario.lista_mail:
        mail = input("Ese mail ya tiene un usuario. Ingrese su mail: ")
    Usuario.lista_mail.append(mail)
    nom_usuario = input("Ingrese un nombre de usuario: ")
    while (nom_usuario in Usuario.dic_usuarios.keys()) or (nom_usuario == ""):
        nom_usuario = input("Ese nombre es inválido. Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese una contraseña: ")
    while len(contrasena) <= 0: 
        contrasena = input("No es una contraseña válida. Ingrese una contraseña: ")
    usuario = Usuario(nom_usuario, contrasena, nombre, apellido, dni, mail)
    Usuario.dic_usuarios[nom_usuario] = usuario
    guardar_usuario()

def guardo3():
    """
    Permite al usuario cambiar su contraseña. Verifica si hay usuarios registrados y solicita al usuario que ingrese su nombre de usuario y contraseña actual.
    Si la contraseña ingresada es correcta, se solicita una nueva contraseña y se actualiza en el objeto de usuario correspondiente.
    Finalmente, guarda los cambios en la base de datos.
    """
    if len(Usuario.dic_usuarios) == 0:
        print("No hay ningun usuario registrado. Para cambiar una contraseña, debe haber algún usuario registrado.")
    else:
        esta = "No"
        while esta == "No":
            nom_usuario = input("Ingrese su nombre de usuario: ")
            if Usuario.dic_usuarios.get(nom_usuario)!= None:
                esta = "Si"
                contrasena = input("Primero ingrese su contraseña vieja: ")
                try: 
                    if contrasena != Usuario.dic_usuarios.get(nom_usuario).contra:
                        raise ValueError
                    contra_nueva = input("Ingrese su nueva contraseña: ")
                    Usuario.dic_usuarios.get(nom_usuario).cambiar_contra(contra_nueva)
                    guardar_usuario()
                    esta = "Sí"
                except:
                    print("La contraseña es incorrecta.")
            if esta == "No":
                print("El nombre de usuario no existe.")