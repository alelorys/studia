# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:26:49 2020

@author: Ola
"""
#wip - work in progress
import math
from math import *
print("""Kalkulator tarasu """)
choose = input("""Jaki typ tarasu wybierasz? 
               s - standardowy, c - niestandardowy:\n""")
def tarasStandardowy():
    print("Podaj wymiary trarasu w metrach")
    bok_tarasu_a = float(input())
    bok_tarasu_b = float(input())
    
    print("Wymiary paneli/płyt w metrach")
    bok_panela_a = float(input())
    bok_panelu_b = float(input())
    
    powierzchnia_tarasu = bok_tarasu_a*bok_tarasu_b
    powierzchnia_plyty = bok_panela_a * bok_panelu_b
    
    print("Będzie potrzebnych:",powierzchnia_tarasu/powierzchnia_plyty,"płyt")

def tarasDostosowany():
    print("Podaj wymiary tarasu w metrach: ")
    bok_a = float(input("Bok a: "))
    bok_b = float(input("Bok b: "))
    bok_c = float(input("Bok c: "))
    bok_d = float(input("Bok d: "))
    bok_e = float(input("Bok e: "))
    bok_f = float(input("Bok f: "))
    bok_g = float(input("Bok g: "))
    bok_h = float(input("Bok h: "))
    
    print("Podaj wymiary płyty/panela w metrach: ")
    plyta_a = float(input("Bok a: "))
    plyta_b =float(input("Bok b: "))
    if bok_a + bok_g == bok_c + bok_e and bok_b+bok_d == bok_h + bok_f:
        powierzchnia_tarasu = pow((bok_a+bok_g),2) * pow((bok_h + bok_f),2)
        powierzchnia_plyty = plyta_a * plyta_b
        print("Będzie potrzebnych:",powierzchnia_tarasu/powierzchnia_plyty,"płyt")
        
if choose == "s":
    tarasStandardowy()
else:
    tarasDostosowany()