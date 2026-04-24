import time, random

class Enemigo:#defino clase enemigo para crear distintas oleadas de ataques
    def __init__(self, tipo, daño, recompensa):#cada enemigo tiene un tipo, un daño que hace a la torre y una recompensa en monedas que da al ser derrotado.
        self.tipo = tipo
        self.daño = daño
        self.recompensa = recompensa

class Torre:#defino clase de la torre del jugador, con atributos de nombre, resistencia, monedas y si el escudo está activo o no.
    def __init__(self, nombre):
        self.nombre = nombre
        self.resistencia = 100
        self.monedas = 50
        self.escudo_activo = False

    def recibir_ataque(self, enemigo):#metodo para recibir el ataque y reducir la resistencia teniendo en cuenta el esudo.
        print(f"\n ALERTA-----¡Un {enemigo.tipo} ataca la torre!")
        if self.escudo_activo:
            daño_reducido = enemigo.daño // 2#el escudo me reduce el daño a la mitad.
            self.resistencia -= daño_reducido
            print(">>> ¡EL ESCUDO ABSORBE EL IMPACTO! (Daño reducido al 50%)")
            self.escudo_activo = False # se desactiva el escudo después de un ataque
        else:
            self.resistencia -= enemigo.daño
            print(f"¡IMPACTO DIRECTO!! Daño recibido: {enemigo.daño}")

        print(f">>>Daño recibido: {enemigo.daño}. Resistencia restante: {self.resistencia}<<<")
        
    def menu_mejoras(self):#muestro metodo con menu de mejoras para que el jugador pueda elegir antes de cada oleada, teniendo en cuenta las monedas que tiene y el costo de cada mejora.
        print(f"\n---  TIENDA DE MEJORAS (Monedas: {self.monedas}) ---")
        print("[1] Reparación Ligera (+15 Resistencia ❤️ ) - 20 monedas")
        print("[2] Reparación Reforzada (+40 Resistencia ❤️ ) - 50 monedas")
        print("[3] Activar Escudo (Próximo daño -50%) - 30 monedas")
        print("[4] Activar Escudo + Reparación (+50 Resistencia ❤️  y Próximo daño -50%) - 100 monedas")
        print("[5] No comprar mejoras, seguir con la defensa actual.")

        op = input("Selecciona una mejora: ")
        
        if op == "1" and self.monedas >= 20: #a mejora 1 es ligera, solo son 15 extra de resisencia.
            self.resistencia = min(100, self.resistencia + 15)
            self.monedas -= 20
            print(">> Torre reparada un poco. ¡Sigue resistiendo! <<")
        elif op == "2" and self.monedas >= 50:#a mejora 2 es reforzada, son 40 extra de resistencia, pero cuesta mas monedas.
            self.resistencia = min(100, self.resistencia + 40)
            self.monedas -= 50
            print(" >> ¡Gran reparación completada! << ")
        elif op == "3" and self.monedas >= 30:#la mejora 3 es el escudo, que me reduce el daño a la mitad, pero solo dura para un ataque, despues se desactiva.
            self.escudo_activo = True
            self.monedas -= 30
            print(">> Escudo de energía activado <<")
        elif op == "4" and self.monedas >=100:#la mejora 4 es la mejor, me da 50 extra de resistencia y el escudo activado, pero cuesta 100 monedas.
            self.escudo_activo = True
            self.monedas -= 100
            self.resistencia = min(100, self.resistencia + 50)
            print(">> ¡MEJORA MÁXIMA! Escudo activado y torre reforzada <<")
            
        elif op == "5":#si al jugador no le interesa, ahorra sus monedas para la siguiente oleada.
            print("Decidiste ahorrar tus monedas.")
        else:
            print("No tienes suficientes monedas o la opción es inválida.")

    def dibujar_torre(self):
        print("\n      ESTADO DE LA TORRE:")
        if self.resistencia > 50:
            # Torre intacta
            print("          [|||]          ")
            print("          |   |          ")
            print("        --|___|--        ")
            print("       [_________]       ")
        elif self.resistencia > 0:
            # Torre dañada
            print("          [x  ]          ")
            print("          | / |          ")
            print("        --|___|--        ")
            print("       [_________]       ")
        else:
            #  (GAME OVER)
            print("          .  .           ")
            print("       .       .   .     ")
            print("      _,,---,,_  .       ")
            print("    [___________]        ")
            print("   --- ESCOMBROS ---     ")

# --- CONFIGURACIÓN INICIAL ---
print(" ¡BIENVENIDO A ÚLTIMA DEFENSA! ")#texto de bienvenida al juego, explicando la misión del jugador.
print("Tu misión es proteger tu torre de oleadas de enemigos cada vez más fuertes. Sobrevive el mayor número de oleadas posible y mejora tu torre para resistir más ataques.")
time.sleep(3)
torre = Torre(input("Nombre de tu fortaleza: "))#creo objeto torre con el nombre que el jugador elija al inicio del juego.

# (Tipo, Daño, Monedas que da)
atacantes = [#defino una lista de enemigos con su tipo, el daño que hacen a la torre y las monedas que dan al ser derrotados.
    Enemigo("Caballero", 10, 20),#son todos objetos de la clase enemigo, con sus atributos correspondientes.
    Enemigo("Arquero Real", 5, 25),
    Enemigo("Cañon", 25, 45),
    Enemigo("Gigante Noble", 40, 70),
    Enemigo("Dragón", 60, 100),
    Enemigo("Mago", 15, 30)
]

oleada = 0
print("\n¡LA DEFENSA COMIENZA!")

# --- BUCLE PRINCIPAL ---
while torre.resistencia > 0:#mientras la resistencia de la torre sea mayor a 0, el juego sigue, cada vez con oleadas mas fuertes.
    oleada += 1
    print("\n" + "—"*70)#muestro estadisticas
    print(f" OLEADA {oleada:^12} | ❤️  VIDA: {torre.resistencia:^12} | 💰 MONEDAS: {torre.monedas:^12}")
    print("—"*70)

    torre.dibujar_torre()

    print("\nFase de preparación: ¿Quieres entrar a la tienda antes del ataque?")
    print("[A] Abrir Tienda")#el usuario decide que quiere hacer. 
    print("[B] Esperar al enemigo")
    
    preparar = input("Selección: ").lower()
    if preparar == "a":
        torre.menu_mejoras()

    #2. FASE DE ATAQUE
    rival = random.choice(atacantes)
    torre.recibir_ataque(rival)
    
    # 3. FASE DE RECOMPENSA (Solo si sobrevive)
    if torre.resistencia > 0:#si la torre sobrevive al ataque, el jugador recibe la recompensa en monedas que da el enemigo derrotado, y se muestra un mensaje de victoria.
        print(f"\n ¡Oleada resistida! El {rival.tipo} ha sido repelido.")
        print(f" Recompensa: +{rival.recompensa} monedas.")
        torre.monedas += rival.recompensa
        time.sleep(2)
    else:
        print(f"\nEl {rival.tipo} ha destruido los cimientos...")
    
    
    time.sleep(1.5)

print("\n" + "="*40)
print(f"  LA TORRE {torre.nombre.upper():^15} HA CAÍDO")
print(f"  Resististe {oleada:^5} oleadas.")
torre.dibujar_torre()

print("   GAME OVER")
print("="*40)