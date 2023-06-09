class Usuario():

    dic_usuarios = dict()
    lista_mail = []

    def __init__(self, nom_usuario, contra, nombre, apellido, dni, mail): 
        self.nom_usuario = nom_usuario
        self.contra = contra
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.mail = mail

    def __str__(self):
        return("Mi nombre de usuario es {}.Me llamo {} {}, mi DNI es {}, mi mail es {} y mi contraseña es {}.".format(self.nom_usuario,self.apellido,self.nombre,self.dni,self.mail,self.contra))

    def cambiar_contra(self,nueva):
        """
        Cambia la contraseña del usuario.
        Recibe como parámetro la nueva contraseña y la asigna al atributo 'contra' del objeto Usuario.
        Parámetros:
            nueva (str): Nueva contraseña del usuario.
        """
        self.contra = nueva
        print("Se cambió exitosamente la contraseña.")