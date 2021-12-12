#! /usr/bin/env python
import rospy
import random

list_a = [0 for i in range (3)]

for i in range (3):
	if(i==0):
		list_a[i] = int(input("enter x"))
	elif(i==1):
		list_a[i] = int(input("enter y"))
	else:
		list_a[i] = int(input("enter z"))

list_a.sort()

print(list_a)