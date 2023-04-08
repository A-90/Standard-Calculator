#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Welcome to my standard calculator")
a=float(input('what is your first number?'))
b=float(input('what is your secnd number?'))
c=input('what is our operator?+,-,*,/?')
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
else:
    print("Thanke you for using my standard calculator.")
    

