#!/usr/bin/env python
# coding: utf-8

# Create the below pattern using nested for loop in Python.

# In[3]:


rows=int(input('Enter the number of rows'))

for i in range(0,rows):
    for j in range(0,i+1):
        if(i>=j):
            print('* ', end='')
    print('\n')
for i in range(rows,-1,-1):
    for j in range(0,i+1):
        if(i>=j):
            print('* ',end='')
    print('\n')


# Write a Python program to reverse a word after accepting the input from the user
# 

# In[6]:


str=input('Enter the word to be reversed')
print('The reversed word: ' + str[::-1])


# In[1]:





# In[ ]:




