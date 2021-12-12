#! /usr/bin/env python
import rospy

a='a','b','c'
b='d','e','f'


c=tuple(a)
print(c)

d=a+b
print("tuple a+tuple b = ",d)

e=a*3
print("tuple a*3=",e)

(A,B,C)=c
print(A)


tuple_1=(1,2,3,4,5,2,3,4,3,4,5)
count_n=tuple_1.count(2)
print("the count number of",2,"=",count_n)

dict_a={'a':'apple','b':'banana','c':'cat'}
dict_b=dict(A='APPLE',B='NAMAMA',C='CAT')
print("dict_a",dict_a)
print("dict_b",dict_b)

list_a=[['a',1],['b',2],['c',3]]
dict_c=dict(list_a)
print("list_a to dict = ",dict_c)

key_dict=dict.fromkeys(c,1)
print(key_dict)

dict_c['d']=4
print(dict_c)

dict_c.update({'e':'5'})
print(dict_c)

print(dict_c['a'])  #if not exist will getError
print(dict_c.get('a'))  #if not exist will print none
print(dict_c.get('g'))

dict_c.pop('a')
print(dict_c)

dict_c.clear()
print(dict_c)