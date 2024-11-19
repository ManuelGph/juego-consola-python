 
import random


class Enemigo:
    def __init__(self, nombre, salud, dano):
        self.nombre = nombre
        self.salud = salud
        self.dano = dano

    def atacar(self):
        return random.randint(5,15)  #menor dano que el jugador
    
    def recibir_dano(self, dano):
        self.salud -= dano
        if self.salud <= 0:
            print(f"¡Has derrotado a {self.nombre}!")
            return True
        return False  #aca no hace falta poner un else, xq el retun corta la accion
    