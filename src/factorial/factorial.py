#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        exit()

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) == 0:
   print("Debe informar un número!")
   sys.exit()

#inf = int(input("Número inferior hasta 1: "))
inf_dos = int(input("Número inferior hasta 60: "))

num=int(input("Número: "))

if (num < inf_dos or num > 60): #(num > 1 or num < inf) or 
    print("Rango no permitido")
    exit()

print("Factorial ",num,"! es ", factorial(num)) 

