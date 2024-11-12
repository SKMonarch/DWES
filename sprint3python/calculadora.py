from operaciones import sumar, restar, multiplicacion, division

REPETIR = "S"
while REPETIR != "N":
    print("=============================")
    print("         Calculadora         ")
    print("=============================")
    print("     Teclea la opción(1-4)   ")
    print("-----------------------------")
    print("         1-Sumar             ")
    print("         2-Restar            ")
    print("         3-Multiplicar       ")
    print("         4-Dividir           ")
    print("=============================")
    
    OPCION = int(input("Operacion ? (1-4): "))
    
    if OPCION not in range(1, 5):
        print("No está en el rango de opciones")
        break
    
    NUM1 = float(input("Introduce el primer número: "))
    NUM2 = float(input("Introduce el segundo número: "))
   
    if OPCION == 1:
        sumar(NUM1, NUM2)
    elif OPCION == 2:
        restar(NUM1, NUM2)
    elif OPCION == 3:
        multiplicacion(NUM1, NUM2)
    elif OPCION == 4:
        division(NUM1, NUM2)
        
    REPETIR = input("¿Quieres realizar otra operación? (S/N): ").upper()
