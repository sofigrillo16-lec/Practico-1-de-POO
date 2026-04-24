"""Ejercicio 5 
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, 
el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones 
● Añadir contacto 
● Lista de contactos 
● Buscar contacto 
● Editar contacto 
● Cerrar agenda """

class Agenda:
    def __init__(self):
        self.contactos = []  # Lista para almacenar los contactos

    def agregar_contacto(self): #metodo para agregar un contacto a la agenda
        nombre = input("Ingrese el nombre: ")
        nombre = nombre.capitalize()#lo convierto a mayuscula para que se vea mejor y sea mas facil de buscar
        telefono = input("Ingrese el teléfono: ")
        email = input("Ingrese el email: ")

        contacto = {"nombre": nombre, "telefono": telefono, "email": email}#guardo todos los datos del contacto en un diccionario
        self.contactos.append(contacto) #agrego el contacto a la lista de contactos
        print("Contacto agregado exitosamente.")    
    
    def lista_contactos(self):#metodo para mostrar la lista de contactos guardados en la agenda
        if not self.contactos: #si la lista esta vacia,muestro un mensaje
            print("No hay contactos en la agenda.")
        else:
            print("\n--- LISTA DE CONTACTOS ---") #sino muestro la lista de contactos
            for contacto in self.contactos: #recorro la lista y muestro c/elemento con su respectivo formato
                print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")# uso la clave del diccionario para mostrar cada dato del contacto
    
    def buscar_contacto(self):#metodo para buscar un contacto por su nombre
        busca_nombre = input("\nIngrese el nombre del contacto a buscar: ").capitalize()#lo convierto a mayuscula para que sea mas facil de buscar,ya que asi lo guarde antes
        encontrado = False #variable para saber si encontre el contacto o no

        for contacto in self.contactos: #si la lista no esta vacia, la recorro en busca del contacto
            if contacto['nombre'] == busca_nombre:# comparo los datos
                print(f"Contacto encontrado ---> Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
                encontrado = True #si lo encuentro,muestro los datos del contacto y cambio la variable encontrado a True para saber que lo encontre

        if not encontrado:#si no encontre el contacto,muestro un mensaje
            print("Contacto no encontrado.")
    
    def editar_contacto(self):#metodo para editar un contacto por su nombre
        busca_nombre = input("\nIngrese el nombre del contacto a editar: ").capitalize()
        encontrado = False

        for contacto in self.contactos:
            if contacto['nombre'] == busca_nombre:#si encuentro el contacto,le pido al usuario que ingrese los nuevos datos y los guardo en el diccionario del contacto
                nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                nuevo_email = input("Ingrese el nuevo email: ")
                
                contacto['telefono'] = nuevo_telefono
                contacto['email'] = nuevo_email
                print("Contacto actualizado exitosamente.")
                encontrado = True #cambio la variable encontrado a True para saber que lo encontre y edite

        if not encontrado: #sino encontre el contacto,muestro un mensaje
            print("No se puede editar: contacto no encontrado.")
    
    def menu(self):#metodo para mostrar el menu de opciones y ejecutar las funciones correspondientes segun la opcion elegida por el usuario
        opcion = "0"
        while opcion != "5": #muestro el menu
            print("\n--- AGENDA PERSONAL ---")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            
            opcion = input("Elija una opción: ")
            
            if opcion == "1":
                self.agregar_contacto()
            elif opcion == "2":
                self.lista_contactos()
            elif opcion == "3":
                self.buscar_contacto()
            elif opcion == "4":
                self.editar_contacto()
            elif opcion == "5":
                print("Saliendo de la agenda... ¡Adiós!")
            else:
                print("Opción inválida, intente de nuevo.")

# -- CÓDIGO PRINCIPAL --
mi_agenda = Agenda()#creo una instancia de la clase Agenda
mi_agenda.menu()#llamo al metodo menu para mostrar el menu de opciones y ejecutar las funciones correspondientes segun la opcion elegida por el usuario
