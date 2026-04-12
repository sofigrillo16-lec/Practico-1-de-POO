"""Ejercicio 4 
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el 
método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un 
método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora. """

class Calculadora:
    def __init__(self): #metodo para iniciaizar los atributos de la clase
        self.num1=int(input("Ingrese el primer número: "))
        self.num2=int(input("Ingrese el segundo número: "))
    
    def suma(self):# metodo para sumar los valores y mostrar el resultado
        resultado=self.num1+self.num2
        print(f"La suma: {self.num1} + {self.num2} = {resultado}")

    def resta(self):# metodo para restar los valores y mostrar el resultado
        resultado=self.num1-self.num2
        print(f"La resta:  {self.num1} - {self.num2} = {resultado}")

    def multiplicacion(self):# metodo para multiplicar los numeros
        resultado=self.num1*self.num2
        print(f"La multiplicación:  {self.num1} * {self.num2} = {resultado}")

    def division(self):
        if self.num2 != 0:
            resultado=self.num1/self.num2
            print(f"La división:  {self.num1} / {self.num2} es: {resultado}")
        else:
            print("Error: No se puede dividir por cero.")

#--CODIGO PRINCIPAL--
calculadora1=Calculadora() #creo un objeto llamado calculadora1 y es de la clase Calculadora
calculadora1.suma() #muestro el resultado de la suma
calculadora1.resta() #muestro el resultado de la resta
calculadora1.multiplicacion() #muestro el resultado de la multiplicacion
calculadora1.division()# muestro el resultado de la division
