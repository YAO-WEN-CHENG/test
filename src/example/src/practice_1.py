#! /usr/bin/env python

import rospy

rospy.init_node("practice_python_node")

kilometers_to_centimeters=7*1000*100
time_spent = (kilometers_to_centimeters//0.123)*60
rospy.loginfo(time_spent)

Avengers_End_Game = "I love you 3000"

s=len(Avengers_End_Game)
s1 = len(Avengers_End_Game[1:])
s2 = len(Avengers_End_Game[:-1])
s3 = len(Avengers_End_Game[1:-1])

rospy.loginfo(str(s) +' '+ str(  Avengers_End_Game))
rospy.loginfo(str(s1)+' '+ str(  Avengers_End_Game[1:]))
rospy.loginfo(str(s2)+' '+ str(  Avengers_End_Game[:-1]))
rospy.loginfo(str(s3)+' '+ str(  Avengers_End_Game[1:-1]))


