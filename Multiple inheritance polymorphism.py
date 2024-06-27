#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Base1(object):
    def __init__(self):
        self.str1="Piyush"
        print("Base1 class")#because there is always one class
class Base2(object):
    def __init__(self):
        self.str2="Ahuja"
        print("Base2 Class")
class Derieved(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derieved class")
        
    def printastr(self):
        print(self.str1,self.str2)

ob=Derieved()
ob.printastr()


# In[10]:


#Base Class
class Grandfather:
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername

        
#Intermidiate class
class Father(Grandfather):
    def __init__(self,fathername,grandfathername):
        self.fathername=fathername
        
#invoking constructor of grandfather class
        Grandfather.__init__(self,grandfathername)

#derieved class

class Son(Father):
    def __init__(self,sonname,fathername,grandfathername):
        self.sonname=sonname
        #invoking constructor class
        Father.__init__(self,fathername,grandfathername)
        
    def print_name(self):
        print('Grandfathername:',self.grandfathername)
        print('Fathername:',self.fathername)
        print('Son name:',self.sonname)
        

obc=Son("Piyush","Hitesh","shashikant")
obc.print_name()


# In[16]:


#base class
class Parent:
    def func1(self):
        print("This is parent class")
#derieved class 1
class Child1(Parent):
    def func2(self):
        print("this is in child 1")
#Derieved class
class child2(Parent):
    def func3(self):
        print("This is in child 2")
obj1=Child1()
obj2=child2()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()


# In[19]:


#Polymorphism

class complex:
    def __init__(self,a,b):
        self.real=a
        self.img=b
        #adding two objects
    def __add__(self,Obj2):
        return self.real+Obj2.real, self.img+Obj2.img
Obj1=complex(1.5,2.5)
obj2=complex(2.2,3.3)
Obj3=Obj1+obj2
print(Obj3)


# In[30]:


class A:
    def __init__(self,a):
        self.a=a
    def __gt__(self,obj2):#gt is for greater than
        if(self.a>obj2.a):
            return True
        else:
            return False
obj1=A(42)
obj2=A(33)

if(obj1>obj2):
    print("Obj1 is greater")
else:
    print("Obj2 is greater")


# In[32]:


#Function overloading
class India():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("hindi is wiedly spoken")
    def type1(self):
        print("India Developing country")
class  USA():
    def capital(self):
        print('Washington,D.C')
    def language(self):
        print('English is widely spoken')
    def type1(self):
        print('Developed country')
        
ind=India()
usa=USA()
 
for i in(ind,usa):
    i.capital()
    i.language()
    i.type1()


# In[34]:


from math import pi
class shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass
class square(shape):
    def __init__(self,length):
        super().__init__("Square")
        self.length=length
    def area(self):
        return self.length**2

class circle(shape):
    def __init__(self,radius):
        super().__init__("circle")
        self.radius=radius
    def area(self):
        return pi*self.radius**2

a=square(4)
b=circle(5)
print(a.area())
print(b.area())


# In[ ]:




