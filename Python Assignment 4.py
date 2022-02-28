#!/usr/bin/env python
# coding: utf-8

# ###### 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

# In[1]:


import math 
class len_of_sides:
    def __init__(self):
        self.a=int(input('Enter the a value'))
        self.b=int(input('Enter the a value'))
        self.c=int(input('Enter the a value'))
class area_of_triangle(len_of_sides):
    def __init__(self,*args):
        super(area_of_triangle,self).__init__(*args)
            
    def area(self):
        s=(self.a+self.b+self.c)/2
        area1=(s*(s-self.a)*(s-self.b)*(s-self.c))
        return(math.sqrt(area1))


# In[2]:


ob1=area_of_triangle()
ob1.area()


# Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.###### 

# In[15]:


def filter_long_words(l1,n):
    l2=[]
    for i in l1:
        if len(i)>n:
            l2.append(i)
    return l2
    


# In[17]:


filter_long_words(['my','dream','is','to','be','a','data','scientist'],5)


# ###### Function with *args keyword as parameter

# In[27]:


def filter_long_words_args(*args):
    l2=[]
    for i in args[0]:
        if len(i)>args[1]:
            l2.append(i)
    return l2
    


# In[28]:


filter_long_words_args(['my','dream','is','to','be','a','data','scientist'],3)


# 2.1 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.
# 2.2

# In[29]:


def count(l1):
    l2=[]
    for i in l1:
            l2.append(len(i))
    return l2
            


# In[30]:


count(['ineuron','Machine Learning','Deep Learning'])


# ###### using *args

# In[31]:


def count(*args):
    l2=[]
    for i in args[0]:
            l2.append(len(i))
    return l2
            


# In[32]:


count(['ineuron','Machine Learning','Deep Learning'])


# ###### `Write a Python function which takes a character (i.e. a string of length 1) and returns True if
# it is a vowel, False otherwise.
# NOTE:

# In[49]:


def Vowel_check(char):
    if char in ['a','e','i','o','u','A','E','I','O','U']:
        return True
    else :
        return False


# In[50]:


Vowel_check('a')


# In[35]:


Vowel_check('z')


# In[ ]:




