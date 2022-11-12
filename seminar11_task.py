#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sympy import *


# In[4]:


# 1 Определить корни

x = Symbol('x')
func=-5*x**2+10*x-150
y=solve(func)
x1=complex(y[0])
x2=complex(y[1])
print(x1,x2)


# In[6]:


# 2 Найти интервалы, на которых функция возрастает

fd=diff(func)
print(solve(0<fd))


# In[8]:


# 3 Найти интервалы, на которых функция убывает

print(solve(fd<0))


# In[10]:


# 4 Построить график

import matplotlib.pyplot as plt
list_y=[]
for i in range(-5,6):
    x=i
    y=-5*x**2+10*x-150
    list_y.append(y)
print(list_y)
plt.plot(range(-5,6),[0,0,0,0,0,0,0,0,0,0,0])
plt.plot(range(-5,6),list_y)


# In[12]:


# 5 Вычислить вершину

corni=solve(fd)
top=corni[0]
x=top
y=-5*x**2+10*x-150
print(top,y)


# In[14]:


# 6 Определить промежутки, на котором f > 0

solve(0<func)


# In[15]:


# 7 Определить промежутки, на котором f < 0

solve(func<0)

