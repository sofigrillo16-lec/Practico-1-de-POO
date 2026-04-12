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
            print("Lista de contactos:") #sino muestro la lista de contactos
            for contacto in self.contactos: #recorro la lista y muestro c/elemento con su respectivo formato
                print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")# uso la clave del diccionario para mostrar cada dato del contacto
    
    def buscar_contacto(self):#metodo para buscar un contacto por su nombre
        busca_nombre = input("Ingrese el nombre del contacto a buscar: ")
        busca_nombre = busca_nombre.capitalize()#lo convierto a mayuscula para que sea mas facil de buscar,ya que asi lo guarde antes

        encontrado = False #variable para saber si encontre el contacto o no

        for contacto in self.contactos: #si la lista no esta vacia, la recorro en busca del contacto
            if contacto['nombre'] == busca_nombre:# comparo los datos
                print(f"Contacto encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
                encontrado = True #si lo encuentro,muestro los datos del contacto y cambio la variable encontrado a True para saber que lo encontre

        if not encontrado:#si no encontre el contacto,muestro un mensaje
            print("Contacto no encontrado.")
    
    def editar_contacto(self):#metodo para editar un contacto por su nombre
        busca_nombre = input("Ingrese el nombre del contacto a editar: ")
        busca_nombre = busca_nombre.capitalize()#lo convierto a mayuscula para que sea mas facil de buscar,ya que asi lo guarde antes

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
            print("Contacto no encontrado.")
    
    def cerrar_agenda(self):#metodo para cerrar la agenda
        print("Cerrando agenda. ¡Hasta luego!")
  
    
#--CODIGO PRINCIPAL--
agenda = Agenda() #creo un objeto llamado agenda y es de la clase Agenda
print("---OPCIONES DEL MENU---" 
"\n1. Añadir contacto" 
"\n2. Lista de contactos" 
"\n3. Buscar contacto" 
"\n4. Editar contacto" 
"\n5. Cerrar agenda")
op=input("Ingrese una opción: ")

while op != "5": #mientras la opcion ingresada sea diferente a 5,el programa seguira ejecutandose
    if op == "1":
        agenda.agregar_contacto() #llamo al metodo para agregar un contacto
    elif op == "2":
        agenda.lista_contactos() #llamo al metodo para mostrar la lista de contactos
    elif op == "3":
        agenda.buscar_contacto() #llamo al metodo para buscar un contacto   
    elif op == "4":
        agenda.editar_contacto() #llamo al metodo para editar un contacto
    else:
        print("Opción no válida. Por favor, ingrese una opción del menú.")
    print("---OPCIONES DEL MENU---" 
"\n1. Añadir contacto" 
"\n2. Lista de contactos" 
"\n3. Buscar contacto" 
"\n4. Editar contacto" 
"\n5. Cerrar agenda")
    op=input("Ingrese una opción: ")

agenda.cerrar_agenda() #llamo al metodo para cerrar la agenda