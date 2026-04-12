""" Ejercicio 1 
Realizar un programa que conste de una clase llamada Alumno que tenga 
como atributos el nombre y la nota del alumno. Definir los métodos para 
inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado 
de la nota y si ha aprobado o no.  """
class Alumno: #defino mi clase Alumno
    def __init__(self): #defino el metodo para inicializar los atributos de la clase
        self.nombre =input("Ingrese el nombre del alumno: ") #pido al usuario que ingrese el nombre del alumno  
        self.nota =float(input("Ingrese la nota del alumno: ")) #pido al usuario que ingrese la nota del alumno

    def imprimir(self):
        print(f"Nombre: {self.nombre}, Nota: {self.nota}")

    def resultado(self):
        if self.nota >= 7:
            print(f"{self.nombre} ha aprobado.")
        else:
            print(f"{self.nombre} no ha aprobado.")


#--CODIGO PRINCIPAL--
alumno1=Alumno() #creo un objeto que se llama alumno 1 y es de la clase Alumno
alumno1.imprimir()
alumno1.resultado() #imprimo los resultados del alumno1

alumno2=Alumno() # creo otro objeto que se llama alumno 2 y es de la clase Alumno
alumno2.imprimir()
alumno2.resultado() #muestro el resultado del alumno2