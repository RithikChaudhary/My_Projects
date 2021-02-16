# Simple Calculator that does basic calculations invovling decimals and negative numbers.

import tkinter
from tkinter import *

value = 0
expression = ""


def clicked(number):
    global value
    global expression

    value = number


def display():
    global value
    global expression

    expression = expression + value
    label1['text'] = str(expression)


def press(number):
    global expression

    clicked(number)
    display()


def evaluate():
    global value
    global answer

    answer = eval(expression)
    label1['text'] = str(answer)


def clear():
    global answer
    global expression

    expression = ""
    answer = str(0)
    label1['text'] = ['Cleared']


bestcalc = tkinter.Tk()

bestcalc.title('Calculator')
bestcalc.geometry('320x450')
bestcalc.resizable(width=False, height=False)
bestcalc.configure(background='dim gray')

button1 = Button(bestcalc, text="1", font="Helvectica 12", command=lambda: press("1"), width=5, height=2, fg='black', bg='steel blue')
button1.place(x=30, y=150)

button2 = Button(bestcalc, text="2", font="Helvectica 12", command=lambda: press("2"), width=5, height=2, fg='black', bg='steel blue')
button2.place(x=100, y=150)

button3 = Button(bestcalc, text="3", font="Helvectica 12", command=lambda: press("3"), width=5, height=2, fg='black', bg='steel blue')
button3.place(x=170, y=150)

button4 = Button(bestcalc, text="4", font="Helvectica 12", command=lambda: press("4"), width=5, height=2, fg='black', bg='steel blue')
button4.place(x=30, y=210)

button5 = Button(bestcalc, text="5", font="Helvectica 12", command=lambda: press("5"), width=5, height=2, fg='black', bg='steel blue')
button5.place(x=100, y=210)

button6 = Button(bestcalc, text="6", font="Helvectica 12", command=lambda: press("6"), width=5, height=2, fg='black', bg='steel blue')
button6.place(x=170, y=210)

button7 = Button(bestcalc, text="7", font="Helvectica 12", command=lambda: press("7"), width=5, height=2, fg='black', bg='steel blue')
button7.place(x=30, y=270)

button8 = Button(bestcalc, text="8", font="Helvectica 12", command=lambda: press("8"), width=5, height=2, fg='black', bg='steel blue')
button8.place(x=100, y=270)

button9 = Button(bestcalc, text="9", font="Helvectica 12", command=lambda: press("9"), width=5, height=2, fg='black', bg='steel blue')
button9.place(x=170, y=270)

button10 = Button(bestcalc, text="+", font="Helvectica 12", command=lambda: press("+"), width=5, height=2, fg='black', bg='steel blue')
button10.place(x=240, y=150)

button11 = Button(bestcalc, text="-", font="Helvectica 12", command=lambda: press("-"), width=5, height=2, fg='black', bg='steel blue')
button11.place(x=240, y=210)

button12 = Button(bestcalc, text="x", font="Helvectica 12", command=lambda: press("*"), width=5, height=2, fg='black', bg='steel blue')
button12.place(x=240, y=270)

button13 = Button(bestcalc, text="/", font="Helvectica 12", command=lambda: press("/"), width=5, height=2, fg='black', bg='steel blue')
button13.place(x=240, y=330)

button14 = Button(bestcalc, text="=", font="Helvectica 12", command=evaluate, width=5, height=2, fg='black', bg='steel blue')
button14.place(x=240, y=390)

button15 = Button(bestcalc, text="Clear", font="Helvectica 12", command=clear, width=20, height=2, fg='black', bg='steel blue')
button15.place(x=30, y=390)

button16 = Button(bestcalc, text="0", font="Helvectica 12", command=lambda: press("0"), width=13, height=2, fg='black', bg='steel blue')
button16.place(x=30, y=330)

button17 = Button(bestcalc, text=".", font="Helvectica 12", command=lambda: press("."), width=5, height=2, fg='black', bg='steel blue')
button17.place(x=170, y=330)

label1 = Label(bestcalc, text="", font="Helvetica 24", borderwidth=5, relief='sunken', width=13, height=2, bg='white')
label1.place(x=30, y=50)

bestcalc.mainloop()
