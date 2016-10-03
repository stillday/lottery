# -*- coding: utf-8 -*-
import random
import Tkinter #import von Tkinter
import tkMessageBox #import vom Message Fenster

#öffnen vom Fenster
window = Tkinter.Tk()

#Text ausgabe
greeting = Tkinter.Label(window, text="Welcome to the Lottery numbers generator.")
greeting.pack()
greeting = Tkinter.Label(window, text="Please enter how many random numbers would you like to have? ")
greeting.pack()

#Eingabe
number = Tkinter.Entry(window)
number.pack()

#definition
def lottery():

    while True:
        rand = []
        lott = random.sample(range(0, 45), int(number.get()))

        #Ausgabe der Zahlen
        tkMessageBox.showinfo("Zahlen", lott)

#Submit Button
submit = Tkinter.Button(window, text = "Lottery Number Calculator", command=lottery)
submit.pack()

window.mainloop()