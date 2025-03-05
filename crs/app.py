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

    def dano(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        dano = self.dano(enemigo)
        enemigo.vida = enemigo.vida - dano
        print(self.nombre, " ha realizado ", dano, " puntos de daño a ", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de ", enemigo.nombre, " es ", enemigo.vida)
        else:
            enemigo.morir()
    
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
    
    def cambio_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8 (2) Matadragones, daño 10 "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecto")

    def atributos(self):
        super().atributos()
        print("- Espada: ", self.espada)
    
    def dano(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa

class Mago(Personaje):
    def __init__(self, nombre, furza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, furza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("- Libro: ", self.libro)

    def dano(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa

def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")

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
my_enemigo = Personaje("Ana", 8,5,3,100)
my_personaje.atacar(my_enemigo)
my_personaje.morir() 
print (my_personaje.esta_vivo())
my_personaje.atributos()

gusts = Guerrero("Gusts", 20,10,10,100,5)
gusts.atributos()
print(gusts.espada)
gusts.cambio_arma()
gusts.atributos()
print(gusts.espada)

print("Juego nuevo")
goku = Personaje("Goku", 20,15,10,100)
gust = Guerrero("Guts", 20,15,10,100,5)
venessa = Mago("Vanessa", 20,15,10,100,5)
print("Atrivutos sin ataque")
goku.atributos()
gust.atributos()
venessa.atributos()


print("Atrivutos con ataque")
goku.atacar(gust)
gust.atacar(venessa)
venessa.atacar(goku)
goku.atributos()
gust.atributos()
venessa.atributos()

print("Combate")
goku1 = Personaje("Goku", 20,15,10,100)
gust1 = Guerrero("Guts", 20,15,10,100,5)
combate(goku1,gust1)