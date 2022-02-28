#!/usr/bin/env python
# coding: utf-8

# ###### 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[16]:


list1=list(range(2000,3200))
list2=[]
for i in list1:
    if (i % 7==0) & (i%5!=0):
        list2.append(i)
print(list2)  


# ######  2. Write a Python program to accept the user's first and last name and then getting them and printed in the the reverse order with a space between first name and last name.

# In[19]:


First_Name=input('Enter your first name')
Last_Name=input('Enter your Last name')

print(First_Name[::-1]+' '+Last_Name[::-1])


# 3. Write a Python program to find the volume of a sphere with diameter 12 cm

# In[18]:


import math 
Dia=12
radius=Dia/2
volume= (4/3)* math.pi *(radius*radius*radius)
print('The Volume of Sphere is '+ str(volume))


# In[ ]:





# In[ ]:





# In[ ]:




