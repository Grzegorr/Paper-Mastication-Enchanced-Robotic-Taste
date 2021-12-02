#Load UR5 conroller
import UR5Controller.kg_robot as kgr

#Chewing Moves
import CookingMoves.ChewingMoves as CHEW

#Connecting the arm
print("------------Connection to the UR5-------------")
robot = kgr.kg_robot(port=30010, db_host="169.254.114.206") #This is the arm's IP, change last number with respect to ethernet IP number
print("----------------Arm Connected!-----------------\r\n")


#print(robot.getl())
CHEW.circle_chewing(robot, 5)






















