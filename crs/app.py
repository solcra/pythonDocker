print("¡Hola desde Docker en el directorio crs! 🚀")
print("Carlos")

class Personaje:
    nombre = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(self.nombre, ": ", sep="")
        print("- Furza: ", self.fuerza)
        print("- Inteligencia: ", self.inteligencia)
        print("- Degensa: ", self.defensa)
        print("- Vida: ", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    
    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, " ha muerto")



my_personaje = Personaje("Carlos", 10, 1, 5, 100)

print(my_personaje)
print("El nombre del jugador es", my_personaje.nombre)
print("La fuerza", my_personaje.fuerza)
print("La inteligencia", my_personaje.inteligencia)
print("La defensa", my_personaje.defensa)
print("Vida", my_personaje.vida)

my_personaje.atributos()
my_personaje.subir_nivel(1,2,3)
my_personaje.atributos()
print (my_personaje.esta_vivo())
my_personaje.morir()
print (my_personaje.esta_vivo())