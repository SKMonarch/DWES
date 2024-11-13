from heroe import Heroe
from monstruo import Monstruo
from tesoro import Tesoro


class Mazmorra:
    def __init__(self,heroe):
        self.heroe = heroe  
        self.monstruos = [
              Monstruo("Goblin",15,5,75),
              Monstruo("Slime",5,10,50),
              Monstruo("Orco",20,15,150),
              Monstruo("Lich",10,5,250),
              Monstruo("Dragon Menor",20,30,100),
              Monstruo("Hidra",30,25,500)
        ]
        self.tesoro = Tesoro()

    def jugar(self):
        print("--------------------------")
        print(f"{self.heroe.nombre} entra en la mazmorra")
        print("--------------------------")
        for monstruo in self.monstruos:
            print(f"Te has encontrado con un {monstruo.nombre}")
            self.enfrentar_enemigo(monstruo)
            if not self.heroe.esta_vivo():
                print("El héroe ha diso derrotado en la mazmorra")
                return
            self.buscar_tesoro()

        print(f"¡{self.heroe.nombre} ha derrotado a todos los monstruos y ha conquistado la mazmorra!")


    def enfrentar_enemigo(self,enemigo):
          while self.heroe.esta_vivo() and enemigo.esta_vivo():
                print("==========================")
                print("   1.Atacar              ")
                print("   2.Defenderse           ")
                print("   3.Curarse              ")
                accion=int(input(print("¿Qué deseas hacer?        ")))
                print("==========================")
                if accion == 1:
                    self.heroe.atacar(enemigo)
                elif accion == 2:
                    self.heroe.defenderse()
                elif accion == 3:
                    self.heroe.curarse()
                else:
                    print("Opción no válida.")
                    continue

                if enemigo.esta_vivo():
                    enemigo.atacar(self.heroe)

                if self.heroe.usando_defensa:
                    self.heroe.reset_defensa()

    def buscar_tesoro(self):
        print("==========================")
        print("    Buscando tesoro...    ")
        print("==========================")
        self.tesoro.encontrar_tesoro(self.heroe)