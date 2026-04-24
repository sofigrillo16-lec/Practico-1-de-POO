"""Ejercicio 7
Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. 
Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta. 
La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.
La clase PlazoFijo tendrá dos atributos propios, plazo e interés. Tendrá un método para obtener el 
importe del interés (cantidad*interés/100) y otro método para mostrar la información, datos del titular 
plazo, interés y total de interés.
Crear al menos un objeto de cada subclase. """

class Cuenta: #defino la clase padre Cuenta
    def __init__(self): #defino el metodo para inicializar los atributos de la clase
        self.titular = input("Ingrese el nombre del titular: ") #pido el nombre del titular
        self.cantidad = float(input("Ingrese la cantidad: ")) #pido la cantidad de dinero

    def imprimir(self):
        print(f"Titular: {self.titular} | Cantidad: {self.cantidad}")

class CajaAhorro(Cuenta):   #clase hija de Cuenta.
    def mostrar_informacion(self): #metodo para mostrar la informacion del titular y la cantidad de dinero
        print("\n>>> DETALLE DE CAJA DE AHORRO <<<")
        self.imprimir() #llamo al metodo imprimir de la clase padre para mostrar los datos del titular y la cantidad de dinero
    
class PlazoFijo(Cuenta): #defino la clase hija PlazoFijo que hereda de Cuenta, clase hija 2
    def __init__(self):
        super().__init__() #llamo al metodo init de la clase padre para inicializar los atributos heredados
        self.plazo = int(input("Ingrese el plazo en meses: ")) #pido el plazo en meses
        self.interes = float(input("Ingrese el interés anual en porcentaje: ")) #pido el interes anual en porcentaje

    def calcular_interes(self): #metodo para calcular el importe del interes
        return self.cantidad * self.interes / 100

    def mostrar_informacion(self): #metodo para mostrar la informacion del titular, plazo, interes y total de interes
        print("\n>>> DETALLE DE PLAZO FIJO <<<")
        print(f"Titular: {self.titular} | Plazo: {self.plazo} meses | Interés anual: {self.interes}% | Total de interés: {self.calcular_interes()}")

#--CODIGO PRINCIPAL-No creamos un objeto 'Cuenta' porque es una clase general, no se necesita instanciarla.
# Solo se crean objetos de las clases hijas 'CajaAhorro' y 'PlazoFijo' para mostrar su funcionamiento.
print("\n--- CAJA DE AHORRO ---")
caja = CajaAhorro() # creo almenos un objeto de esta subclase
caja.mostrar_informacion()

print("-" * 40)

print("\n--- PLAZO FIJO ---")
plazo = PlazoFijo() #creo almenos un objeto de esta subclase
plazo.mostrar_informacion()