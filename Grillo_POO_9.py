import random
import time
class Explorador():# defino mi clase explorador, que es el personaje que el usuario va a controlar.
    def __init__(self):
        self.nombre= input("Ingrese como se desea llamar: ")
        self.monedas=0# cantidad de monedas que va a ir recolectando el jugador a medida que abre los cofres.
        self.cantidad_ganzuas=random.randint(3,5)#le asigno ganzuas entre 3 a 5.
    
    def usar_ganzua(self):
        self.cantidad_ganzuas -= 1 # cada cofre que abro es una ganzua menos
    
class Cofre():#clase donde se definen los cofres que el jugador va a encontrar, con sus atributos y metodos para abrirlos.
    def __init__(self, tipo, min_m, max_m, es_bueno):#recibe el tipo de cofre, el rango de monedas que puede tener y si es bueno o maldito.
        self.tipo = tipo
        self.cantidad_monedas = random.randint(min_m, max_m)# sera un numero aleatorio entre el minimo y maximo que le asigno segun el tipo de cofre.
        self.es_bueno = es_bueno

        if self.es_bueno == False:
            self.estado = "Cerrado"  # Si es maldito, SIEMPRE esta cerrado asi el jugador decide
        else:
            self.estado = random.choice(["Abierto", "Cerrado"])#sino es malo, sera una eleccion random.
    
    def perder_todo(self, explorador):# metodo para perder todo si se cae en la maldicion del cofre trampa.
        print("¡Mmm que cofre mas raro!")
        op=input("El cofre está cerrado.Tiene " + str(explorador.cantidad_ganzuas) + " ganzuas. ¿Desea usar una ganzua para abrirlo? (s/n): ")
        if op.lower() == "s": #fuerzo al usuario a usar la ganzua, asi el decide si se arriesga o no, pero si lo hace, pierde todo.
            explorador.usar_ganzua()
            explorador.monedas =0
            explorador.cantidad_ganzuas=0
            print(f"{explorador.nombre} ha abierto el cofre MALDITO, y pierde todos sus recursos!")
            time.sleep(2)
            return False   #devulve falso asi el juego no sigue
        else:
            print(f"{explorador.nombre}, decidiste ahorrar tu recurso y seguir de largo. Tal vez te salvaste de algo!")
            time.sleep(2)
            return True #devuelve verdadero asi el juego sigue.
    
    def abrir(self, explorador): #metodo para abrir el cofre, recibe al explorador como parametro para poder interactuar con sus atributos.
        if self.es_bueno == False: # si es malo, se activa la maldicion y se pierde todo.
            return self.perder_todo(explorador)

        if self.estado == "Cerrado": #si esta cerrado se pregunta que hacer con las ganzuas que se tiene.
            if explorador.cantidad_ganzuas > 0:
                op=input("El cofre está cerrado.Tiene " + str(explorador.cantidad_ganzuas) + " ganzuas. ¿Desea usar una ganzua para abrirlo? (s/n): ")
                
                
                if op.lower() == "s": #si lo abre gasta una ganzua, se abre el cofre y gana las monedas que tiene adentro.
                    explorador.usar_ganzua()
                    self.estado = "Abierto"
                    explorador.monedas += self.cantidad_monedas
                    print(f"{explorador.nombre} ha abierto el cofre y ha ganado {self.cantidad_monedas} monedas!")
                    time.sleep(2)   
                else:
                    print(f"{explorador.nombre}, decidiste ahorrar tu recurso y seguir de largo.")
                    time.sleep(2)
            else:
                print("¡Mala suerte! Está cerrado y no te quedan ganzúas.")
                time.sleep(2)
        else:#sino ay esta abierto y el jugador gana las monedas sin gastar recursos.
            print("El cofre ya está abierto.Estas de suerte")
            time.sleep(4)
            explorador.monedas += self.cantidad_monedas
            print(f"{explorador.nombre} ha ganado {self.cantidad_monedas} monedas al abrir el cofre!")
            time.sleep(2)
        return True#devuelve true asi sigue el juego.
    
    def dibujar_cofre(self):
        print("═"*30)
        if self.estado == "Cerrado":
            print("      __________")
            print("     /         /|")
            print("    /_________/ |")
            print("    |    🔒   | |")
            print("    |_________|/")
        else:
            print("      __________")
            print("     /        /|")
            print("    /________/ |")
            print("    |    💰  | |")
            print("    |________|/")
        print(f" TIPO: {self.tipo.upper()} | ESTADO: {self.estado}")
        print("═"*30)
            


#--CODIGO PRINCIPAL--
print("¡Bienvenido al juego de abrir cofres!") #muestro historia del juego.
print("\nEn este juego, serás un explorador que se encuentra con cofres misteriosos. Cada cofre puede estar abierto o cerrado, y dentro de cada cofre hay una cantidad aleatoria de monedas esperando ser descubierta.")
print("Tu objetivo es abrir los cofres utilizando tus ganzuas, pero ten cuidado, ya que cada cofre cerrado requerirá una ganzua para abrirlo. Administra bien tus recursos. ¡Buena suerte en tu aventura de abrir cofres y ganar monedas!")
time.sleep(8) #hago una pausa de 8 segundos para que el usuario pueda leer.

print("\n\nPrepara tus antorchas y ajusta tus botas...") #texto para que la historia tenga un poco mas de contexto
time.sleep(1.5)
print("Te adentraras en las profundidades de la Cueva de Cristal.")
time.sleep(2)

jugador = Explorador() #creo un objeto de la clase explorador
opciones_cofres = [ #creo una lista de opciones de cofres, con su tipo, rango de monedas y si son buenos o malos.
    ["Madera", 50, 150, True],
    ["Plata", 200, 400, True],
    ["Oro", 500, 1000, True]
]

cofres_raros = [ #agrego una lista de cofres raros, con mas monedas pero con la posibilidad de ser malditos.
    ["Esmeralda",1000,1450,True],
    ["Diamante",1500,2000,True],
    ["Desconocido", 0, 0, False]  # cofre trampa
]


for i in range(10): #creo un bucle para que el jugador pueda intentar abrir 10 cofres.
    print(f"\nAl caminar te cruzas algo brillante ente tanta oscuridad. ¡Es el COFRE {i+1}!:") #muestro el intento actual
    if i < 3:# los primeros 3 cofrs siempre seran buenos, asi el jugador gana monedas.
        datos = random.choice(opciones_cofres)
    else:#de ahi en adelante le pueden salir mejores o peores cofres.
        datos=random.choice(opciones_cofres+cofres_raros)

    cofre_actual = Cofre(datos[0], datos[1], datos[2], datos[3])#creo un objeto de la clase cofre con los datos del cofre actual que me salio.
    

    cofre_actual.dibujar_cofre() #dibujo el cofre para que sea mas visual.
    time.sleep(3) #hago una pausa de 2 segundos para que el usuario pueda ver el cofre y su estado antes de decidir que hacer.

    continuar_jugando = cofre_actual.abrir(jugador) # intento abrir el cofre, y dependiendo de lo que pase, el juego puede seguir o no.

    if continuar_jugando == False: #texto que se muestra cuando se pierde todo por abrir un cofre maldito.
        print("\nSin recursos ni fuerzas, no puedes continuar la exploración...")
        break

    print(f"\nEstado de {jugador.nombre}: {jugador.monedas} monedas | {jugador.cantidad_ganzuas} ganzúas.") #estado de mi jugador despues de cada intento, para que pueda ir viendo como va su progreso.
    time.sleep(2)


time.sleep(2)
print("\n" + "="*30)
print("          GAME OVER")
print("="*30)
print(f"RESUMEN FINAL: {jugador.nombre} recolectó {jugador.monedas} monedas.")#muestro estadisticas finales
