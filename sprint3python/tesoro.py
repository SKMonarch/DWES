from heroe import *
import random

class Tesoro:
    def __init__(self):
        self.beneficios = ["fuerza","defensa","vida"]
        self.aumento_ataque = 10
        self.aumento_defensa= 10
    def encontrar_tesoro(self,heroe):
    
        beneficio = random.choice(self.beneficios)
        print(f"Héroe ha encontrado un tesoro: {beneficio} ")
        if beneficio == "fuerza":
            heroe.ataque += self.aumento_ataque
            print(f"El ataque de {heroe.nombre} aumenta a {heroe.ataque}")
        elif beneficio == "defensa":
            heroe.defensa += self.aumento_defensa
            print(f"La defensa de {heroe.nombre} aumenta a  {heroe.defensa}")
        elif beneficio == "vida":
            heroe.salud = heroe.salud_maxima
            print(f"La salud de {heroe.nombre} ha sido restaurada a  {heroe.salud}")