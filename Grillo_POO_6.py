"""Ejercicio 6
En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere 
también al final del día calcular la cantidad de dinero que se ha depositado.
Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos 
nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.
La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y
deposito_total."""

class Cliente:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del cliente: ")
        self.cantidad = 0.0
    
    def depositar(self):
        monto = float(input("Ingrese el monto a depositar: "))
        self.cantidad += monto
        print(f"{self.nombre} ha depositado ${monto}. Total: ${self.cantidad}")
    
    def extraer(self):
        print(f"\n\nSaldo actual de {self.nombre}:${self.cantidad}")
        monto_extraer= float(input("Ingrese el monto a extraer: "))
        if monto_extraer <= self.cantidad:
            self.cantidad -= monto_extraer
            print(f"{self.nombre} ha extraído {monto_extraer}. Total: ${self.cantidad}")
        else:
            print("No tiene suficiente saldo para extraer esa cantidad.")
        
    def mostrar_total(self):
        print(f"\n\nEstado de cuenta de {self.nombre}:${self.cantidad}")

class Banco:
    def __init__(self):
        self.clientes = []  # lista de clientes
    #lo defino asi para que se puedan crear los clientes en el momento de operar.

    def operar(self):
        for i in range(3):#realizo un ciclo para crear 3 clientes y realizar las operaciones de cada uno
            print(f"\n--- Cliente {i+1} ---")
            cliente = Cliente()  # se crea acá (pide nombre en el momento)
            self.clientes.append(cliente) #lo agrego a la lista de clientes del banco

            cliente.depositar()#realiazo las operaciones posibles
            cliente.extraer()
            cliente.mostrar_total()
    
    def deposito_total(self):
        total = 0 #sumo el dinero de cada cliente para mostrar el total depositado en el banco
        for cliente in self.clientes:
            total += cliente.cantidad
        print(f"\nTotal de dinero en el banco: ${total}")

#--CODIGO PRINCIPAL--
banco = Banco() #creo un objeto llamado banco y es de la clase Banco
banco.operar() #realizo las operaciones de cada cliente
banco.deposito_total() #muestro el total de dinero depositado en el banco
