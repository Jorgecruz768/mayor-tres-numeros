"""
Determina el mayor de tres números ingresados por el teclado
"""


class OrdenadarTresNumeros:

    def __init__(self, numero1, numero2, numero3):  # Corregido: __int__ por __init__
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3

    def intercambiar_valores(self, numero1, numero2):
        temporal = numero1
        numero1 = numero2
        numero2 = temporal
        return numero1, numero2

    def ingresar_numeros(self):
        self.numero1 = int(input("Ingrese el primer numero : "))
        self.numero2 = int(input("Ingrese el segundo numero : "))  # Corregido: "primer" por "segundo"
        self.numero3 = int(input("Ingrese el tercer numero : "))   # Corregido: "primer" por "tercer"

    def ordenar_numeros(self):
        if self.numero1 > self.numero2:
            self.numero1, self.numero2 = self.intercambiar_valores(self.numero1, self.numero2)  # Añadido self.

        if self.numero2 > self.numero3:
            self.numero2, self.numero3 = self.intercambiar_valores(self.numero2, self.numero3)  # Añadido self.

        if self.numero1 > self.numero2:
            self.numero1, self.numero2 = self.intercambiar_valores(self.numero1, self.numero2)  # Añadido self.

    def imprimir_numeros(self):
        print(f"Numeros ordenados: {self.numero1}, {self.numero2}, {self.numero3}")

if __name__ == "__main__":
    numero1 = 5
    numero2 = 10
    numero3 = 1
    numeros = OrdenadarTresNumeros(numero1, numero2, numero3)
    print("\n Numeros desordenados\n")
    numeros.imprimir_numeros()
    print("\n Numeros ordenados\n")
    numeros.ordenar_numeros()
    numeros.imprimir_numeros()

    numeros.ingresar_numeros()
    print("\n Numeros ordenados\n")
    numeros.ordenar_numeros()
    numeros.imprimir_numeros()