class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#Modificar los valores
Persona.nombre = "Juan" # Esto es asignación de valores al azar
Persona.edad = 28

#Acceder a los valores
print(Persona.nombre)  #Imprimir los valores
print(Persona.edad)

#Creación de un objeto
persona = Persona("Karla", 30)
print(persona.nombre)                                # <<-- Creacion del primer objetos -->>
print(persona.edad)
print(id(persona))
    
#Creación de un segundo objeto
persona2 = Persona("Carlos", 40)
print(persona2.nombre)
print(persona2.edad)                            # <<-- Creacion del segundo objetos -->>
print(id(persona2))
