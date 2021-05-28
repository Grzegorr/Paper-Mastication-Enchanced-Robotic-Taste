#openCV import
import cv2 as cv

#Load UR5 conroller
import UR5Controller.kg_robot as kgr

#Load salinity sensor
from SalinitySensor.SalinitySensor import SalinitySensor as salt_sensor

#Load in repository of mixing moves
import CookingMoves.MixingMoves as MIX

#Connecting the arm
print("------------Connection to the UR5-------------")
robot = kgr.kg_robot(port=30010, db_host="169.254.114.206") #This is the arm's IP, change last number with respect to ethernet IP number
print("----------------Arm Connected!-----------------\r\n")

#Preparing Salinity Sensor
SALT = salt_sensor(no_samples=5)


cam = cv.VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    cv.namedWindow("cam-test")
    cv.imshow("cam-test",img)
    cv.waitKey(0)
    cv.destroyWindow("cam-test")
    cv.imwrite("filename.jpg",img)




robot.home()
MIX.zigzag_stir_scramble(robot, 0.01, 0.15)


robot.home()
SALT.return_next_reading()