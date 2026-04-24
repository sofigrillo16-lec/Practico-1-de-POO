import time,random 
class Aventurero():#clase aventurero con sus atributos y metodos para interactuar con los objetos que encuentra en la isla, y para mostrar su estado actual.
    def __init__(self,nombre):
        self.nombre= nombre
        self.inventario = []#lista donde guardare los objetos que encuentre el aventurero.
        self.energia = 100
    
    def recoger_objeto(self, elemento):#metodo para recoger objetos, recibe el elemento que se encuentra como parametro y lo agrega al inventario del aventurero.
        self.inventario.append(elemento)
        print(f">>>Has encontrado {elemento} y lo guardas en tu inventario!")
        time.sleep(1.5)
    
    def descartar_objeto(self, elemento):#metodo para descartar objetos, recibe el elemento que se quiere descartar como parametro y lo elimina del inventario del aventurero.
        elemento = elemento.capitalize() # Asegura que la primera letra esté en mayúscula para coincidir con el formato del inventario
        if elemento in self.inventario:
            self.inventario.remove(elemento)
            print(f">>>Has descartado {elemento} de tu inventario.")
        else:
            print(f">>>No tienes {elemento} en tu inventario para descartar.")
        time.sleep(1.5)
    
    def mostrar_estado(self):#muestro mi estado actual.
        print("\n" + "—"*40)
        print(f"AVENTURERO: {self.nombre} | ENERGÍA: {self.energia}%")
        if self.inventario:
            print(f"INVENTARIO: {', '.join(self.inventario)}")
        else:
            print(f"{self.nombre} no tiene ningún objeto en su inventario.")
        print("—"*40)
        time.sleep(1)
    
#-----CODIGO PRINCIPAL-----
elementos = [ "Linterna", "Pico","Pala", "Escudo", "Arco y flechas", "Tarta de manzana","Chatarra"]#posibles elementos

print("BIENVENIDO QUERIDO JUGADOR!")#contexto para que quede mas emocionante la historia.
time.sleep(1.5)
print("En esta aventura, podrás recoger objetos, descartarlos y revisar tu inventario!")
time.sleep(2)

aventurero = Aventurero(input("¿Cuál es tu nombre? "))#creo un objeto de la clase aventurero, pidiendole al usuario que ingrese su nombre para personalizar la experiencia.

print("\nUn avion se cae y quedas atrapado en una isla misteriosa. Para sobrevivir, necesitas encontrar objetos útiles que te ayuden a escapar.")
time.sleep(2)
print("Sales de las ruinas del avión y comienzas a explorar la isla. ")
time.sleep(2)
print("De repente, encuentras un cofre antiguo. Al abrirlo, descubres que contiene varios objetos.\n")
time.sleep(3)

#recoleccion inicial de objetos
for i in range(random.randint(2,4)): #hago un ciclo para que el aventurero pueda recoger entre 2 y 4 objetos de forma aleatoria.
    objeto = random.choice(elementos)
    if objeto not in aventurero.inventario: #mientras el objeto no este en el inventario, se vuelve a elegir otro.
        aventurero.recoger_objeto(objeto)

jugando = True
while jugando and aventurero.energia>0: # Mientras pueda seguir y tenga enertgia
    aventurero.mostrar_estado()#muestro su estado
    print("\n--- ¿Qué quieres hacer ahora? ---")#menu de opciones
    print("1. Seguir explorando la isla(-20E)")
    print("2. Descansar y comer Tarta (+40E)")
    print("3. Tirar algo de la mochila")
    print("4. Intentar escapar de la isla (Final)")
    
    opcion = input("Seleccion: ")

    if opcion == "1":
        aventurero.energia -= 20
        print("\n--- ZONAS DE EXPLORACIÓN ---") #ZONAS DE EXPLORACION POSIBLES, CADA UNA CON SU BENEFICIO Y RIESGO.
        print("[A] Explorar la Selva (Mucha vegetación)")
        print("[B] Explorar la Cueva Oscura (Un poco aterrador)")
        print("[C] Caminar por la Costa (Restos del avión)")
        
        zona = input("¿A qué zona quieres ir? (a/b/c): ").lower()

        if zona == "a": # SELVA
            print("\nTe adentras en la espesa selva...")
            time.sleep(1.5)

            # EVENTO DE CAZA: Si tiene arco y flechas, puede intentar cazar un jabalí para recuperar energía
            if "Arco y flechas" in aventurero.inventario:
                print("\n\nMientras caminas, escuchas ruidos entre los arbustos...")
                print("¡Ves un jabalí! Tienes arco y flechas.")
                if input("¿Intentas cazarlo? (s/n): ").lower() == 's':
                    print("¡Éxito! Consigues carne y recuperas 30 de energía.")
                    aventurero.energia = min(aventurero.energia + 30, 100)# evita que la energía supere el máximo de 100
                    aventurero.descartar_objeto("Arco y flechas")         

        # EVENTO DE AVISPAS:si tiene escudo puede protegerse, sino pierde energia extra.
            if random.random() < 0.45: # 45% de probabilidad de ataque
                print("\n\nMientras caminas, escuchas un zumbido... ¡Un enjambre de avispas gigantes se acerca rápidamente!")
                print("¡Unas AVISPAS GIGANTES te atacan!")
                time.sleep(2)
                if "Escudo" in aventurero.inventario:
                    print("¡Usas tu escudo para protegerte y sales ileso!")
                    if "Machete" not in aventurero.inventario:
                        print("En el suelo ves un Machete que alguien perdió.Tal vez lo puedas usar si vas a la costa.")
                        aventurero.recoger_objeto("Machete")
                else:
                    print("No tienes protección. Pierdes 10 de energía extra por las picaduras.")
                    aventurero.energia -= 10

            print("\nSigues explorando la selva y encuentras una caja de madera semi enterrada...")
            hallazgo = random.choice(elementos)#sino aun asi te da un elemento.
            print(f"Encuentras: {hallazgo}")
            if input("¿Recogerlo? (s/n): ").lower() == 's':#el usuairio decide si lo recoge o no, pero si lo hace se agrega a su inventario.
                aventurero.recoger_objeto(hallazgo)
 
        elif zona == "b": # CUEVA (si tienen linterna puede entrar, sino pierda energia)
            if "Linterna" not in aventurero.inventario:
                print("\nTe adentras en la cueva oscura sin una linterna... No puedes ver nada y te sientes perdido... tropiezas y pierdes 10 de energía. Debes salir de forma inmediata.")
                aventurero.energia -= 10
                time.sleep(1.5)
            else:
                print("\nEntras a la cueva con cuidado... Pero tu miedo crece y crece a medida que avanzas, la oscuridad es tan intensa que apenas puedes con lo que alumbra tu linterna. De repente, ves una pared con una grieta...")
                if "Pico" in aventurero.inventario:#SI TIENE PICO, puede intentar picar la pared y encontrar la llave para escapar.
                    if input("¿Quieres picar la pared? (s/n): ").lower() == 's':
                        print("¡Encontraste la Llave misteriosa!")
                        aventurero.recoger_objeto("Llave misteriosa")
                else:
                    print("No tienes nada para investigar este evento, así que decides seguir adelante, pero no encuentras nada más de interés.")
                    print("Tal vez necesitas algo para investigar la pared sospechosa...")
                    time.sleep(1.5)

        elif zona == "c": # COSTA (si tiene pala puede cavar y encontrar un tesoro, sino solo encuentra un objeto)
            print("\nBuscas entre los restos del avión en la costa...")
            print("El sonido de las olas y la brisa marina te acompañan mientras buscas entre los escombros del avión. De repente, algo brilla entre los restos...")
            time.sleep(3)
            
            hallazgo = random.choice(elementos) #hallazgo aleatorio entre los elementos.
            print(f"\nEncuentras: {hallazgo}")
            if input("¿Recogerlo? (s/n): ").lower() == 's':
                aventurero.recoger_objeto(hallazgo)

            if "Pala" in aventurero.inventario:#si llega a tener pala cava y encuentra un tesoro
                print("\nMientras sigues buscando, te das cuenta de que la pala podría ser útil para cavar entre los restos del avión...")
                accion = input("¿Quieres usar tu pala para cavar entre los restos? (s/n): ").lower()
                if accion == 's':#el usuario decide que hacer.
                    print("\nEncuentras un cofre enterrado...")
                    tesoro = random.choice(["Tarta de manzana", "Escudo", "Arco y flechas"])
                    aventurero.recoger_objeto(tesoro)

            if "Machete" in aventurero.inventario:#si tiene machete, se desbloquea otro evento en la costa, el de los cocos, que le da energia extra.
                # Evento de los Cocos (Uso del Machete)
                print("\n\nVes unas palmeras cargadas de cocos, pero están muy altos y la cáscara es dura.")
                print("Mientras observas, te das cuenta de que necesitas algo para alcanzar los cocos...")
                op=input("¿Quieres usar tu Machete para bajar y abrir unos cocos? (s/n): ")
                if op.lower() == 's':
                    print("¡Con golpes precisos de tu machete, logras abrir los cocos!")
                    print("El agua de coco te refresca mucho. Recuperas 20 de energía. Pero se rompe tu machete en el proceso.")
                    aventurero.energia = min(aventurero.energia + 20, 100)
                    aventurero.descartar_objeto("Machete") # El machete se rompe al usarlo para abrir los cocos

    elif opcion == "2": #si elige descansar, recupera energia pero solo si tiene tarta de manzana, sino le digo que no tiene comida.
        if "Tarta de manzana" in aventurero.inventario:
            aventurero.energia = min(aventurero.energia + 40, 100)
            aventurero.descartar_objeto("Tarta de manzana")
            print("¡Delicioso! Te sientes mucho mejor.")
        else:
            print("\nNo tienes comida. ¡Debes ir a buscar!")

    elif opcion == "3":#si elige tirar algo, se le muestra su inventario y se le pregunta que quiere tirar, y se descarta ese objeto.
        que_tirar = input("¿Qué objeto quieres descartar?: ")
        aventurero.descartar_objeto(que_tirar)

    elif opcion == "4":#si elige escapar de la isla, se verifica si tiene la llave misteriosa, si la tiene gana el juego, sino le digo que no puede escapar.
        print("\nLlegas a la orilla y ves un bote viejo...")
        if "Llave misteriosa" in aventurero.inventario:
            print("¡La llave encaja en el motor del bote! Logras escapar de la isla.")
            jugando = False
        else:
            print("El bote está encadenado. Necesitas una llave para liberarlo.")
    
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")
    
    if aventurero.energia <= 0: #si no comio en ningun momento pierde por falta de energia.
        print("\nTe has quedado sin fuerzas... el cansancio te vence.")
        time.sleep(2)
        jugando=False

print("\n" + "="*25)
print("      GAME OVER")
print("="*25)
        