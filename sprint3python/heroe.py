from monstruo import *

class Heroe:
    def __init__(self,nombre,ataque,defensa,salud,salud_maxima):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        self.salud_maxima = salud_maxima

    def atacar(self, enemigo):
        daño = self.ataque - enemigo.defensa
        if daño > 0 :
            enemigo.salud -= daño
            print(f"Héroe ataca a {enemigo.nombre}.")
            print(f"El enemigo {enemigo.nombre} ha recibido {daño} puntos de daño.")
        else:
            print(f"El enemigo ha bloqueado el ataque.")

    def curarse(self):
        self.salud += 20
        if self.salud >= self.salud_maxima :
            self.salud = self.salud_maxima
        print(f"Héroe se ha curado. Salud actual: {self.salud}")

    def defenderse(self):
        self.defensa_temporal = 5
        self.defensa = self.defensa + self.defensa_temporal
        print(f"El héroe aumenta temporalmente su defensa en 5 puntos para el siguiente ataque.")

    def reset_defensa(self):
        self.defensa -= self.defensa_temporal
        self.defensa_temporal = 0
        print(f"La defensa de  {self.nombre} vuelve a la normalidad.")

    def esta_vivo(self):
        vivo = True
        if self.salud == 0:
            vivo = False
        return vivo



