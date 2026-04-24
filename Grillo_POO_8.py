import random,time
class Personaje(): #creo mi clase personajes 
    def __init__(self,nombre,vida,ataque):#los atributos son las cosas que caracterizan a cada personaje, como su nombre, vida y ataque,etc.
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.energia=100 #energia que se gasta al atacar/cubrise asi no siempre se usa lo mismo y se administran recursos
        self.defiendo = False #al iniciarlo no se esta defendiendo
    
    def mostrar_estado(self):# metodo para mostrar el estado actual del personaje, investigue sobre algunos caracteres ASCII
        largo_barra = 20
        # Calculamos cuántos bloques llenar (proporcional a la vida)
        bloques_llenos = int(self.vida * largo_barra / 100)#se calcula asi, ya que la vida es un porcentaje.
        barra = "█" * bloques_llenos + "░" * (largo_barra - bloques_llenos)
    
        # uso f-strings con espacios fijos para que todo quede alineado
        print(f"\n{self.nombre.upper():<15} [ {barra} ] {self.vida:>3}% LIFE")
        print(f"{' ':15} ENERGÍA: {self.energia}%")
        print("-" * 45)


    def atacar(self, otro_personaje, tipo_ataque):#metodo para atacar, va a recibir el otro personaje y que ataque se esta haciendo como parametros
        daño_final = 0 #variable donde voy a almacenar mi daño final segun si me cubri o no
        costo_energia=0 #cuanta energia gasto al hacer esto

        if tipo_ataque == 1: #segun lo que me ingrese el usuario, se calcula el daño final del ataque
            daño_final = self.ataque #si uso el 1, es el daño basico de mi personaje
            print(f"\n{self.nombre} lanza un ataque normal!")
            costo_energia=0#el daño basico no necesita de energia 

        elif tipo_ataque == 2:#si elige el 2, es un ataque fuerte, que hace un 50% mas de daño
            daño_final = self.ataque * 1.5
            print(f"\n{self.nombre} lanza un ataque fuerte!")
            costo_energia=30#este ya me saca 30 de energia ya que requiero mas esfuerzo.

        elif tipo_ataque == 3:#si elige el 3, es un ataque critico, que hace el doble de daño
            daño_final = self.ataque * 2
            costo_energia=50 #al querer usar un ataque mejor, me saca la mitad de mi energia.
            print(f"\n{self.nombre} lanza un ATAQUE CRÍTICO!!")

        else:
            print(f"Se CONFUNDE el {self.nombre} y realiza un ataque debil.")#si elige una opcion que no es valida, se le asigna un ataque normal por defecto
            daño_final = self.ataque
            costo_energia=0 #cuando me confundo, el ataque es malo y no uso energia.

        if self.energia >= costo_energia: #tengo que verificar que la cantidad de energia que tengo es suficiente
            self.energia-=costo_energia #en el caso de que si lo sea, le resto la energia que acabo de gastar
        
            if otro_personaje.defiendo: #cuanto dano hago si se estaba defendiendo.
                if tipo_ataque==3: #solamnto recibo algo de daño aun cubriednome cuando el ataque es critico
                    daño_final=daño_final * 0.4 #recibo el 40% del daño
                    print(f"¡{otro_personaje.nombre} estaba cubierto, pero el crítico dolió igual!")
                    time.sleep(2)
                else:
                    daño_final=0 #sino mi defenza es exitosa y no me quedan secuelas de daño
                    print(f"¡{otro_personaje.nombre} bloqueó el ataque por completo!")
                    time.sleep(2)
            
            otro_personaje.vida-=daño_final #la vida que le saco depende de la defenza segun el tipo de ataque

        else:
            print(f"¡{self.nombre} está agotado! No tiene energía para ese ataque.")

    def defenderse(self):
        if self.energia >= 15:#el defenderme me cuesta 15, por eso debo tener si o si mas que eso
            self.energia -= 15 #le resto la defenza actual que acabo de hacer
            self.defiendo = True 
            print(f"{self.nombre} se pone en guardia.")
            time.sleep(2)
        else:
            print(f"{self.nombre} intentó cubrirse pero está muy cansado.")#como engo menos de lo necesario no puedo hacer nada

    def descansar(self):
        self.energia += 40 #si no hago nada gano energia
        if self.energia > 100: 
            self.energia = 100 # No puede pasar de 100
        print(f"{self.nombre} se toma un momento y recupera energía.")
        time.sleep(2)

    def esta_vivo(self): #metodo para saber si esta vivo o no
        if self.vida > 0:
            return True# devuelve true es decir, esta vivo, si la vida es mayor a 0
        else:
            return False# devuelve false, es decir, esta muerto, si la vida es menor o igual a 0

#--CODIGO PRINCIPAL--
print("¡Bienvenido al juego de batalla de personajes!")#mensaje de bienvenida
print("En esta arena de lucha, podrás elegir entre personajes diferentes, cada uno con sus propias características de vida y ataque.")#mensaje de introduccion
print("Tu objetivo es derrotar a tu oponente, que será controlado por la computadora, eligiendo el tipo de ataque que deseas realizar en cada turno.")#mensaje de introduccion
print("Ademas de tener que administrar tu energia restante para cubrirte o poder atacar con mejores golpes!")
print("¡Que comience la batalla!")#mensaje de inicio del juego

time.sleep(3) #hago una pausa de 5 segundos para que el usuario pueda leer.
#el usuario elige su personaje, y la computadora elige uno aleatorio
opciones = [
    Personaje("Guerrero", 90, 15),
    Personaje("Mago", 85, 25),
    Personaje("Arquero", 100, 17),
    Personaje("Asesino", 70, 30),
    Personaje("Paladin", 125, 15),
    Personaje("Ninja", 110, 25),
    Personaje("Cyborg", 115, 18)
]

for i, personaje in enumerate(opciones, start=1): #muestro las opciones con enumerate
    print(f"{i}. {personaje.nombre}")

op=int(input("Seleccione el personaje: "))
if 1 <= op <= len(opciones):#mientras la opcion sea valida,se asigna el personaje elegido.
    personaje1 = opciones[op - 1] #como usamos el indice le debo restar 1 (posicionamiento directo).
else:
    print("Opción no válida. Se asignará Guerrero.")
    personaje1 = opciones[0]#sino le asigno por defecto el guerrero

personaje2 = random.choice(opciones) #elijo un personaje de forma aleatoria para la pc.
while personaje2 == personaje1: # mientras sea el mismo que el elegido por el usuario, se vuelve a elegir otro.
    personaje2 = random.choice(opciones)#le asigno uno nuevo de forma aleatoria. 

print(f"\nEl personaje 2 aleatorio es: {personaje2.nombre}")

print("\n-----IMPORTANTE-----")
print(" Todos los personajes tinen su energia al 100 cuando comienzan. Segun sus acciones esta cambiara, Ten cuidado!")
time.sleep(2)

while personaje1.esta_vivo() and personaje2.esta_vivo():#mientras ambos esten vivos, se vana  turnar para atacarse mutuamente
    personaje1.defiendo = False
    personaje2.defiendo = False
    print(f"\n--- Turno del {personaje1.nombre} ---")#el usuario elige que tipo de accion que quiere hacer, y se lo paso al metodo atacar del personaje 1.
    accion = int(input("1. Ataque Normal (0E)\n2. Ataque Fuerte (30E)\n3. Ataque Crítico (50E)\n4. Defender (15E)\n5. Descansar (+40E)\nSelección: "))
    if accion <= 3:#si es de las primeras 3 opciones se lo paso como parametro al metodo atacar
        personaje1.atacar(personaje2, accion)
    elif accion == 4:
        personaje1.defenderse()#sino me defiendo
    elif accion == 5:
        personaje1.descansar()#o descanso

    print(f"\n--- Turno del {personaje2.nombre} ---")
    if personaje2.esta_vivo(): # si el personaje 2 esta vivo, elige de forma aleaoria su ataque. 
        accion_aleatoria=random.randint(1,5)
        if accion_aleatoria<=3:# si es de las primeras 3 opciones es un parametro para el metodo atacar
            personaje2.atacar(personaje1, accion_aleatoria)
        elif accion_aleatoria == 4:
            personaje2.defenderse()#sino me defiendo
        else:
            personaje2.descansar()#o descanso

    
    #muestro el estado de vida de mis personajes despues de cada turno
    personaje1.mostrar_estado()
    personaje2.mostrar_estado()
    time.sleep(3) #hago una pausa de 5 segundos para poder leer los resultados.


print("\n" + "="*20)
print("      GAME OVER")
print("="*20)

#cuando se sale del bucle de los ataque porque algun personaje murio, se muestra quien gano. 
if personaje1.esta_vivo():
    print(f"¡{personaje1.nombre} ha salido victorioso! EL USUARIO GANA!!")
else:
    print(f"¡{personaje2.nombre} te ha derrotado! LA COMPUTADORA GANA!!")
