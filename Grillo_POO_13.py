import random,time

class Jugador():
    def __init__(self,nombre):
        self.nombre=nombre
        self.puntos=0
    
    def dibujar_dado(self, valor):#dibujo por terminal las caras de los dados.
        caras = {
            1: ["|       |", "|   O   |", "|_______|"],
            2: ["| O     |", "|       |", "|_____O_|"],
            3: ["| O     |", "|   O   |", "|_____O_|"],
            4: ["| O   O |", "|       |", "|_O___O_|"],
            5: ["| O   O |", "|   O   |", "|_O___O_|"],
            6: ["| O   O |", "| O   O |", "|_O___O_|"]
        }
        
        print(" _______")
        for linea in caras[valor]:
            print(linea)
    
    def tirar_dado(self):
        return random.randint(1,6)  

#-----CODIGO PRINCIPAL-----
print("¡Bienvenido al Desafío de Dados!")
print("En este juego, cada jugador tirará un dado de 6 caras durante varias rondas. El jugador con más puntos al final gana.")
time.sleep(2)

lista_nombres = ["Alice", "Bob", "Charlie", "Diana", "Juan", "Maria", "Pedro", "Joaco"]
random.shuffle(lista_nombres)#los demas personajes siempres seran aleatorios, por eso mezclo la lista de nombres para que no siempre sean los mismos.


nombre_usuario=input("Ingrese su nombre: ")
jugador1=Jugador(nombre_usuario)
jugador2=Jugador(lista_nombres[0]) #le asigno el primer nombre de la lista al jugador 2
jugador3=Jugador(lista_nombres[1]) #le asigno el segundo nombre de la lista al jugador 3
jugador4=Jugador(lista_nombres[2]) #le asigno el tercer nombre de la lista al jugador 4
participantes=[jugador1, jugador2, jugador3, jugador4]
print(f"{jugador1.nombre} vs {jugador2.nombre} vs {jugador3.nombre} vs {jugador4.nombre}")


rondas=int(input("Ingrese la cantidad de rondas que desea jugar: "))
for i in range(rondas):
    print("\n" + "═"*40)
    print(f"         RONDA {i+1}")
    print("═"*40)

    for j in participantes:
        if j == jugador1:
            input(f"\n>>> {j.nombre}, presiona ENTER para lanzar tus dados...")
        else:
            print(f"\n{j.nombre} está lanzando...")
            time.sleep(1.5)
        
        resultado = j.tirar_dado()
        j.dibujar_dado(resultado)
        j.puntos += resultado
        
        print(f"¡{j.nombre} obtuvo un {resultado}!")
        print(f"Puntaje total: {j.puntos}")
        time.sleep(1)

print("\n" + "="*30)
print("       RESULTADOS FINALES")
print("="*30)
time.sleep(2)

participantes.sort(key=lambda x: x.puntos, reverse=True)#ordeno la lista de participantes por puntos de mayor a menor para mostrar el ranking final.
#uso lambda para indicar que la clave de ordenamiento es el atributo puntos de cada jugador, y reverse=True para ordenar de mayor a menor.

for pos, j in enumerate(participantes, 1):
    # Agregamos una medalla al primero
    medalla = " 🥇" if pos == 1 else "  "
    print(f"{pos}. {medalla} {j.nombre:<12} | {j.puntos} puntos")

print("\n" + "="*30)
print("       GAME OVER")
print("="*30)