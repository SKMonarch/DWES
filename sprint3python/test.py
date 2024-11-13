from heroe import Heroe
from monstruo import Monstruo
from tesoro import Tesoro

# Crear un héroe, un monstruo y un tesoro
heroe = Heroe(nombre="Ares", ataque=25, defensa=10, salud=100, salud_maxima=100)
monstruo = Monstruo(nombre="Troll", ataque=20, defensa=5, salud=80, salud_maxima=80)
tesoro = Tesoro()

# Mostrar el estado inicial de héroe y monstruo
print(f"Estado inicial: {heroe.nombre} - Salud: {heroe.salud} | {monstruo.nombre} - Salud: {monstruo.salud}")

# Héroe ataca al monstruo
heroe.atacar(monstruo)

# Monstruo ataca al héroe
monstruo.atacar(heroe)

# Héroe se cura y encuentra un tesoro
heroe.curarse()
tesoro.encontrar_tesoro(heroe)

# Monstruo ataca nuevamente
monstruo.atacar(heroe)

# Héroe aumenta su defensa
heroe.defenderse()

# Monstruo ataca después del aumento de defensa
monstruo.atacar(heroe)

# Restablecer la defensa del héroe a la normalidad
heroe.reset_defensa()

# Comprobación de si héroe y monstruo siguen vivos
if not heroe.esta_vivo():
    print(f"{heroe.nombre} ha muerto.")
else:
    print(f"{heroe.nombre} sigue vivo.")

if not monstruo.esta_vivo():
    print(f"{monstruo.nombre} ha muerto.")
else:
    print(f"{monstruo.nombre} sigue vivo.")
