class Persona():

    lista_personas = []
    lista_dni_personas = []

    def __init__(self, nombre, apellido, dni, edad, nacionalidad, estatura, peso):  
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.estatura = estatura
        self.peso = peso