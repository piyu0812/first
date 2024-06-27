#!/usr/bin/env python
# coding: utf-8

# In[3]:


#numpy support dimension 0-n the elemnets in 0 dimensional array are called as scalars
import numpy as np
a=np.array(42)
print(a)
print(a.ndim)


# In[9]:


#1-D array
# An array that has 0D arrays 
arr=np.array([1,2,3])
print(arr)
print(arr.ndim)


# In[5]:


#2D: An array that has 1D arrays as its elements is called 2D array. they are often use to represent a matrix or second order tensors.
ar=np.array([[1,2,3],[4,5,6]])
print(ar)
print(ar.ndim)


# In[8]:


#3D An array that has 2 D array as its element it is called as 3 D 
A=np.array([[[1,2,3,4]],[[5,6,7,8]]])
print(A)
print(A.ndim)


# In[10]:


# Numpy arrays provides an attribute ndim that returns the integer  thaat convience how many dimensons the array have 
print(arr.ndim)
print(ar.ndim)
print(A.ndim)


# In[11]:


# Write a progrram to create 0D 1D 2D 3d numpy arrays and check their dimensions
a=np.array(32)
print(a)
print(a.ndim)


# In[12]:


b=np.array([32,4,5])
print(b)
print(b.ndim)


# In[13]:


c=np.array([[32,6,7],[5,4,3]])
print(c)
print(c.ndim)


# In[14]:


d=np.array([[[32,4,5]]])
print(d)
print(d.ndim)


# In[15]:


q=np.array([[[[2,3,4]]]])
print(q)
print(q.ndim)


# In[2]:


#create an array withb 5 dimensions and print the dimensions of the array cretaed 
import numpy as np
a=np.array([[[[[1,2,3,4]]]]])
print(a)
print(a.ndim)


# In[7]:


#another method
arr=np.array([1,2,3,4],ndmin=5)
print(arr)
print(arr.ndim)
#in te given array the innermost dimension i.e 5 as four elements. the 4th dimensions as  vector the 3rd dimension as  one elements which is matrix holding a vector the second dimension has one element i.e 3d array and the 1 st dimensions has one element wwhich is a 4d array


# In[8]:


# Numpy array indexing
# Array indexing is use to acess the array elements by refering the elements to its index number. the indexes in numpy starts with 0 value.
a=np.array([1,2,3])
print(a)
print(a[0])


# In[10]:


print(a[0]+a[2])


# In[12]:


# Aess the elemment on the 1 st row second column of a 2d array and 2nd row and 5 th column in the same column for performing addition operation over it
a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a)
print(a.ndim)


# In[21]:


print(a[0,1])
print(a[1,4])
print(a[0,1]+a[1,4])


# In[23]:


# To acess a elements from a 3d array we can use comma seperated integers representing the dimensions and the index of the element
arr=np.array([[[1,2,3,4,5]],[[6,7,8,9,10]]])
print(arr)
print(arr.ndim)


# In[1]:


print(arr[0,2])


# In[1]:


# Negative indexing using numpy we can acess the elementr of array from the ened

#write a program to print the last element from a 2D array using negative indexing;
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print(a.ndim)


# In[8]:


print(a[-1,-1])
print(a[0:1,1:3])#0:1 so it takes only 0 row and 1: 3 so it takes 1 2


# In[2]:


#Slicing in python is a concept of picking elements from a given indeex to another index
#syntax: [Start: End]
#Steps: Steps are used to jump over for certain number of elements while slicing out or performing slicing operations over a given nd array
#Syntax for performing over  2 d array {start:end,start:end:Steps}

#the default data types in python are strings integer float boolean and compllex. The data type supported in numpy is denoted by single character 
# i-integer
#b-boolean
#u-unsigned
#f-float 
#c- complex
# m-time data 
#O- object, S-string,U-unicode,V-void

#Create an array with a data ttype string 
import numpy as np
arr=np.array([1,2,3,4],dtype='S')
print(arr)


# In[3]:


print(arr.dtype)


# In[2]:


#create a numpy array or strig and print its data type
a=np.array(['apple','banana','Tnmayad'])
print(a)
print(a.dtype)


# In[3]:


#Creating an data type with 4 byte interger
A=np.array(['a','b','c','d'],dtype='i')
print(A)
print(A.dtype)


# In[ ]:


#astype function create a copy of the array and allows the user to specify the data type as the parameter 
#This method is used to change the data type of an existing array and allows   to convert the data type of the content

