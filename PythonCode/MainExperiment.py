import UR5Controller.kg_robot as kgr
from SalinitySensor.SalinitySensor import SalinitySensor as salt_sensor

#Connecting the arm
print("------------Connection to the UR5-------------")
robot = kgr.kg_robot(port=30010, db_host="169.254.114.206") #This is the arm's IP, change last number with respect to ethernet IP number
print("----------------Arm Connected!-----------------\r\n")

#Preparing Salinity Sensor
SALT = salt_sensor(no_samples=5)

#robot.home()
SALT.return_next_reading()