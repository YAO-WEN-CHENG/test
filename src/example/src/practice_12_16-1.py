#! /usr/bin/env/python
import rospy


def welcome(name):
    print("hi,",name,"Good Morning")

welcome('everyone')

def interest(interest_type,subject):
    print("I like "+interest_type," activity")
    print("in",interest_type,"activity,My favorite is ",subject)

interest(interest_type='a',subject='volleyball')
interest(subject='volleyball',interest_type='a')