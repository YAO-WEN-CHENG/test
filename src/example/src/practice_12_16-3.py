#! /usr/bin/env python
import rospy

def list_tran(num):
    a=list(range(len(num)))
    for i in range(len(num)):
        num[i]=num[i]+30

number = [0,20,40]
list_tran(number)
print(number)