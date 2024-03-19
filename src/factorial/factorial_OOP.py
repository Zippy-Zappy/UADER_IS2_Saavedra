#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    def __init__(self):
        pass
    
    def factorial(self, num):
        if num < 0:
            print("No existe el factorial de un número negativo.")
            exit()
        elif num == 0:
            return 1
        else:
            return num * self.factorial(num - 1)

    def run(self, min, max):
        resultado = {}
        for i in range(min, max + 1):
            resultado[i] = self.factorial(i)
        return resultado


min = int(input("Ingrese el mínimo: "))
max = int(input("Ingrese el máximo: "))

fact = Factorial()

print(fact.run(min, max))
