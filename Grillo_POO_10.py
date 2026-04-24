import time, random
meta = 100
class Auto:#defino clase Auto, que es el vehiculo que el usuario va a controlar.
    def __init__(self, equipo, velocidad_base,potencia_nitro, simbolo="🚗"):#le doy los parametros
        self.equipo = equipo
        self.simbolo = simbolo#el simbolo es para que sea mas visual y divertido, y se muestra en la pista.
        self.distancia = 0
        self.velocidad = velocidad_base
        self.potencia_nitro = potencia_nitro
        self.energia = 100 #nitro para gestionar


    def avanzar(self):#defino metodo para avanzar, que es la accion mas basica, y se va a usar siempre, incluso cuando se use nitro o se frene, ya que el auto siempre avanza un poco.
        avance = random.randint(5,15) + self.velocidad#el avance depende de la velocidad actual que ha ido acumulando
        self.distancia += avance#aumento la distancia recorrida segun el avance que me dio el random mas mi velocidad actual.
        print(f">>>{self.equipo} avanza {avance}m. Total: {self.distancia}m")
        self.energia = max(0, self.energia - 15)# El avance normal consume un poquito de energía
        time.sleep(1.5)
        
    def acelerar(self):#defino el metodo para acelerar, que es una accion mas arriesgada pero que puede dar una gran ventaja, ya que aumenta la velocidad y el avance, pero consume energia.
        if self.energia >= 20:#si tengo energia para usar el nitro, puedo acelerar
            boost=self.velocidad + self.potencia_nitro
            self.energia -= 20#resto la energia que consume el nitro
            self.distancia += boost# Al acelerar también se mueve un poco mas por el impulso extra.
            print(f">>>{self.equipo} quema NITRO! Velocidad aumenta +{self.potencia_nitro} km/h | Energía restante: {self.energia}% | Avanza {boost}m. Total: {self.distancia}m")
            time.sleep(1)
            
        else:
            print(f"¡{self.equipo} no tiene suficiente energía para acelerar!")
        time.sleep(1)

    def frenar(self):#defino el metodo para frenar, que es una accion de recuperacion, ya que me baja la velocidad pero me recupera energia.
        recuperacion_energia = 30 #la cantidad de energia que recupero al frenar
        self.velocidad = max(0, self.velocidad - 10)#al frenar, mi velocidad baja, pero no puede ser menor a 0.
        self.energia = min(100, self.energia + recuperacion_energia)#al frenar, recupero energia, pero no puedo pasar de 100.
        print(f">>> {self.equipo} frena. Velocidad actual: {self.velocidad}km/h | Energía: {self.energia}%")
        time.sleep(1.5)

    def mostrar_carril(self, objetivo):
        # Dibujamos la pista proporcional a la meta
        espacios = 30 # Tamaño visual de la pista en caracteres
        progreso = int((self.distancia / objetivo) * espacios)#calculo el progreso proporcional a la distancia recorrida respecto a la meta, y lo convierto en un numero de espacios para mostrar en el dibujo.
        progreso = min(progreso, espacios) # Que no se pase del dibujo
        
        pista = "-" * progreso + self.simbolo + " " * (espacios - progreso)
        print(f"{self.equipo:12} [ {pista} ] {self.distancia}m | {self.energia}%")

opciones=[#mis objetos son los posibles autos que el usuario puede elegir.
    Auto("Ferrari", 20, 15, "🏎️"), 
    Auto("Mercedes", 15, 11, "🚗"), 
    Auto("Red Bull", 18, 10, "🚙"), 
    Auto("McLaren", 16, 8,"🚕"),
    Auto("Alpine", 10, 7,"🚓"),
    Auto("Aston Martin", 10, 25,"🚐"),
    Auto("AlphaTauri", 27, 2,"🚚"),
    Auto("Haas", 11, 11,"🚛"),
    Auto("Alfa Romeo", 7, 15,"🚜"),
    Auto("Williams", 5, 18,"🚘")
]

#-----CODIGO PRINCIPAL-----
print("\n==========¡GRAN PREMIO DE MONACO!==========")#textos de contexto.
print("Bienvenido a la pista mas glamorosa del mundo, el principado de Monaco.")
time.sleep(2)
print("En esta carrera, competirás contra 3 rivales en una pista de 100 metros. El primero en cruzar la meta gana.")
print("Cada turno puedes elegir avanzar, usar NITRO para acelerar o frenar para recuperar energía. ¡Buena suerte!")
print("="*60)
time.sleep(2)

print("\nLos equipos en esta parilla son:")
time.sleep(1)
for i, auto in enumerate(opciones): #se enumeran los equipos
    print(f"{i+1}. {auto.simbolo} {auto.equipo:12} | Base: {auto.velocidad} | Nitro: +{auto.potencia_nitro}")
    time.sleep(0.5)

seleccion = int(input("Elige tu equipo (1-10): ")) - 1

jugador = opciones[seleccion]#se guarda el auto elegido por el usuario como jugador, para luego usarlo en la carrera.

rivales = [] #lista donde guardo a los rivales
for i in range(3): #selecciono 3 rivales distintos al jugador
    rival = random.choice(opciones)
    while rival == jugador or rival in rivales: #mientras el rival sea el mismo que el jugador o ya haya sido elegido como rival, se vuelve a elegir otro.
        rival = random.choice(opciones)
    rivales.append(rival)

print(f"Rivales: {rivales[0].equipo} {rivales[0].simbolo}, {rivales[1].equipo} {rivales[1].simbolo}, {rivales[2].equipo} {rivales[2].simbolo}")


time.sleep(3)

print(f"\n¡Has elegido {jugador.equipo}! Los semáforos se apagan en...") #semaforo para darle mas emocion.
for i in range(3, 0, -1):
    print(f"{i}...")
    time.sleep(1)
print("🟢 ¡LARGARON!\n")

jugando = True
while jugando: #mientras el juego siga activo, se muestra el panel de control y se piden las acciones del jugador, y se simulan las acciones de los rivales.
    print("\n" + "—"*70)
    print(f"PANEL {jugador.equipo} | DISTANCIA: {jugador.distancia}/{meta}km | VELOCIDAD: {jugador.velocidad}km/h | ENERGÍA: {jugador.energia}%")
    print("—"*70)
    print("[1] Avanzar(normal)")
    print("[2] NITRO (-20% energía)")
    print("[3] Frenar(+30% energía)|BOXES \n")
    
    opcion = input(">>Selecciona una acción: ")#segun la opcion seleccionada, actuo.
    if opcion == "1":
        jugador.avanzar()
    elif opcion == "2":
        jugador.acelerar()
    elif opcion == "3":
        jugador.frenar()
    else:
        print("\n Pierdes el turno por maniobra inválida.")
        
    
    
    for r in rivales:# Los rivales tienen una especie de IA: si tienen energía, hay 30% de chance de que usen Nitro
        if r.energia >= 25 and random.random() < 0.3:
            r.acelerar()
        else:
            r.avanzar()
    
    competidores = [jugador] + rivales #creo una lista con el jugador y los rivales para mostrar su progreso en la pista.

    # muestro carriles y posiciones
    print(("="*30) + " POSICIONES EN LA PISTA " + "="*30)

    for auto in competidores:
        auto.mostrar_carril(meta)#muetsro el carril de cada auto, con su simbolo y su progreso visual, ademas de su distancia recorrida y energia restante.
    time.sleep(2)


    for auto in competidores:# verifico si alguien llegó a la meta
        if auto.distancia >= meta:
            print("\n" + "="*80)
            if auto == jugador: #sies el jugador le digo que gano, sino le digo que perdio y quien gano.
                print(f" ¡FELICIDADES! {jugador.equipo} ganó la carrera! GANASTE LA CARRERA MAS GLAMOROSA DEL MUNDO!")
            else:
                print(f" {auto.equipo} cruzó la meta primero. ¡Has perdido!")
            print("="*80 + "\n")
            jugando = False
            break
print("\nFin del GP de Monaco.")