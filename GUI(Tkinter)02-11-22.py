#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
top= Tk()
top.geometry("400x400")
top.title("1 st GUI application")
top.mainloop()


# In[3]:


from tkinter import *
top=Tk()
top.geometry("500x400")
top.title("Button")
redbutton=Button(top,text='red',fg='red')
redbutton.pack(side=LEFT)
bluebutton=Button(top,text='blue',fg='blue')
bluebutton.pack(side=RIGHT)
greenbutton=Button(top,text='green',fg='green')
greenbutton.pack(side=TOP)
blackbutton=Button(top,text='black',fg='black')
blackbutton.pack(side=BOTTOM)
top.mainloop()


# In[6]:


from tkinter import *
parent=Tk()
parent.geometry("300x300")
redbutton=Button(parent,text="Red",fg="red",width=5,height=5,bg="orange",activebackground='red')
redbutton.pack(side=LEFT)
blackbutton=Button(parent,text="Black",fg="black")
blackbutton.pack(side=RIGHT)
bluebutton=Button(parent,text="Blue",fg="blue")
bluebutton.pack(side=TOP)
greenbutton=Button(parent,text="Green",fg="green")
greenbutton.pack(side=BOTTOM)
parent.mainloop()


# In[1]:


from tkinter import *
top=Tk()#class impoorted from tkinter
top.geometry("400x250")
name=Label(top,text="Name")
name.place(x=30,y=50)
email=Label(top,text="email")
email.place(x=30,y=90)
password=Label(top,text="Password")
password.place(x=30,y=130)
e1=Entry(top)
e1.place(x=80,y=50)
e2=Entry(top)
e2.place(x=80,y=90)
e3=Entry(top)
e3.place(x=80,y=130)
b1=Button(top,text="Submit")
b1.place(x=200,y=200)
top.mainloop()#always


# In[ ]:





# In[ ]:





# In[24]:


from tkinter import messagebox
def fun1():
    messagebox.showinfo("Hello","Red button clicked")
def fun2():
    messagebox.showinfo("Hello","blue button clicked")
def fun3():
    messagebox.showinfo("Hello","green Button CLicked")
def fun4():
    messagebox.showinfo("Hello","Black Button Clicked")
from tkinter import *
parent=Tk()
parent.title("Button Demo")
parent.geometry("300x300")
redbutton= Button(parent, text='Red', fg='red',width=10,height=10,bg='yellow', activebackground="Blue",activeforeground='black',command=fun1)
redbutton.pack(side= LEFT)
greenbutton= Button(parent, text ='Black', fg='black',command=fun2)
greenbutton.pack(side=RIGHT)
bluebutton= Button(parent, text='Blue', fg='blue',command=fun3)
bluebutton.pack(side=TOP)
blackbutton= Button(parent, text='Green', fg='green',command=fun4)
blackbutton.pack(side=BOTTOM)
parent.mainloop()


# In[1]:


from tkinter import messagebox
def fun1():
    if checkvar1.get()==1:
        messagebox.showinfo("Hello", "C Programming selected")
    if checkvar1.get()==0:
        messagebox.showinfo("Unselected c Programme")
def fun2():
    if checkvar2.get()==1:
        messagebox.showinfo("hello","You have selected C++")
def fun3():
    if checkvar3.get()==1:
        messagebox.showinfo("Hello","Java selected")
from tkinter import *
top=Tk()
top.title("check button")
top.geometry("300x500")
checkvar1=IntVar()#Empty which can have only integer value
checkvar2=IntVar()
checkvar3=IntVar()
ckbtn1=Checkbutton(top,text='C',variable=checkvar1,onvalue=1,offvalue=0,width=10,height=2,command=fun1)#variable kisme store karege,onvalue when u select
ckbtn2=Checkbutton(top,text='C++',variable=checkvar2,onvalue=1,offvalue=0,width=10,height=2,command=fun2)
ckbtn3=Checkbutton(top,text='Java',variable=checkvar3,onvalue=1,offvalue=0,width=10,height=2,command=fun3)
ckbtn1.pack()
ckbtn2.pack()
ckbtn3.pack()#group into single window
top.mainloop()


# In[1]:


from tkinter import *
def sel():
    selection= "You have selected the option "+str(var.get())
    label.config(text=selection)#config will change as per the selection
top=Tk()
top.title("Radio Button ")
top.geometry("400x300")
var=IntVar()
R1=Radiobutton(top,text="Option1",variable=var,value=1,command=sel)
R1.pack()
R2=Radiobutton(top,text="Option2",variable=var,value=2,command=sel)
R2.pack()
R3=Radiobutton(top,text="Option3",variable=var,value=3,command=sel)
R3.pack()
label=Label(top)
label.pack()
top.mainloop()


# In[3]:


#Frame: Frame basically as container which contain different containt
#below we have created the frame and added different containt into it. that is btn 1 btn2
from tkinter import *
top=Tk()
top.geometry("400x300")
top.title("frame demo")
leftframe=Frame(top)#we created a frame at left side which as container i.e btn1 btn2
leftframe.pack(side=LEFT)
rightframe=Frame(top)
rightframe.pack(side=RIGHT)
btn1=Button(leftframe,text="Button1",fg='red',activebackground='red')
btn1.pack(side=LEFT)
btn2=Button(leftframe,text="Button2",fg='brown',activebackground='brown')
btn2.pack(side=LEFT)
btn3=Button(rightframe,text="Button3",fg='blue',activebackground='blue')
btn3.pack(side=RIGHT)
btn4=Button(rightframe,text="Button4",fg='white',activebackground='white')
btn4.pack(side=RIGHT)
top.mainloop()



# In[2]:


import tkinter as tk
from functools import partial
def add(n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    result=int(num1)+int(num2)
    label_result.config(text="Result = %d"%result)
    return
top=Tk()
top.geometry("400x300")
top.title('Caalculator')
number1=tk.StringVar()
number2=tk.StringVar()
labelnum1=tk.Label(top,text='A',fg='red')
labelnum1.grid(row=1,column=0)
labelnum2=tk.Label(top,text='B',fg='blue')
labelnum2.grid(row=2,column=0)
label_result=Label(top)
label_result.grid(row=7,column=2)
entrynum1=tk.Entry(top,textvariable=number1)#text variables retrie means when user enter it saves values in number 1
entrynum1.grid(row=1,column=2)
entrynum2=tk.Entry(top,textvariable=number2)#text variables retrie means when user enter it saves values in number 1
entrynum2.grid(row=2,column=2)
addition=partial(add,number1,number2)#partial is use to call fun and pass the parametr
btn=Button(top,text='Addition',command=addition)
btn.grid(row=3,column=0)
top.mainloop()


# ###### 
