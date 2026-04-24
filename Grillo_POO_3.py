"""Ejercicio 3 
Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con 
los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el 
tipo de triángulo que es (equilátero, isósceles o escaleno). """

class Triangulo:
    def __init__(self):#metodo para iniciaizar los atributos de la clase
        self.lado1=float(input("Ingrese el valor del primer lado: ")) # se ingresan de a una las medidas de los lados
        self.lado2=float(input("Ingrese el valor del segundo lado: "))
        self.lado3=float(input("Ingrese el valor del tercer lado: "))

    def imprimir(self): #metodo para mostrar los datos cargados
        print(f"Lado 1: {self.lado1}, Lado 2: {self.lado2}, Lado 3: {self.lado3}")

    def mayor(self): # metodo para calcular cual es el mayor de los 3 lados 
        mayor=max(self.lado1, self.lado2, self.lado3)#uso max para saber cual es la mayor valor guardado
        print(f"El lado mayor es: {mayor}")

    def tipo(self):# metodo para saber como se relacionan las medidas de los lados y saber su tipo
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")

triangulo1=Triangulo() #creo un objeto llamado triangulo1 y es de la clase Triangulo
triangulo1.imprimir()#imprimo los datos guardados en triangulo 1
triangulo1.mayor()# muestro el lado mayor 
triangulo1.tipo()# muestro su clasificacion.
