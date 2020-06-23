# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 11:08:05 2020

@author: Eswar
"""
from tkinter import *
from tkinter import ttk
from functools import partial  

   


window = Tk()
window.title("Welcome to Techkncok Solutions")
window.geometry('400x400')
window.configure(background = "green");

a = Label(window ,text = "First Name", bg='green', fg='white').grid(row = 0,column = 0)
b = Label(window ,text = "Last Name", bg='green', fg='white').grid(row = 1,column = 0)
c = Label(window ,text = "Email Id", bg='green', fg='white').grid(row = 2,column = 0)
d = Label(window ,text = "Contact Number", bg='green', fg='white').grid(row = 3,column = 0)
e = Label(window ,text = "Source", bg='green', fg='white').grid(row = 4,column = 0)
f = Label(window ,text = "Destination", bg='green', fg='white').grid(row = 5,column = 0)
g = Label(window ,text = "Budget", bg='green', fg='white').grid(row = 6,column = 0)
a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1)
e1 = Entry(window).grid(row = 4,column = 1)
f1 = Entry(window).grid(row = 5,column = 1)
number1 = tk.StringVar() 

g1 = Entry(window).grid(row = 6,column = 1)
def clicked(labelResult, g1):
    num1 = (g1.get())
    #result = int(num1)  
    labelResult.config(text="Result = %s" % num1)  
    return  

    
   
#btn = ttk.Button(window ,text="Submit").grid(row=7,column=0)

clicked = partial(clicked, window, number1)  
  
buttonCal = ttk.Button(window, text= "Submit", command=clicked).grid(row=7, column=0)  

window.mainloop()