import time
import random
import math

#Load in repository of mixing moves
import CookingMoves.GenericRobotMoves as GenericMoves

#This is a function to sample solenity in a circle of raduis r, with no_sample number of samples
#The function will reset the current data stored in the SalinitySensor instance - so beware of losing data
def mass_salinity_test(robot, SALT, r, no_samples):
    GenericMoves.move_to_mixing_home(robot)
    SALT.resetData()
    # h1 - down to work from mixing home
    # h2 - down to pan
    # h3 - down to test eggs (dip movement)
    # h5 - up to brush
    h1 = 0.32
    h2 = 0.0945
    h3 = 0.024

    ##generating random testpoints
    #empty array for the points
    test_points = []
    for n in range(no_samples):
        #dummy values bigger then r for sure
        x = 100000
        y = 100000
        #randomly sampled from square - check if inside a circle
        while(math.sqrt(x*x + y*y) > r):
            x = random.uniform(0, 1) * r
            y = random.uniform(0, 1) * r
        point = [x, y]
        test_points.append(point)

    #print("Test points: " + str(test_points))

    #Move to mixing home, which is high enough for safe spatula rotation
    GenericMoves.move_to_mixing_home(robot)
    #rotate wrist - spatula up, sensor sown
    robot.movej_rel([0, 0, 0, 0, 3.14, 0])
    # go down to work area, two moves to make it more accurate
    robot.movel_tool([0, 0, -h1, 0, 0, 0], acc = 0.2)
    robot.movel_tool([0, 0, -h2, 0, 0, 0], acc = 0.1)
    print(robot.getl())

    #now sequence for every test point
    for test_point in test_points:
        #Make an offset from the middle of the pan
        robot.movel_tool([test_point[0], test_point[1], 0, 0, 0, 0], acc=0.2)
        #dip the sensor
        robot.movel_tool([0, 0, -h3, 0, 0, 0], acc=0.1)
        #sleep before measurement
        time.sleep(2)
        #Take measurement
        SALT.getNextReading()
        #Take the sensor up from eggs
        robot.movel_tool([0, 0, h3, 0, 0, 0], acc=0.2)
        #Sensor back to middle of the pan
        GenericMoves.move_to_sensor_above_eggs(robot)

    robot.movel_tool([0, 0, h2, 0, 0, 0], acc=0.2)
    robot.movel_tool([0, 0, h1, 0, 0, 0], acc=0.2)
    robot.movej_rel([0, 0, 0, 0, -3.14, 0])
    data = SALT.returnData()
    # print(data)
    GenericMoves.move_to_mixing_home(robot)
    return data

#Uses brush to clean up
def mass_salinity_test_brush(robot, SALT, r, no_samples):
    GenericMoves.move_to_mixing_home(robot)
    SALT.resetData()
    # h1 - down to work from mixing home
    # h2 - down to pan
    # h3 - down to test eggs (dip movement)
    # h5 - up to brush
    h1 = 0.32
    h2 = 0.0945
    h3 = 0.024
    h5 = 0.22

    ##generating random testpoints
    #empty array for the points
    test_points = []
    for n in range(no_samples):
        #dummy values bigger then r for sure
        x = 100000
        y = 100000
        #randomly sampled from square - check if inside a circle
        while(math.sqrt(x*x + y*y) > r):
            x = random.uniform(0, 1) * r
            y = random.uniform(0, 1) * r
        point = [x, y]
        test_points.append(point)

    #print("Test points: " + str(test_points))

    #Move to mixing home, which is high enough for safe spatula rotation
    GenericMoves.move_to_mixing_home(robot)
    #rotate wrist - spatula up, sensor sown
    robot.movej_rel([0, 0, 0, 0, 3.14, 0])
    # go down to work area, two moves to make it more accurate
    robot.movel_tool([0, 0, -h1, 0, 0, 0], acc = 0.2)
    robot.movel_tool([0, 0, -h2, 0, 0, 0], acc = 0.1)
    print(robot.getl())

    #now sequence for every test point
    for test_point in test_points:
        #Make an offset from the middle of the pan
        robot.movel_tool([test_point[0], test_point[1], 0, 0, 0, 0], acc=0.2)
        #dip the sensor
        robot.movel_tool([0, 0, -h3, 0, 0, 0], acc=0.1)
        #sleep before measurement
        time.sleep(2)
        #Take measurement
        SALT.getNextReading()
        #Take the sensor up from eggs
        robot.movel_tool([0, 0, h3, 0, 0, 0], acc=0.2)
        #Sensor back to middle of the pan
        GenericMoves.move_to_sensor_above_eggs(robot)

        # brush sequence
        robot.movel_tool([0, 0, h2, 0, 0, 0], acc=0.2)
        robot.movel_tool([0, 0, h5, 0, 0, 0], acc=0.2)
        robot.translatel_rel([0.05, -0.22, 0, 0, 0, 0])
        robot.translatel_rel([0.05, 0, 0, 0, 0, 0])
        robot.translatel_rel([-0.05, 0, 0, 0, 0, 0])
        robot.translatel_rel([-0.05, 0.22, 0, 0, 0, 0])
        robot.movel_tool([0, 0, -h5, 0, 0, 0], acc=0.2)
        GenericMoves.move_to_sensor_above_eggs(robot)

    robot.movel_tool([0, 0, h2, 0, 0, 0], acc=0.2)
    robot.movel_tool([0, 0, h1, 0, 0, 0], acc=0.2)
    robot.movej_rel([0, 0, 0, 0, -3.14, 0])
    data = SALT.returnData()
    # print(data)
    GenericMoves.move_to_mixing_home(robot)
    return data


#Adds the movement which shakes the eggs off the sensor after sampling
def mass_salinity_test_shakeoff(robot, SALT, r, no_samples):
    GenericMoves.move_to_mixing_home(robot)
    SALT.resetData()
    # h1 - down to work from mixing home
    # h2 - down to pan
    # h3 - down to test eggs (dip movement)
    h1 = 0.32
    h2 = 0.0945
    h3 = 0.024

    ##generating random testpoints
    #empty array for the points
    test_points = []
    for n in range(no_samples):
        #dummy values bigger then r for sure
        x = 100000
        y = 100000
        #randomly sampled from square - check if inside a circle
        while(math.sqrt(x*x + y*y) > r):
            x = random.uniform(0, 1) * r
            y = random.uniform(0, 1) * r
        point = [x, y]
        test_points.append(point)

    #print("Test points: " + str(test_points))

    #Move to mixing home, which is high enough for safe spatula rotation
    GenericMoves.move_to_mixing_home(robot)
    #rotate wrist - spatula up, sensor sown
    robot.movej_rel([0, 0, 0, 0, 3.14, 0])
    # go down to work area, two moves to make it more accurate
    robot.movel_tool([0, 0, -h1, 0, 0, 0], acc = 0.2)
    robot.movel_tool([0, 0, -h2, 0, 0, 0], acc = 0.1)
    #print(robot.getl())

    #now sequence for every test point
    for test_point in test_points:
        #Make an offset from the middle of the pan
        robot.movel_tool([test_point[0], test_point[1], 0, 0, 0, 0], acc=0.2)
        #dip the sensor
        robot.movel_tool([0, 0, -h3, 0, 0, 0], acc=0.1)
        #sleep before measurement
        time.sleep(2)
        #Take measurement
        SALT.getNextReading()
        #Take the sensor up from eggs
        robot.movel_tool([0, 0, h3, 0, 0, 0], acc=0.2)
        #Sensor back to middle of the pan
        GenericMoves.move_to_sensor_above_eggs(robot)

        #shake the eggs off
        robot.movel_tool([0, 0, 0.2, 0, 0, 0], acc=0.2, vel = 2)
        robot.movej_rel([0, 0, 0, 0, -3.14/1.4, 0], vel = 1.5)
        time.sleep(3)
        robot.movej_rel([0, 0, 0, 0, 3.14 /1.4, 0], vel = 1.5)
        GenericMoves.move_to_sensor_above_eggs(robot)
        GenericMoves.move_to_sensor_above_eggs(robot)

    robot.movel_tool([0, 0, h2, 0, 0, 0], acc=0.2)
    robot.movel_tool([0, 0, h1, 0, 0, 0], acc=0.2)
    robot.movej_rel([0, 0, 0, 0, -3.14, 0])
    data = SALT.returnData()
    # print(data)
    GenericMoves.move_to_mixing_home(robot)
    return data







