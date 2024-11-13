from heroe import Heroe
from monstruo import Monstruo


heroe = Heroe(nombre="Ares", ataque=25, defensa=10, salud=100, salud_maxima=100)
monstruo = Monstruo(nombre="Troll", ataque=20, defensa=5, salud=80, salud_maxima=80)


print(f"Estado inicial: {heroe.nombre} - Salud: {heroe.salud} | {monstruo.nombre} - Salud: {monstruo.salud}")


heroe.atacar(monstruo)

monstruo.atacar(heroe)


heroe.curarse()


monstruo.atacar(heroe)


heroe.defenderse()


monstruo.atacar(heroe)


heroe.reset_defensa()


if not heroe.esta_vivo():
    print(f"{heroe.nombre} ha muerto.")
else:
    print(f"{heroe.nombre} sigue vivo.")

if not monstruo.esta_vivo():
    print(f"{monstruo.nombre} ha muerto.")
else:
    print(f"{monstruo.nombre} sigue vivo.")
