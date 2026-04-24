"""Ejercicio 6
En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere 
también al final del día calcular la cantidad de dinero que se ha depositado.
Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos 
nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.
La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y
deposito_total."""

class Cliente:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del cliente: ") #pido el nombre del cliente al momento de crear el objeto
        self.cantidad = 0.0
    
    def depositar(self):#metodo para depositar dinero y sumarlo a la cuenta del cliente
        monto = float(input(f"Ingrese monto a depositar para {self.nombre}: "))
        self.cantidad += monto
    
    def extraer(self):#metodo para extraer dinero y restarlo de la cuenta del cliente, verificando que tenga suficiente saldo.
        monto = float(input(f"Ingrese monto a extraer para {self.nombre}: "))
        if monto <= self.cantidad:
            self.cantidad -= monto
            print(f"{self.nombre} ha extraído ${monto}")
        else:
            print("No tiene suficiente saldo para extraer esa cantidad.")
        
    def mostrar_total(self):#muestra el estado al finalizar sus operaciones
        print(f"\n\nEstado de cuenta de {self.nombre}:${self.cantidad}")

class Banco:
    def __init__(self):
        self.clientes = [] #creo una lista vacía para almacenar los clientes del banco

    def operar(self):
        for i in range(3):#realizo un ciclo para crear 3 clientes y realizar las operaciones de cada uno
            print(f"\n--- Cliente {i+1} ---")
            cliente = Cliente()  # se crea acá (pide nombre en el momento)
            

            cliente.depositar()#realiazo las operaciones posibles
            cliente.extraer()
            cliente.mostrar_total()

            self.clientes.append(cliente) #lo agrego a la lista de clientes del banco
    
    def deposito_total(self):
        total = 0 #sumo el dinero de cada cliente para mostrar el total depositado en el banco
        for cliente in self.clientes:
            total += cliente.cantidad
            
        print("\n" + "="*30)
        print(f"TOTAL DEPOSITADO EN EL BANCO: ${total}")
        print("="*30)

#--CODIGO PRINCIPAL--
banco = Banco() #creo un objeto llamado banco y es de la clase Banco
banco.operar() #realizo las operaciones de cada cliente
banco.deposito_total() #muestro el total de dinero depositado en el banco
