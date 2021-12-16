#! /usr/bin/env python
import rospy

def subtract(x1,x2):
    return x1-x2

def addition(x1,x2):
    return x1+x2


print("1 : add")
print("2 : sub")

op=int(input("enter op (1/2) : "))
a=int(input("a : "))
b=int(input("b : "))

if op==1:
    print("a+b=",addition(a,b))
elif op==2:
    print("a-b=",subtract(a,b))
else:
    print("input error")