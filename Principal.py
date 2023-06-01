from ModuloFunciones import *

leer_usuarios()
while(menu_usuario != 4):
    entrar = "no"
    while entrar == "no":
        guardar = menu_usuario()
        if guardar in [1,2,3,4]:
            entrar = "si"

    if guardar == 1:
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

    elif guardar == 2:
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
        while (nom_usuario in Usuario.lista_nom_usuarios) or (nom_usuario == ""):
            nom_usuario = input("Ese nombre es inválido. Ingrese un nombre de usuario: ")
        Usuario.lista_nom_usuarios.append(nom_usuario)
        contrasena = input("Ingrese una contraseña: ")
        while len(contrasena) <= 0: 
            contrasena = input("No es una contraseña válida. Ingrese una contraseña: ")
        usuario = Usuario(nom_usuario, contrasena, nombre, apellido, dni, mail)
        Usuario.dic_usuarios[nom_usuario] = usuario
        guardar_usuario()
    
    elif guardar == 3 :
        if len(Usuario.dic_usuarios) == 0:
            print("No hay ningun usuario registrado. Para cambiar una contraseña, debe haber algún usuario registrado.")
        else:
            esta = "No"
            while esta == "No":
                nom_usuario = input("Ingrese su nombre de usuario: ")
                if Usuario.dic_usuarios.get(nom_usuario)!= None:
                    esta = "Si"
                    contrasena = input("Primero ingrese su contraseña vieja: ")
                    while contrasena != Usuario.dic_usuarios.get(nom_usuario).contra:
                        contrasena = input("La contraseña es incorrecta. Intente nuevamente: ")
                    contra_nueva = input("Ingrese su nueva contraseña: ")
                    Usuario.dic_usuarios.get(nom_usuario).cambiar_contra(contra_nueva)
                    guardar_usuario()
                    esta = "Sí"
                if esta == "No":
                    print("El nombre de usuario no existe.")
                        



                # nom_usuario = input("Ingrese su nombre de usuario: ")
                # for i in range(len(Usuario.lista_usuarios)):
                #     if nom_usuario == Usuario.lista_usuarios[i].nom_usuario:
                #         contrasena = input("Primero ingrese su contraseña vieja: ")
                #         try:
                #             if contrasena != Usuario.lista_usuarios[i].contra:
                #                 raise ValueError
                #             contra_nueva = input("Ingrese su nueva contraseña: ")
                #             Usuario.lista_usuarios[i].cambiar_contra(contra_nueva)
                #             guardar_usuario()
                #             esta = "Sí"
                #         except:
                #             print("La contraseña es incorrecta.")
                # if esta == "No":
                #     print("El nombre de usuario no existe.")

    elif guardar < 1 or guardar > 4 :
        print("Error al elegir acción. Intente de nuevo: ")

    elif guardar == 4:
        break