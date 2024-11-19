import random


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 100
        self.nivel = 1
        self.experiencia = 0
        #estos son atributos que no hace falta que el jugador nos pase, arranca con estos datos



#definimos el primer metodo, importamos random
    def atacar(self):
        return random.randint(10, 20) * self.nivel #definimos rango entre 10 y 20 * self.niven(mientras el nivel sea mas alto mas dano vamos a hacer)
    
#definimo el segundo metodo
    def recibir_dano(self, dano):
        self.salud -= dano
        if (self.salud) <= 0:
            print(f"{self.nombre} ha muerto. ¡Game Over!")
        else:
            print(f"Te quedan {self.salud} puntos de salud")

#definimos el tercer metodo
    def ganar_experiencia(self, experiencia):
        print(f"{self.nombre} ha ganado {experiencia} puntos de experiencia")
        self.experiencia += experiencia
        if self.experiencia >= 100:
            self.nivel += 1  #si la exp es mayor a 100 subo de nivel +1
            self.experiencia = 0 # y la exp la volvemo a pasar a cero
            print(f"{self.nombre} ha sabido de nivel a {self.nivel}")
            
    