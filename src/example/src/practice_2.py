#! /usr/bin/env python

from time import sleep

t=int(1)

while t<=10:
  if t==10:
    sleep(1)
    print("Time's up")
    t+=1
  elif t<10:
    sleep(1)
    print(t)
    t+=1
