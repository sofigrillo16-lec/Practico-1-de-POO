import time,random
class Hechicero(): #creo mi clase personajes 
    def __init__(self,nombre,vida,hechizo):#los atributos son las cosas que caracterizan a cada personaje, como su nombre, vida y ataque
        self.nombre = nombre
        self.vida = vida
        self.hechizo = hechizo # Atributo para que cada mago pegue distinto
        self.magia=100 #energia que se gasta al atacar,cubrise asi no siempre se usa lo mismo y se administran recursos
        self.escudo_activo = False #al iniciarlo no se esta defendiendo
    
    def mostrar_estado(self):# metodo para mostrar el estado actual del personaje
        vida_visual = max(0, self.vida)#evita errores si la vida/magia baja de 0

        largo_barra = 20
        bloques_llenos = int(vida_visual * largo_barra / 100)#se calcula asi, ya que la vida es un porcentaje.
        barra_vida = "█" * bloques_llenos + "░" * (largo_barra - bloques_llenos)
    
        # uso f-strings con espacios fijos para que todo quede alineado
        print("\n" + "="*50)
        print(f"{self.nombre.upper():<15} [ {barra_vida} ] {vida_visual:>3}% LIFE")
        print(f"{' ':15} MAGIA: {self.magia}%")
        print("="*50)
        

    def lanzar_hechizo(self, otro_personaje, tipo_hechizo):#metodo para atacar, va a recibir el otro personaje y que ataque se esta haciendo como parametros
        daño_final = 0 #variable donde voy a almacenar mi daño final segun si me cubri o no
        costo_magia=0 #cuanta energia gasto al hacer esto

        if tipo_hechizo == 1: #segun lo que me ingrese el usuario, se calcula el daño final del ataque
            daño_final = self.hechizo #si uso el 1, es el daño basico de mi personaje
            print(f"{self.nombre} lanza chispas, un hechizo muy basico!")
            costo_magia=5 #se gasta algo de magia

        elif tipo_hechizo == 2:#si elige el 2, es un gran hechizo , que hace un 50% mas de daño
            daño_final = self.hechizo * 1.5 #si uso el 2, es un gran hechizo que hace un 50% mas de daño
            print(f"{self.nombre} lanza un gran hechizo!")
            costo_magia=20 #este ya me saca 30 de energia ya que requiero mas esfuerzo.

        elif tipo_hechizo == 3:#si elige el 3, es un hechizo critico, que hace el doble de daño
            daño_final = self.hechizo * 2  #si uso el 3, es un hechizo critico que hace el doble de daño
            costo_magia=50 #al querer usar un hechizo mejor, me saca la mitad de mi energia.
            print(f"¡{self.nombre} lanza un HECHIZO CRITICO!!")

        else:
            print(f"Se CONFUNDE el {self.nombre} y realiza un hechizo debil.")#si elige una opcion que no es valida, se le asigna un hechizo normal por defecto
            daño_final = self.hechizo * 0.5 #cuando me confundo, el hechizo es malo y hace menos daño.
            costo_magia=10 #cuando me confundo, el hechizo es malo y uso poca magia.

        if self.magia >= costo_magia: #tengo que verificar que la cantidad de energia que tengo es suficiente
            self.magia-=costo_magia #en el caso de que si lo sea, le resto la energia que acabo de gastar
        
            if otro_personaje.escudo_activo: #cuanto dano hago si se estaba defendiendo.
                if tipo_hechizo==3: #solamnto recibo algo de daño aun cubriednome cuando el ataque es critico
                    daño_final=daño_final * 0.5 #recibo el 50% del daño
                    print(f"¡{otro_personaje.nombre} estaba cubierto, y su escudo mágico amortiguó el impacto!")
                    time.sleep(2)
                else:
                    daño_final=0 #sino mi defenza es exitosa y no me quedan secuelas de daño
                    print(f"¡{otro_personaje.nombre} bloqueó el hechizo por completo con un Escudo Magico!")
                    time.sleep(2)
            
            otro_personaje.vida-=daño_final #la vida que le saco depende de la defenza segun el tipo de ataque

        else:
            print(f"¡{self.nombre} está agotado! No tiene energía para ese ataque.")

    def escudo_magico(self):
        if self.magia >= 15:#el defenderme me cuesta 15, por eso debo tener si o si mas que eso
            self.magia -= 15 #le resto la defenza actual que acabo de hacer
            self.escudo_activo = True 
            print(f"{self.nombre} se pone en guardia.")
            time.sleep(2)
        else:
            print(f"{self.nombre} intentó cubrirse pero está muy cansado.")#como engo menos de lo necesario no puedo hacer nada

    def meditar(self):
        self.magia += 30 #si no hago nada gano energia
        if self.magia > 100: 
            self.magia = 100 # No puede pasar de 100
        print(f"{self.nombre} se toma un momento y recupera energía.")
        time.sleep(2)

    def esta_vivo(self): #metodo para saber si esta vivo o no
        if self.vida > 0:
            return True# devuelve true es decir, esta vivo, si la vida es mayor a 0
        else:
            return False# devuelve false, es decir, esta muerto, si la vida es menor o igual a 0

#--CODIGO PRINCIPAL--
print("¡Bienvenido al juego de batalla de hechiceros!")#mensaje de bienvenida
print("En esta arena de lucha, podrás elegir entre Hechiceros diferentes, cada uno con sus propias características de vida y magia.")#mensaje de introduccion
print("Tu objetivo es derrotar al Hechicero Oscuro, que será controlado por la computadora, eligiendo el tipo de magia que deseas implementar en cada turno.")#mensaje de introduccion
print("Ademas de tener que administrar tu magia restante para cubrirte o poder atacar con mejores hechizos!")
print("¡Que comience la batalla!")#mensaje de inicio del juego

time.sleep(3) #hago una pausa de 5 segundos para que el usuario pueda leer.
#el usuario elige su personaje, y la computadora elige uno aleatorio
opciones = [
    Hechicero("Wizard", 98, 15),
    Hechicero("Sorcerers", 99, 25),
    Hechicero("Enchanter", 100, 17),
    Hechicero("Warlock", 97, 30),
    Hechicero("Necromancer", 105, 20)
]

for i, personaje in enumerate(opciones, start=1): #muestro las opciones con enumerate
    print(f"{i}. {personaje.nombre}")

op=int(input("Seleccione el hechicero que desea: "))
if 1 <= op <= len(opciones):#mientras la opcion sea valida,se asigna el personaje elegido.
    personaje1 = opciones[op - 1] #como usamos el indice le debo restar 1 (posicionamiento directo).
else:
    print("Opción no válida. Se asignará Wizard.")
    personaje1 = opciones[0]#sino le asigno por defecto el guerrero

time.sleep(2)
personaje2 = random.choice(opciones) #elijo un personaje de forma aleatoria para la pc.
while personaje2 == personaje1: # mientras sea el mismo que el elegido por el usuario, se vuelve a elegir otro.
    personaje2 = random.choice(opciones)#le asigno uno nuevo de forma aleatoria. 

print(f"\nEl personaje 2 aleatorio es: {personaje2.nombre}")

time.sleep(2)
print("\n-----IMPORTANTE-----")
print("Todos los personajes tinen su magia al 100 cuando comienzan. Segun sus acciones esta cambiara, Ten cuidado!")
time.sleep(2)

while personaje1.esta_vivo() and personaje2.esta_vivo():#mientras ambos esten vivos, se vana  turnar para atacarse mutuamente
    personaje1.escudo_activo = False
    personaje2.escudo_activo = False
    print(f"\n--- Turno del {personaje1.nombre} ---")#el usuario elige que tipo de accion que quiere hacer, y se lo paso al metodo atacar del personaje 1.
    accion = int(input("1. Hechizo Basico (5M)\n2. Hechizo Fuerte (20M)\n3. Hechizo Crítico (50M)\n4. Escudo Mágico (15M)\n5. Meditar (+30M)\nSelección: "))
    if accion <= 3:#si es de las primeras 3 opciones se lo paso como parametro al metodo atacar
        personaje1.lanzar_hechizo(personaje2, accion)# lanzo el hechizo que elija el usuario, y le paso como parametro el personaje 2 para que se le reste la vida.
    elif accion == 4:
        personaje1.escudo_magico()#sino me defiendo con un escudo magico
    elif accion == 5:
        personaje1.meditar()#recupero energia

    print(f"\n--- Turno del {personaje2.nombre} ---")
    if personaje2.esta_vivo(): # si el personaje 2 esta vivo, elige de forma aleaoria su ataque. 
        accion_aleatoria=random.randint(1,5)
        if accion_aleatoria<=3:# si es de las primeras 3 opciones es un parametro para el metodo atacar
            personaje2.lanzar_hechizo(personaje1, accion_aleatoria)
        elif accion_aleatoria == 4:
            personaje2.escudo_magico()#sino me defiendo con un escudo magico
        else:
            personaje2.meditar()#recupero energia
    
    #muestro el estado de vida de mis personajes despues de cada turno
    personaje1.mostrar_estado()
    personaje2.mostrar_estado()
    time.sleep(3) #hago una pausa de 3 segundos para poder leer los resultados.


print("\n" + "="*20)
print("      GAME OVER")
print("="*20)

#cuando se sale del bucle de los ataque porque algun personaje murio, se muestra quien gano. 
if personaje1.esta_vivo():
    print(f"¡{personaje1.nombre} ha salido victorioso! EL USUARIO GANA!!")
else:
    print(f"¡{personaje2.nombre} te ha derrotado! LA COMPUTADORA GANA!!")