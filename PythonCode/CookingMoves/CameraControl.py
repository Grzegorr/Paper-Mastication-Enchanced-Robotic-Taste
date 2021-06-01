#openCV import
import cv2 as cv

#Load in repository of mixing moves
import CookingMoves.GenericRobotMoves as GenericMoves

def returnPanPicture(robot):
    GenericMoves.move_to_mixing_home(robot)
    # rotate wrist - spatula up, sensor down
    robot.movej_rel([0, 0, 0, 0, 3.14, 0])
    # go down
    robot.movel_tool([0, 0, -0.3, 0, 0, 0], acc=0.2)

    bool, img = return_picture()

    #reversing the moves
    robot.movel_tool([0, 0, 0.3, 0, 0, 0], acc=0.2)
    robot.movej_rel([0, 0, 0, 0, -3.14, 0])
    GenericMoves.move_to_mixing_home(robot)
    return img


#First return is success indicator 0/1
#2nd output is the frame itself
def return_picture():
    cam = cv.VideoCapture(0)  # 0 -> index of camera
    s, img = cam.read()
    if s:  # frame captured without any errors
        return 1, img
    else:
        print("Picture error!")
        return 0, 0

#Simple test will capture picture from camera
def camera_test():
    cam = cv.VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        cv.namedWindow("cam-test")
        cv.imshow("cam-test",img)
        cv.waitKey(0)
        cv.destroyWindow("cam-test")
        cv.imwrite("filename.jpg",img)

