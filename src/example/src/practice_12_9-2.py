#! /usr/bin/env python
import rospy

account="iclab_xiao_ming"
print("account : iclab_xiao_ming")
password=input("enter your password")
if password !="aa":
    while(password!="aa"):
        print("your password is not correct")
        print("account : iclab_xiao_ming")
        password=input("enter your password")
        if password=="aa":
            print("welcome")
            break
else:
    print("welcome")

