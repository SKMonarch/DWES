from heroe import *
import random

class Tesoro:
    def __init__(self):
        self.beneficios = ["fuerza","defensa","vida"]

    def encontrar_tesoro(self,heroe):
        ataque = 10
        defensa = 10
        beneficio = random.choice(self.beneficios)
        print(f"Héroe ha encontrado un tesoro: {beneficio} ")
        if beneficio == "fuerza":
            heroe.ataque += ataque
            print(f"El ataque de {heroe.nombre} aumenta a {heroe.ataque}")
        elif beneficio == "defensa":
            heroe.defensa += defensa
            print(f"La defensa de {heroe.nombre} aumenta a  {heroe.defensa}")
        elif beneficio == "vida":
            heroe.salud += 20
            if heroe.salud >= heroe.salud_maxima :
                heroe.salud = heroe.salud_maxima
            print(f"La salud de {heroe.nombre} ha sido restaurada a  {heroe.salud}")