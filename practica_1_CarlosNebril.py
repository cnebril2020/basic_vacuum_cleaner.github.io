from GUI import GUI
from HAL import HAL
import rospy
import random

state = 1
v = 0
w = 2

def wait(n):
    HAL.setW(0)
    HAL.setV(0)
    rospy.sleep(n)
    

while True:
    global state, v, w

    # STATE 1: first spiral
    if (state == 1 and HAL.getBumperData().state == 0): 
        HAL.setV(v)
        HAL.setW(w)
        v += 0.01

    # STATE 2: random robot turn
    elif HAL.getBumperData().state == 1:
        state = 2
        wait(3)
        r = random.randint(0, 4)
        HAL.setW(2)
        rospy.sleep(r)
        wait(3)
        state = 3
   
    # STATE 3: move forward (if collides: state 2)
    elif state == 3:
        v = 3
        w = 0
        HAL.setV(v)
        HAL.setW(w)
        if HAL.getBumperData().state == 1:
            HAL.setV(0)
            HAL.setW(0)
            state = 2
