def sumar(numero1, numero2):
    print(f"La suma de {numero1} y {numero2} es : {numero1+numero2}.")



def restar(numero1, numero2):
    print(f"La resta de {numero1} y {numero2} es : {numero1 - numero2}.")


def multiplicacion(numero1, numero2):
    print(f"La multiplicacion de{ numero1} y {numero2} es : {numero1 * numero2}.")


def division(numero1, numero2):

    if numero2 == 0:
        print("No es posible dividir entre 0")
    else :
        print(f"La division de{ numero1} y {numero2} es : {numero1 / numero2}.")
 



sumar(2,3)
restar(4,8)
multiplicacion(5,3)
division(4,0)
division(4,2)
division(4,8)