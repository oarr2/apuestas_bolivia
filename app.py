import random
saldo = 0
def ganador():
    return random.randint(1,2) 
while True:
    oponentes = ['Uruguay', 'Brazil', 'Argentina']
    index_oponente = random.randint(0, 2)
    print("el siguiente partido sera entre")
    print("Bolvia vs" + oponentes[index_oponente])
    print("la lista de equipos es:")
    print("1. Bolvia")
    print("2. " + oponentes[index_oponente])
    print("introduzca el numero del equipo a apostar")
    n = int(input())
    print("introduzca la cantidad")
    cantidad = int(input())
    winner = ganador()
    if ganador == n:
        saldo = saldo + cantidad*2
        print("Felidades ganaste, tu saldo es ", saldo)
    else:
        saldo = saldo - cantidad
        print("Lo sentimos, perdiste, tu saldo es ", saldo)
    print("quiere continuar? s/n")
    continuar = input()
    if continuar == 'n':
        break
