import tkinter
import time
import datetime
from playsound import playsound
from tkinter import *

time_value = time.localtime()
current_time = time.strftime("%H:%M:%S", time_value)

test_time = datetime.datetime.now().time()
time_set = datetime.time(23, 59, 59, 0)

x = 1


def clicked(argument):
    if argument == "Exit":
        alarm.destroy()

    if argument == "Start":
        set_time()

    if argument == "Clear":
        clear()


def clear():
    global x
    global time_set

    entry1.delete(0, 'end')
    x = 1
    time_set = datetime.time(23, 59, 59, 0)


def calc_time():
    global test_time
    global x
    test_time = datetime.datetime.now().time()

    if time_set < test_time:

        if x == 1:
            x = x + 1

        if x == 2:
            playsound('alarmsound.mp3', block=False)
            x = x + 1

    alarm.after(1500, calc_time)


def self_update():
    global current_time
    new_time_value = datetime.datetime.now()
    current_time = new_time_value.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, self_update)


def set_time():
    global current_time
    global test_time
    global time_set

    test_time = datetime.datetime.now().time()

    time_entry = entry1.get()
    hour, minute, second = map(int, time_entry.split(':'))
    time_set = datetime.time(hour, minute, second)

    calc_time()


alarm = tkinter.Tk()
alarm.geometry('700x450')
alarm.resizable(width=False, height=False)
alarm.title('Personal Alarm Clock')
alarm.attributes('-alpha', 1)
alarm.configure(background='purple2')

Font_tuple = ("Rockwell", 55, "bold", "italic")
Font_tuple1 = ("Rockwell", 26, "bold")
Font_tuple2 = ("Rockwell", 15, "bold")
Font_tuple3 = ("Rockwell", 40, "bold")

title = Label(alarm, text="Alarm Clock", font=Font_tuple, fg='white', bg='purple2')
title.place(x=135, y=35)

start = Button(alarm, text="Start", command=lambda: clicked("Start"), font=Font_tuple2, width=8, height=2, fg='spring green', bg='snow4').place(x=520, y=170)
clear1 = Button(alarm, text="Clear", command=lambda: clicked("Clear"), font=Font_tuple2, width=8, height=2, bg='snow4').place(x=520, y=270)
stop = Button(alarm, text="Exit", command=lambda: clicked("Exit"), font=Font_tuple2, width=8, height=2, bg='red2').place(x=130, y=350)
snooze = Button(alarm, text="Snooze", font=Font_tuple2, width=14, height=2, bg='RoyalBlue3').place(x=280, y=350)

time_label = Label(alarm, text=current_time, font=Font_tuple3, relief='sunken', width=11, height=1, bg='black', fg='white')
time_label.place(x=100, y=170)

self_update()

entry1 = Entry(alarm, text="", font=Font_tuple1)
entry1.place(x=100, y=280)

calc_time()
alarm.mainloop()

