import time
import random
import math
import numpy as np

#Load in repository of generic moves
import CookingMoves.GenericRobotMoves as GenericMoves

#This is a function to sample solenity in a circle of raduis r, with no_sample number of samples
#The function will reset the current data stored in the SalinitySensor instance - so beware of losing data
# if_retract_more - if set to "True", the probe will go extra 1/3 of h2 up.
def simple_chewing(robot, chew_number):
    GenericMoves.move_to_chewing_home(robot)
    # h1 - down to work from mixing home
    # h2 - down to pan
    # h3 - down to test eggs (dip movement)
    # h5 - up to brush
    h1 = 0.14
    h2 = 0.015

    for i in range(chew_number):
        #Move to mixing home, which is high enough for safe spatula rotation
        GenericMoves.move_to_chewing_home(robot)
        # go down to work area, two moves to make it more accurate
        robot.movel_tool([0, 0, h1, 0, 0, 0], acc = 0.2)
        robot.movel_tool([0, 0, h2, 0, 0, 0], acc=0.1)
        time.sleep(0.2)
        robot.movel_tool([0, 0, -h1, 0, 0, 0], acc=0.2)
        GenericMoves.move_to_chewing_home(robot)


def standard_chewing(robot, chew_number):
    val = 0.025
    points = [
        [0,0],
        [val, 0],
        [-val, 0],
        [0, val],
        [0, -val],

    ]

    GenericMoves.move_to_chewing_home(robot)
    # h1 - down to work from mixing home
    # h2 - down to pan
    # h3 - down to test eggs (dip movement)
    # h5 - up to brush
    h1 = 0.13
    h2 = 0.025

    for i in range(chew_number):
        #Move to mixing home, which is high enough for safe spatula rotation
        GenericMoves.move_to_chewing_home(robot)
        #move round the pot
        point_no = i%5
        robot.translatel_rel([points[point_no][0], points[point_no][1], 0, 0, 0, 0], acc = 0.1)

        # go down to work area, two moves to make it more accurate
        robot.movel_tool([0, 0, h1, 0, 0, 0], acc = 0.2)
        robot.movel_tool([0, 0, h2, 0, 0, 0], acc=0.1)
        time.sleep(0.2)
        robot.movel_tool([0, 0, -h1, 0, 0, 0], acc=0.2)
        GenericMoves.move_to_chewing_home(robot)

def circle_chewing(robot, chew_number):
    val = 0.025
    points = [
        [0, 0],
        [val, 0],
        [-val, 0],
        [0, val],
        [0, -val],
        [0, 0]
    ]

    GenericMoves.move_to_chewing_home(robot)
    # h1 - down to work from mixing home
    # h2 - down to pan
    # h3 - down to test eggs (dip movement)
    # h5 - up to brush
    h1 = 0.14
    h2 = 0.015

    for i in range(chew_number):
        #Move to mixing home, which is high enough for safe spatula rotation
        GenericMoves.move_to_chewing_home(robot)
        # go down to work area, two moves to make it more accurate
        robot.movel_tool([0, 0, h1, 0, 0, 0], acc = 0.2)
        robot.movel_tool([0, 0, h2, 0, 0, 0], acc=0.1)
        time.sleep(0.2)
        middle_pose = robot.getl()
        for j in range(len(points)):
            pose = middle_pose.copy()
            pose[0] = pose[0] + points[j][0]
            pose[1] = pose[1] + points[j][1]
            robot.movel(pose, vel = 1)

        robot.movel_tool([0, 0, -h1, 0, 0, 0], acc=0.2)
        GenericMoves.move_to_chewing_home(robot)



