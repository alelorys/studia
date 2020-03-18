# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:48:46 2020

@author: Ola
"""

import tkinter as tk
from math import *

def bmi():
    wzrost = input_wuser.get()
    waga = input_huser.get()
    
    bmi_user = float(waga)// pow(float(wzrost),2)
    label_bmi = tk.Label(win,text=f"Twoje BMI wynosi:{bmi_user}",
                         font=("calibri",10,"italic"))
    label_bmi.grid(row=6,column=0)
    if bmi_user < 18:
        label = tk.Label(win,text="niedowaga",font=("calibri",10,"italic"))
        label.grid(row=6,column=1,sticky="W")
    elif bmi_user >= 18 and bmi_user < 25:
        label = tk.Label(win,text="Waga w normie",font=("calibri",10,"italic"))
        label.grid(row=6,column=1,sticky="W")
    elif bmi_user >= 25 and bmi_user <30:
        label = tk.Label(win,text="nadwaga",font=("calibri",10,"italic"))
        label.grid(row=6,column=1,sticky="W")
    elif bmi_user >=30 and bmi_user < 40:
        label = tk.Label(win,text="otyłość",font=("calibri",10,"italic"))
        label.grid(row=6,column=1,sticky="W")
    elif bmi_user >= 40:
        label = tk.Label(win,text="otyłość ekstremalna",font=("calibri",10,"italic"))
        label.grid(row=6,column=1,sticky="W")
    else:
        label = tk.Label(win,text="Wynik nie może być ujemny!",font=("calibri",10,"italic"))
        label.grid(row=6,column=1,sticky="W")
win = tk.Tk()
win.title("Kalkulator BMI")

title = tk.Label(win, text="Sprawdź swoje BMI", font=("calibri",15,"bold"))
title.grid(row=0,column=0,columnspan=2)

label_w = tk.Label(win,text="Podaj wzrost w metrach:", font=("calibri",10,"italic"))
label_w.grid(row=2,column=0,sticky="W")
input_wuser = tk.Entry(win)
input_wuser.grid(row=2,column=1)

label_h = tk.Label(win, text="Podaj wagę:", font=("calibri",10,"italic"))
label_h.grid(row=3,column=0,sticky="W")
input_huser = tk.Entry(win)
input_huser.grid(row=3,column=1)

button = tk.Button(win,text="oblicz",
                   font=("calibri",10,"bold"),
                   bg = "navy",
                   fg = "white",
                   command = bmi)
button.grid(row=5,column=0,columnspan=2)
win.mainloop()