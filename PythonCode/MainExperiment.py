#Load UR5 conroller
import UR5Controller.kg_robot as kgr

#Load salinity sensor
from SalinitySensor.SalinitySensor import SalinitySensor as salt_sensor

#Load in repository of mixing moves
import CookingMoves.MixingMoves as MIX

#Load a script containing various ways to sample the salinity
import CookingMoves.SalinitySamplingMoves as SALINITY_SAMPLING

#Load a script containing various ways to sample the salinity
import CookingMoves.CameraControl as CAM

import ExperimentsList as EXP

#Connecting the arm
print("------------Connection to the UR5-------------")
robot = kgr.kg_robot(port=30010, db_host="169.254.114.206") #This is the arm's IP, change last number with respect to ethernet IP number
print("----------------Arm Connected!-----------------\r\n")

#Preparing Salinity Sensor
SALT = salt_sensor(no_samples=50)

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#
#                             Experiments run below
#
#--------------------------------------------------------------------------------------------------------------------------------------------------------

### Choose Experiment

#Experiment = "First Tests"
#Experiment = "First Attempts on Mixing"
Experiment = "Initial Egg Data"



if Experiment == "First Tests":
    EXP.test_mix_picture_measure(robot=robot, SALT=SALT)

if Experiment == "First Attempts on Mixing":
    EXP.first_actual_mixing(robot=robot, SALT=SALT)

if Experiment == "Initial Egg Data":
    EXP.first_egg_mixing(robot=robot, SALT=SALT)







