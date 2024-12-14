nombre1= input("Cómo se llama el jugador 1? ")
nombre2=input("Cómo se llama el jugador 2? ")

jugador1= (input("Hola "+nombre1+". Qué elegís? Piedra, papel o tijera?: ")).lower()
jugador2= (input("Hola "+nombre2+". Jugador 2! Qué elegís? Piedra, papel o tijera?: ")).lower()

if jugador1 == jugador2:
    print("Ha sido un empate!")

elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1== "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
    print("Ha ganando",nombre1)
else:
    print("Ha ganado",nombre2)