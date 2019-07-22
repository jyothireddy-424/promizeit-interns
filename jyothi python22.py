#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#find Roots of Quadratic Equations AX2+BX+C=0
from math import sqrt
print("Quadratic function : (a * x^2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
r = b**2 - 4*a*c
if r > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(r))/(2*a))     
    x2 = (((-b) - sqrt(r))/(2*a))
    print("There are 2 roots: %f and %f" % (x1, x2))
elif r == 0:
    num_roots = 1
    x = (-b) / 2*a
    print("There is one root: ", x)
else:
    num_roots = 0
    print("No roots, discriminant < 0.")
    exit()


# In[ ]:


#find all the divisor of a number
x = 10 
i = 1
while i<x:
    if x%i == 0:
        print('divisor',i)
        i= i + 1


# In[ ]:




