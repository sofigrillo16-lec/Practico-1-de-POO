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
    
    def mayor(self): #creo otro metodo para indicar la mayoria de edad.
        if self.edad>=18:
            print(f"{self.nombre} es mayor de edad")
        else:
            print(f"{self.nombre} no es mayor de edad")

#--CODIGO PRINCIPAL--
persona1=Persona()#creo un objeto que se llama persona1 y es de la clase Persona
persona1.imprimir()#muestro sus datos
persona1.mayor()#indico si esta es mayor de edad o no

print("-" * 30)

persona2=Persona()
persona2.imprimir()
persona2.mayor()