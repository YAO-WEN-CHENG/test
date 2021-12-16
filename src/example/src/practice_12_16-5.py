#! /usr/bin/env python
import rospy


def control():
    print("1 : forword")
    print("0 : not forword")
    forword = int(input("enter forword or not(1/0)"))
    angle = int(input("enter now the angle compare with road"))
    min = 45
    max = 135
    dict_status={'forword':forword,'angle':angle}
    print(dict_status)
    return dict_status

status=control()
if(status['forword']):
    if(status['angle']>135):
        print("turn left")
    elif(status['angle']<45):
        print("turn right")
    else:
        print("forword")

else:
    print("stop")



