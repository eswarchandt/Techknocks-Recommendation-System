# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 00:28:23 2020

@author: Eswar
"""

import tkinter as tk  
from functools import partial  
   
data = [ ["val1", "val2", "val3"],    
["asd1", "asd2", "asd3"],   
["bbb1", "bbb3", "bbb4"], ["ccc1", "ccc3", "ccc4"], ["ddd1", "ddd3", "ddd4"], ["eee1", "eee3", "eee4"] ] 
  
def call_result(label_result, n1,n2):  
    num1 = (n1.get())
    name = (n2.get())
    result = int(num1)
    label_result.config(text="Results with in your budget of rupees  %d"  % result)
    frame = Frame(root) 
    #frame.pack() 
    tree = ttk.Treeview(frame, columns = (1,2,3), height = 5, show = "headings")

    #tree.pack(side = 'left') 

    #tree.heading(1, text="Column 1") 
    #tree.heading(2, text="Column 2")
    #tree.heading(3,text="Column 3") 

    #tree.column(1, width = 100)
    #tree.column(2, width = 100) 
    #tree.column(3, width = 100) 

    scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview) 

    scroll.pack(side = 'right', fill = 'y') 

    tree.configure(yscrollcommand=scroll.set) 

    for val in data: tree.insert('', 'end', values = (val[0], val[1], val[2]) )
    return  
   
root = tk.Tk()  
root.geometry('400x200+100+200')  
  
root.title('Calculator')  
   
number1 = tk.StringVar()  
name = tk.StringVar()
#number2 = tk.StringVar()

labelNum1 = tk.Label(root, text="Full Name").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="Phone Number").grid(row=2, column=0)
labelNum3 = tk.Label(root, text="Email-Id").grid(row=3, column=0)
labelNum4 = tk.Label(root, text="Source").grid(row=4, column=0)
labelNum5 = tk.Label(root, text="Destination").grid(row=5, column=0) 
labelNum6 = tk.Label(root, text="Budget").grid(row=6, column=0) 

  
#labelNum2 = tk.Label(root, text="B").grid(row=2, column=0)  
  
labelResult = tk.Label(root)  
  
labelResult.grid(row=7, column=2)  
  
entryNum2 = tk.Entry(root, textvariable=name).grid(row=1, column=2)
entryNum3 = tk.Entry(root).grid(row=2, column=2)
entryNum4 = tk.Entry(root).grid(row=3, column=2)
entryNum5 = tk.Entry(root).grid(row=4, column=2)
entryNum6 = tk.Entry(root).grid(row=5, column=2)
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=6, column=2)
#entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)  
  
call_result = partial(call_result, labelResult, number1, name)  
  
buttonCal = tk.Button(root, text="Submit", command=call_result).grid(row=7, column=0)  
  
root.mainloop()  
