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
