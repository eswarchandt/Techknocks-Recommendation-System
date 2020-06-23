# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:33:21 2020

@author: Eswar
"""

from tkinter import *
from tkinter import ttk
import tkinter as tk
import itertools


def foodclick():
    labelText.set('Travels you may like : ')
   
    
    support = int(40)
    confidence = int(60)
    
    C1 = {}
    
    transactions = 0
    D = []
    T = []
    
    with open(r"C:\Users\Eswar\Desktop\Simpli_Learn\Internship\Data1.txt", "r") as f:
        for line in f:
            T = []
            transactions += 1
            for word in line.split():
                T.append(word)
                if word not in C1.keys():
                    C1[word] = 1
                else:
                    count = C1[word]
                    C1[word] = count + 1
            D.append(T)

    L1 = []
    for key in C1:
        if (100 * C1[key]/transactions) >= support:
            list = []
            list.append(key)
            L1.append(list)


    def apriori_gen(Lk_1, k):
        length = k
        Ck = [] 
        for list1 in Lk_1:
            for list2 in Lk_1:
                count = 0
                c = []
                if list1 != list2:
                    while count < length-1:
                        if list1[count] != list2[count]:
                            break
                        else:
                            count += 1
                    else:
                        if list1[length-1] < list2[length-1]:
                            for item in list1:
                                c.append(item)
                            c.append(list2[length-1])
                            if not has_infrequent_subset(c, Lk_1, k):
                                Ck.append(c) 
                                c = []
        return Ck


    def findsubsets(S,m):
        return set(itertools.combinations(S, m))


    def has_infrequent_subset(c, Lk_1, k):
        list = []
        list = findsubsets(c,k)
        for item in list: 
            s = []
            for l in item:
                s.append(l)
            s.sort()
            if s not in Lk_1:
                return True
        return False


    def frequent_itemsets():
        k = 2
        Lk_1 = []
        Lk = []
        L = []
        count = 0
        transactions = 0
        for item in L1:
            Lk_1.append(item)
        while Lk_1 != []:
            Ck = []
            Lk = []
            Ck = apriori_gen(Lk_1, k-1)

            for c in Ck:
                count = 0
                transactions = 0
                s = set(c)
                for T in D:
                    transactions += 1
                    t = set(T)
                    if s.issubset(t) == True:
                        count += 1
                if (100 * count/transactions) >= support:
                    c.sort()
                    Lk.append(c)
            Lk_1 = []

            for l in Lk:
                Lk_1.append(l)
            k += 1
            if Lk != []:
                L.append(Lk)
    
        return L
     

    def generate_association_rules():
        s = []
        r = []
        length = 0
        count = 1
        inc1 = 0
        inc2 = 0
        num = 1
        m = []
        L= frequent_itemsets()
        
        for list in L:
            for l in list:
                length = len(l)
                count = 1
                while count < length: 
                    s = []
                    r = findsubsets(l,count)
                    count += 1
                    for item in r:
                        inc1 = 0
                        inc2 = 0
                        s = []
                        m = []
                        for i in item:
                            s.append(i)
                        for T in D:
                            if set(s).issubset(set(T)) == True:
                                inc1 += 1
                            if set(l).issubset(set(T)) == True:
                                inc2 += 1
                        if 100*inc2/inc1 >= confidence:
                            for index in l:
                                if index not in s:
                                    m.append(index)
                            
                            print(" %d : %s ==> %s " %(num, s, m))
                            num += 1  

    generate_association_rules()   

    
        
def beachclick():
    labelText.set(' Accomodations on your choice:')
    
    
    
        
    support = int(35)
    confidence = int(50)
    
    C1 = {}
   
    transactions = 0
    D = []
    T = []
    
    with open(r"C:\Users\Eswar\Desktop\Simpli_Learn\Internship\beaches.txt", "r") as f:
        for line in f:
            T = []
            transactions += 1
            for word in line.split():
                T.append(word)
                if word not in C1.keys():
                    C1[word] = 1
                else:
                    count = C1[word]
                    C1[word] = count + 1
            D.append(T)

    L1 = []
    for key in C1:
        if (100 * C1[key]/transactions) >= support:
            list = []
            list.append(key)
            L1.append(list)


    def apriori_gen(Lk_1, k):
        length = k
        Ck = [] 
        for list1 in Lk_1:
            for list2 in Lk_1:
                count = 0
                c = []
                if list1 != list2:
                    while count < length-1:
                        if list1[count] != list2[count]:
                            break
                        else:
                            count += 1
                    else:
                        if list1[length-1] < list2[length-1]:
                            for item in list1:
                                c.append(item)
                            c.append(list2[length-1])
                            if not has_infrequent_subset(c, Lk_1, k):
                                Ck.append(c) 
                                c = []
        return Ck


    def findsubsets(S,m):
        return set(itertools.combinations(S, m))


    def has_infrequent_subset(c, Lk_1, k):
        list = []
        list = findsubsets(c,k)
        for item in list: 
            s = []
            for l in item:
                s.append(l)
            s.sort()
            if s not in Lk_1:
                return True
        return False


    def frequent_itemsets():
        k = 2
        Lk_1 = []
        Lk = []
        L = []
        count = 0
        transactions = 0
        for item in L1:
            Lk_1.append(item)
        while Lk_1 != []:
            Ck = []
            Lk = []
            Ck = apriori_gen(Lk_1, k-1)

            for c in Ck:
                count = 0
                transactions = 0
                s = set(c)
                for T in D:
                    transactions += 1
                    t = set(T)
                    if s.issubset(t) == True:
                        count += 1
                if (100 * count/transactions) >= support:
                    c.sort()
                    Lk.append(c)
            Lk_1 = []

            for l in Lk:
                Lk_1.append(l)
            k += 1
            if Lk != []:
                L.append(Lk)
    
        return L
     

    def generate_association_rules():
        s = []
        r = []
        length = 0
        count = 1
        inc1 = 0
        inc2 = 0
        num = 1
        m = []
        L= frequent_itemsets()
       
        for list in L:
            for l in list:
                length = len(l)
                count = 1
                while count < length: 
                    s = []
                    r = findsubsets(l,count)
                    count += 1
                    for item in r:
                        inc1 = 0
                        inc2 = 0
                        s = []
                        m = []
                        for i in item:
                            s.append(i)
                        for T in D:
                            if set(s).issubset(set(T)) == True:
                                inc1 += 1
                            if set(l).issubset(set(T)) == True:
                                inc2 += 1
                        if 100*inc2/inc1 >= confidence:
                            for index in l:
                                if index not in s:
                                    m.append(index)
                           
                            print(" %d : %s ==> %s " %(num, s, m))
                            num += 1  

    generate_association_rules()   

    
   

def monumclick():
    labelText.set(' No of Days you want to Stay :')

    
    
        
    support = int(25)
    confidence = int(40)
   
    C1 = {}
    
    transactions = 0
    D = []
    T = []
    
    with open(r"C:\Users\Eswar\Desktop\Simpli_Learn\Internship\monuments.txt", "r") as f:
        for line in f:
            T = []
            transactions += 1
            for word in line.split():
                T.append(word)
                if word not in C1.keys():
                    C1[word] = 1
                else:
                    count = C1[word]
                    C1[word] = count + 1
            D.append(T)

    L1 = []
    for key in C1:
        if (100 * C1[key]/transactions) >= support:
            list = []
            list.append(key)
            L1.append(list)


    def apriori_gen(Lk_1, k):
        length = k
        Ck = [] 
        for list1 in Lk_1:
            for list2 in Lk_1:
                count = 0
                c = []
                if list1 != list2:
                    while count < length-1:
                        if list1[count] != list2[count]:
                            break
                        else:
                            count += 1
                    else:
                        if list1[length-1] < list2[length-1]:
                            for item in list1:
                                c.append(item)
                            c.append(list2[length-1])
                            if not has_infrequent_subset(c, Lk_1, k):
                                Ck.append(c) 
                                c = []
        return Ck


    def findsubsets(S,m):
        return set(itertools.combinations(S, m))


    def has_infrequent_subset(c, Lk_1, k):
        list = []
        list = findsubsets(c,k)
        for item in list: 
            s = []
            for l in item:
                s.append(l)
            s.sort()
            if s not in Lk_1:
                return True
        return False


    def frequent_itemsets():
        k = 2
        Lk_1 = []
        Lk = []
        L = []
        count = 0
        transactions = 0
        for item in L1:
            Lk_1.append(item)
        while Lk_1 != []:
            Ck = []
            Lk = []
            Ck = apriori_gen(Lk_1, k-1)

            for c in Ck:
                count = 0
                transactions = 0
                s = set(c)
                for T in D:
                    transactions += 1
                    t = set(T)
                    if s.issubset(t) == True:
                        count += 1
                if (100 * count/transactions) >= support:
                    c.sort()
                    Lk.append(c)
            Lk_1 = []

            for l in Lk:
                Lk_1.append(l)
            k += 1
            if Lk != []:
                L.append(Lk)
    
        return L
     

    def generate_association_rules():
        s = []
        r = []
        length = 0
        count = 1
        inc1 = 0
        inc2 = 0
        num = 1
        m = []
        L= frequent_itemsets()
       
        for list in L:
            for l in list:
                length = len(l)
                count = 1
                while count < length: 
                    s = []
                    r = findsubsets(l,count)
                    count += 1
                    for item in r:
                        inc1 = 0
                        inc2 = 0
                        s = []
                        m = []
                        for i in item:
                            s.append(i)
                        for T in D:
                            if set(s).issubset(set(T)) == True:
                                inc1 += 1
                            if set(l).issubset(set(T)) == True:
                                inc2 += 1
                        if 100*inc2/inc1 >= confidence:
                            for index in l:
                                if index not in s:
                                    m.append(index)
                            
                            print(" %d : %s ==> %s " %(num, s, m))
                            num += 1  

    generate_association_rules()   

    



root = Tk()

labelText = StringVar("")
labelText.set(' ')



label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)
#root.geometry('400x400')
root.configure(bg='green')
Label(root, text="Planning and Organizing travel and accomodation facility for you",bg='green',fg='white').pack()
Label(root, text="      ",bg='green').pack()
Label(root, text="please be patient",bg='green',fg='white').pack()
Label(root, text="      ",bg='green').pack()
Label(root, text="Tourists Reccomendations Portal",bg='green',fg='white').pack()
Label(root, text="      ",bg='green').pack()
Label(root, text= 'Destination')
Entry(root).pack()
Label(root, text="      ",bg='green').pack()
Label(root, text= 'Client Budget',bg='green', fg='white')
Entry(root).pack()
Label(root, text="      ",bg='green').pack()
Button(root, text="Travel", command=foodclick,bg='green',fg='white').pack()
#Entry(root).pack()
Label(root, text="      ",bg='green').pack()
Button(root, text="Accomodation", command=beachclick,bg='green',fg='white').pack()
#Entry(root).pack()
Label(root, text="      ",bg='green').pack()
Button(root, text="No of days stay", command=monumclick,bg='green',fg='white').pack()
#Entry(root).pack()
Label(root, text="     ",bg='green').pack()
#showScores = tk.Button(scores, text="Show scores", width=15, command=show)


label1 = Label(root, textvariable = labelText,bg='green')
label1.pack()


root.mainloop()