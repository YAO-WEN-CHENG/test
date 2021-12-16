#! /usr/bin/env python
from types import MemberDescriptorType
import rospy

def build_member(name,gender,tel):
    member = {'name':name,'gender':gender}
    if tel:
        member['tel']=tel
    return member

member_name = input("enter your name")
member_gender = input("enter your gender")
member_tel = input("enter your phone number")

print(build_member(member_name,member_gender,member_tel))