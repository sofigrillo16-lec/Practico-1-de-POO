"""Ejercicio 4 
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el 
método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un 
método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora. """

class Calculadora:
    def __init__(self, n1, n2): #metodo para iniciaizar los atributos de la clase
        self.n1 = n1
        self.n2 = n2    
        
    def suma(self):# metodo para sumar los valores y mostrar el resultado
        resultado=self.n1+self.n2
        print(f"La suma: {self.n1} + {self.n2} = {resultado}")

    def resta(self):# metodo para restar los valores y mostrar el resultado
        resultado=self.n1-self.n2
        print(f"La resta:  {self.n1} - {self.n2} = {resultado}")

    def multiplicacion(self):# metodo para multiplicar los numeros
        resultado=self.n1*self.n2
        print(f"La multiplicación:  {self.n1} * {self.n2} = {resultado}")

    def division(self):#metodo para dividir los numeros, evitando la division por cero
        if self.n2 != 0:
            resultado=self.n1/self.n2
            print(f"La división:  {self.n1} / {self.n2} es: {resultado}")
        else:
            print("Error: No se puede dividir por cero.")

#--CODIGO PRINCIPAL--
num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
calculadora1=Calculadora(num1,num2) #creo un objeto llamado calculadora1 y es de la clase Calculadora.
print("-" * 30)
calculadora1.suma() #muestro el resultado de la suma
calculadora1.resta() #muestro el resultado de la resta
calculadora1.multiplicacion() #muestro el resultado de la multiplicacion
calculadora1.division()# muestro el resultado de la division
