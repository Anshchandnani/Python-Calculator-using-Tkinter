# step1: Importing
from tkinter import *

# step2: gui interaction
window = Tk()
window.geometry('500x500')

# step3: adding inputs

# Entry box
e = Entry(window, width=61, borderwidth=5, state="readonly")
e.place(x=5, y=0)

# Function for working button
def click(num):
    e.config(state="normal")
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result)+str(num))
    e.config(state="readonly")

# Buttons

def clear():
    e.config(state="normal")
    e.delete(0, END)
    e.config(state="readonly")

b = Button(window, text='AC', width=12, command=clear)
b.place(x=5, y=30)

def cross():
    e.config(state="normal")
    current = e.get()
    e.delete(0, END)
    e.insert(0, current[:-1])
    e.config(state="readonly")

b = Button(window, text='[×]', width=12, command=cross)
b.place(x=100, y=30)

b = Button(window, text='', width=12)
b.place(x=195, y=30)

def div():
    e.config(state="normal")
    n1 = e.get()
    global i
    global math
    math = "division"
    i = int(n1)
    e.delete(0,END)
    e.config(state="readonly")

b = Button(window, text='÷', width=12, command=div)
b.place(x=290, y=30)

b = Button(window, text='7', width=12, command = lambda:click(7))
b.place(x=5, y=58)

b = Button(window, text='8', width=12, command = lambda:click(8))
b.place(x=100, y=58)

b = Button(window, text='9', width=12, command = lambda:click(9))
b.place(x=195, y=58)

def mul():
    e.config(state="normal")
    n1 = e.get()
    global i
    global math
    math = "multiplication"
    i = int(n1)
    e.delete(0,END)
    e.config(state="readonly")

b = Button(window, text='x', width=12, command=mul)
b.place(x=290, y=58)

b = Button(window, text='4', width=12, command = lambda:click(4))
b.place(x=5, y=86)

b = Button(window, text='5', width=12, command = lambda:click(5))
b.place(x=100, y=86)

b = Button(window, text='6', width=12, command = lambda:click(6))
b.place(x=195, y=86)

def sub():
    e.config(state="normal")
    n1 = e.get()
    global i
    global math
    math = "substraction"
    i = int(n1)
    e.delete(0,END)
    e.config(state="readonly")

b = Button(window, text='-', width=12, command=sub)
b.place(x=290, y=86)

b = Button(window, text='1', width=12, command = lambda:click(1))
b.place(x=5, y=114)

b = Button(window, text='2', width=12, command = lambda:click(2))
b.place(x=100, y=114)

b = Button(window, text='3', width=12, command = lambda:click(3))
b.place(x=195, y=114)

def add():
    e.config(state="normal")
    n1 = e.get()
    global i
    global math
    math = "addition"
    i = int(n1)
    e.delete(0,END)
    e.config(state="readonly")

b = Button(window, text='+', width=12, command=add)
b.place(x=290, y=114)

def zeros2():
    click(0)
    click(0)
b = Button(window, text='00', width=12, command = zeros2)
b.place(x=5, y=142)

b = Button(window, text='0', width=12, command = lambda:click(0))
b.place(x=100, y=142)

def zeros3():
    click(0)
    click(0)
    click(0)

b = Button(window, text='000', width=12, command=zeros3)
b.place(x=195, y=142)

def equal():
    e.config(state="normal")
    n2 = int(e.get())
    e.delete(0, END)
    if math=="addition":
        e.insert(0, i+n2)
    elif math=="substraction":
        e.insert(0, i-n2)
    elif math == "multiplication":
        e.insert(0, i*n2)
    elif math == "division":
        if n2 == 0:
            e.insert(0, "Error")
        else:
            e.insert(0, i/n2)
    e.config(state="readonly")

b = Button(window, text='=', width=12, command=equal)
b.place(x=290, y=142)

# step4: mainloop
mainloop()