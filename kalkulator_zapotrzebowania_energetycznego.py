# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:45:32 2020

@author: Ola
"""

print("Kalkulator zapotrzebowania energetycznego")

def zapotrzebowanieMezczyzny():
    waga = int(input("Masa ciała: "))
    wzrost = int(input('Wzrost(cm): '))
    wiek = int(input('Wiek: '))
    
    zapotrzebowanie = 66+ (13.7 * waga) + (5 * wzrost) - (4.7 * wiek)
    print(zapotrzebowanie)
    
def zapotrzebowanieKobiety():
    waga = int(input("Masa ciała: "))
    wzrost = int(input('Wzrost(cm): '))
    wiek = int(input('Wiek: '))
    
    zapotrzebowanie = 655 + (9.6 * waga) + (1.8 * wzrost) - (4.7 * wiek)
    print(zapotrzebowanie)
    
plec = input('Jesteś kobietą czy mężczyzną? k - kobieta / m - mężczyzna: ')

if plec == "k":
    zapotrzebowanieKobiety()
elif plec == "m":
    zapotrzebowanieMezczyzny()
else:
    print("Podałeś niewłaściwą wartość")