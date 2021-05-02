# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 00:50:42 2021

@author: Amol
"""

class SMS:
    def __init__(self,item,cost,number):
        self.cost=cost
        self.number=number
        self.item=item
        
    def display(self):
        print(self.item)
        print(self.cost)
        print(self.number)
        
     
    def get(self):
        self.item=input('Enter the item name')
        self.cost=int(input('Enter cost'))
        self.number=int(input('Enter number of _'))
        

       
def choose(arr):
    
    print('1. Manager\n')
    print('2. Customer\n')
    x=int(input('Choose one of the above'))
    
    if x==1:
        if CheckPass():
            print('1. Cost Change\n')
            print('2. Restock\n')
            print('3. View item details\n')
            print('4. Change Password\n')
            y=int(input('Choose one of the above'))
            
            if y==1:
                CostChange(arr)
            elif y==2:
                Restock(arr)
            elif y==3:
                getDetails(arr)
            elif y==4:
                ChangePass()
            else:
                print('Not a valid option')
        else:
            print('Wrong password')
            
            
    elif x==2:
        
        print('1. Get details of the items\n')
        print('2. Buy the item\n')
        y=int(input('Choose one of the above'))
        
        if y==1:
            getDetails(arr)
        elif y==2:
            number(arr)
            
def assign():
    
    arr=[]
    
    pen=SMS('Pen',20,100)
    arr.append(pen)
    
    pencil=SMS('Pencil',2,100)
    arr.append(pencil)
    
    book=SMS('Notebook',30,100)
    arr.append(book)
    
    eraser=SMS('Eraser',5,100)
    arr.append(eraser)
    
    return(arr)
    
def CostChange(array):
    
    print('Welcome to cost change operation\n')
    
    for i in range(4):
        print(i+1,array[i].item)
    
    x=int(input('Choose one of the above'))
    if x==1:
        print('Your old cost is '+str(array[0].cost))
        y=int(input('Enter new cost'))
        array[0].cost=y
    elif x==2:
        print('your old cost is '+str(array[1].cost))
        y=int(input('Enter new cost'))
        array[1].cost=y
    elif x==3:
        print('your old cost is '+str(array[2].cost))
        y=int(input('Enter new cost'))
        array[2].cost=y
    elif x==4:
        print('your old cost is '+str(array[3].cost))
        y=int(input('Enter new cost'))
        array[3].cost=y
        
    print('\nCost Updated')
        
def Restock(array):
    print('Welcome to restock operations')
    
    for i in range(4):
        print(i+1,array[i].item)
        
    x=int(input('Choose one of the above'))
    if x==1:
        print('your old stock is '+str(array[0].number))
        y=int(input('Enter new additions'))
        array[0].number=array[0].number+y
    elif x==2:
        print('your old stock is '+str(array[1].number))
        y=int(input('Enter new additions'))
        array[1].number=array[1].number+y
    elif x==3:
        print('your old stock is '+str(array[2].number))
        y=int(input('Enter new additions'))
        array[2].number=array[2].number+y
    elif x==4:
        print('your old stock is '+str(array[3].number))
        y=int(input('Enter new additions'))
        array[3].number=array[3].number+y
        
    print('\nStock updated')
    

def getDetails(array):
    
    for i in range(4):
        array[i].display()

        
def number(array):
    
    for i in range(4):
        print(i+1,array[i].item)
        
    x=int(input('Choose one of the above'))
    if x==1:
        y=int(input('How many do you want?'))
        if y>10 and y<=array[1].number:
            print('Congratulations you have qualified for 10% discount')
            cost=0.9*array[0].cost*y
            array[0].number=array[0].number-y
        elif y>array[0].number:
            print('This much Stock is not available')
        else:
            cost=array[0].cost*y
            array[0].number=array[0].number-y
    elif x==2:
        y=int(input('How many do you want?'))
        if y>10 and y<=array[1].number:
            print('Congratulations you have qualified for 10% discount')
            cost=0.9*array[1].cost*y
            array[1].number=array[1].number-y
        elif y>array[1].number:
            print('This much Stock is not available')
        else:
            cost=array[1].cost*y
            array[1].number=array[1].number-y
    elif x==3:
        y=int(input('How many do you want?'))
        if y>10 and y<=array[2].number:
            print('Congratulations you have qualified for 10% discount')
            cost=0.9*array[2].cost*y
            array[2].number=array[2].number-y
        elif y>array[2].number:
            print('This much Stock is not available')
        else:
            cost=array[2].cost*y
            array[2].number=array[2].number-y
    elif x==4:
        y=int(input('How many do you want?'))
        if y>10 and y<=array[3].number:
            print('Congratulations you have qualified for 10% discount')
            cost=0.9*array[3].cost*y
            array[3].number=array[3].number-y
        elif y>array[1].number:
            print('This much Stock is not available')
        else:
            cost=array[3].cost*y
            array[3].number=array[3].number-y
        
    print('Your final cost is '+ str(cost+12.5))
    
def CheckPass():
    
    f=open('password.txt','r')
    P=f.read()
    passw=input('Enter password ')
    if passw==P:
        return True
    else:
        print('wrong password')
        return False   
    f.close()

def RecheckPass():
    f=open('password.txt','r')
    P=f.read()
    passw=input('Enter current password ')
    if passw==P:
        return True
    else:
        print('wrong password')
        return False   
    f.close()

def ChangePass():
    if RecheckPass():
        SetPasss()
        
def SetPasss():
    passwordd=input('Enter new password')
    f=open('password.txt','w')
    f.write(passwordd)
    f.close()
    
def SetPass():
    passwordd='1qaz2wsx3edc'
    f=open('password.txt','w')
    f.write(passwordd)
    f.close()
    
print('Welcome to Stationary Management System')
SetPass()
ign=assign()
x=1
while x!=0:
    choose(ign)
    a=input('Do you want to continue?(y/n)')
    if a=='n':
        x=0