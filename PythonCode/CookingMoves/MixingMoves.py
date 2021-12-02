#Load in repository of mixing moves
import CookingMoves.GenericRobotMoves as GenericMoves

import numpy


#Grzegorz Sochacki - May 2021
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#                        This is a repository of moves used for mixing
#                    The movement usually starts at hight h above the container
#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#This movement is on a square with side length of 2r.
#The move starts h meters above the mixing position and in the center of the square
def zigzag_stir_scramble(robot, h, r):

    robot.movel_tool([0.5*r, 0.5*r, 0, 0, 0, 0])
    robot.movel_tool([0, 0, h, 0, 0, 0])

    robot.movel_tool([-r, 0, 0, 0, 0, 0])
    robot.movel_tool([r, -0.25 * r, 0, 0, 0, 0])
    robot.movel_tool([-r, 0, 0, 0, 0, 0])
    robot.movel_tool([r, -0.25 * r, 0, 0, 0, 0])
    robot.movel_tool([-r, 0, 0, 0, 0, 0])
    robot.movel_tool([r, -0.25 * r, 0, 0, 0, 0])
    robot.movel_tool([-r, 0, 0, 0, 0, 0])
    robot.movel_tool([r, -0.25 * r, 0, 0, 0, 0])

    robot.movel_tool([0, r, 0, 0, 0, 0])
    robot.movel_tool([-0.25 * r, -r, 0, 0, 0, 0])
    robot.movel_tool([0, r, 0, 0, 0, 0])
    robot.movel_tool([-0.25 * r, -r, 0, 0, 0, 0])
    robot.movel_tool([0, r, 0, 0, 0, 0])
    robot.movel_tool([-0.25 * r, -r, 0, 0, 0, 0])
    robot.movel_tool([0, r, 0, 0, 0, 0])
    robot.movel_tool([-0.25 * r, -r, 0, 0, 0, 0])

    robot.movel_tool([0.5 * r, 0.5 * r, 0, 0, 0, 0]) #back to the middle
    robot.movel_tool([0, 0, -h, 0, 0, 0])


#Same as zigzag_stir_scramble, but move to MIXING HOME automatically before it
def zigzag_stir_scramble_HOME(robot, h, r):
    GenericMoves.move_to_mixing_home(robot)

    robot.movel_tool([0.5*r, 0.5*r, 0, 0, 0, 0])
    robot.movel_tool([0, 0, h, 0, 0, 0])

    robot.movel_tool([-r, 0, 0, 0, 0, 0])
    robot.movel_tool([r, -0.25 * r, 0, 0, 0, 0])
    robot.movel_tool([-1.2*r, 0, 0, 0, 0, 0])
    robot.movel_tool([1.4*r, -0.25 * r, 0, 0, 0, 0])
    robot.movel_tool([-1.4*r, 0, 0, 0, 0, 0])
    robot.movel_tool([1.2*r, -0.25 * r, 0, 0, 0, 0])
    robot.movel_tool([-r, 0, 0, 0, 0, 0])
    robot.movel_tool([r, -0.25 * r, 0, 0, 0, 0])

    robot.movel_tool([0, r, 0, 0, 0, 0])
    robot.movel_tool([-0.25 * r, -r, 0, 0, 0, 0])
    robot.movel_tool([0, r, 0, 0, 0, 0])
    robot.movel_tool([-0.25 * r, -r, 0, 0, 0, 0])
    robot.movel_tool([0, r, 0, 0, 0, 0])
    robot.movel_tool([-0.25 * r, -r, 0, 0, 0, 0])
    robot.movel_tool([0, r, 0, 0, 0, 0])
    robot.movel_tool([-0.25 * r, -r, 0, 0, 0, 0])

    robot.movel_tool([0.5 * r, 0.5 * r, 0, 0, 0, 0]) #back to the middle
    robot.movel_tool([0, 0, -h, 0, 0, 0])


def stir_circle_standard(robot):
    stir_circle_relative(robot, 0.09, 0.125, 0.001, 0.30, 1.5)


#stirring home must in the middle of the circle, spatula edge along x direction
def stir_circle_relative(robot, radius, height, move_radius, move_vel, move_acc):

    #Take care of the robot wrist angle
    for k  in range(4):
        joints = robot.getj()
        if joints[5] > 0:
            robot.movel_tool([0,0,0,0,0,-3.14])
        if joints[5] < -3.14:
            robot.movel_tool([0,0,0,0,0,0.5*3.14])



    # get current positionfor a center of a circle
    stirring_home = robot.getl()

    #iterate over 18 angles along te circle
    for angle_number in range(18):
        if angle_number == 0:
            print("Move: Starting Point on Circle")

            #angle to radians
            angle = (2*3.14) * (angle_number/18)

            #convoluted way to move to first point - could be improved greatly
            x = radius * numpy.cos(angle)
            y = radius * numpy.sin(angle)
            new_pose = [sum(x) for x in zip(stirring_home, [x,y,0,0,0,0])]#its element wise addition
            robot.movel(new_pose)

            #Move toward inner part of circle
            #robot.movel_tool([0, 0, 0, 0, 0, 2 * 3.14 / 36])

            #tool down
            robot.translatel_rel([0, 0, -height, 0, 0, 0])
        else:
            #previous_angle = (2 * 3.14) * ((angle_number-1) / 18)
            #previous_x = radius * numpy.cos(previous_angle)
            #previous_y = radius * numpy.sin(previous_angle)
            #print("previous_x" + str(previous_x))
            #print("previous_y" + str(previous_y))
            #angle = (2 * 3.14) * (angle_number / 18)
            #x = radius * numpy.cos(angle)
            #y = radius * numpy.sin(angle)
            #print("x: " + str(x))
            #print("y: " + str(y))
            #x_diff = x - previous_x
            #y_diff = y - previous_y
            #print("x_diff: " + str(x_diff))
            #print("y_diff: " + str(y_diff))
            robot.movel_tool([0, 0.3*radius, 0, 0, 0, 2 * 3.14 / 18], vel = move_vel, acc = move_acc, radius = move_radius)
            #print(previous_angle - angle)
            #print()

    #lift the tool up
    robot.translatel_rel([0, 0, height, 0, 0, 0])

    joints = robot.getj()
    if joints[5] > 0:
        robot.movel_tool([0, 0, 0, 0, 0, -3.14])