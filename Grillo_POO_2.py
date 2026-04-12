""" Ejercicio 2 
Realizar un programa que tenga una clase Persona con las siguientes características.
 La clase tendrá como atributos el nombre y la edad de una persona. Implementar los métodos 
 necesarios para inicializar los atributos, mostrar los datos e indicar si la persona es mayor 
 de edad o no. """
class Persona:#defino mi clase Persona
    def __init__(self): #defino el metodo para inicializar los atributos de la clase
        self.nombre=input("Ingrese su nombre: ") #ingreso el nombre de la persona
        self.edad=int(input("Ingrese su edad: "))# ingreso la edad 
    
    def imprimir(self):# defino un metodo para mostrar los datos 
        print(f"Nombre: {self.nombre.capitalize()}, Edad: {self.edad}") #muestro los datos
    
    def mayor(self): #creo otro metodo para indicar si es o no mayor de edad 
        if self.edad>=18:
            print("Es mayor de edad")
        else:
            print("NO es mayor de edad")
    
#--CODIGO PRINCIPAL--
persona1=Persona()
persona1.imprimir()
persona1.mayor()

persona2=Persona()
persona2.imprimir()
persona2.mayor()