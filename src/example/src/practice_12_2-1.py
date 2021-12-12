#! /usr/bin/env python
import rospy
import random
list_a = [[[0 for i in range(3)]for j in range (3)]for k in range(3)]
print(list_a)


for i in range(3):
	for j in range(3):
		for k in range (3):
			list_a[i][j][k] = random.randint(0,255)

print(list_a)

for i in range(3):
	for j in range(3):		
		for k in range (3):
			if(list_a[i][j][k]<125):
				list_a[i][j][k]=0
			else:
				list_a[i][j][k]=1

print(list_a)
