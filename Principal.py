from ModuloFunciones import *

leer_usuarios()
while(menu_usuario != 4):
    entrar = "no"
    while entrar == "no":
        guardar = menu_usuario()
        if guardar in [1,2,3,4]:
            entrar = "si"

    if guardar == 1:
        guardo1()

    elif guardar == 2:
        guardo2()
    
    elif guardar == 3 :
        guardo3()           

    elif guardar < 1 or guardar > 4 :
        print("Error al elegir acción. Intente de nuevo: ")

    elif guardar == 4:
        break