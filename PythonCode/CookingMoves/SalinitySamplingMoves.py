import time
import random
import math
import numpy as np
import time

#Load in repository of mixing moves
import CookingMoves.GenericRobotMoves as GenericMoves

# This is a function to sample solenity in a circle of raduis r, with no_sample number of samples
# The function will reset the current data stored in the SalinitySensor instance - so beware of losing data
# if_retract_more - if set to "True", the probe will go extra 1/3 of h2 up.
# if_plate is False by default , if set to diffenrt string it lower a slightle less
def mass_salinity_test(robot, SALT, r, no_samples, if_retract_more = "False", if_plate = "False"):
    GenericMoves.move_to_mixing_home(robot)
    SALT.resetData()
    # h1 - down to work from mixing home
    # h2 - down to pan
    # h3 - down to test eggs (dip movement)
    # h5 - up to brush
    h1 = 0.32
    h2 = 0.0945
    h3 = 0.02

    # plate adjustment
    if if_plate != "False":
        h2 = h2 - 0.005

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
        #make the x,y both positive and negative
        coin = random.randint(0, 3)
        if coin == 0:
            x=x
            y=y
        if coin == 1:
            x=-x
            y=y
        if coin == 2:
            x=-x
            y=-y
        if coin == 3:
            x=x
            y=-y
        point = [x, y]
        test_points.append(point)

    print("Test points: " + str(test_points))

    #Move to mixing home, which is high enough for safe spatula rotation
    GenericMoves.move_to_mixing_home(robot)
    #rotate wrist - spatula up, sensor sown
    robot.movej_rel([0, 0, 0, 0, 3.14, 0])
    # go down to work area, two moves to make it more accurate
    robot.movel_tool([0, 0, -h1, 0, 0, 0], acc = 0.2)
    if if_retract_more == "False":
        robot.movel_tool([0, 0, -h2, 0, 0, 0], acc = 0.1)
    else:
        robot.movel_tool([0, 0, -2*h2/3, 0, 0, 0], acc=0.1)
    print(robot.getl())

    #now sequence for every test point
    for test_point in test_points:
        #Make an offset from the middle of the pan
        robot.movel_tool([test_point[0], test_point[1], 0, 0, 0, 0], acc=0.2)
        #dip the sensor
        if if_retract_more == "False":
            robot.movel_tool([0, 0, -h3, 0, 0, 0], acc=0.1)
        else:
            robot.movel_tool([0, 0, -h2 / 3, 0, 0, 0], acc=0.1)
            robot.movel_tool([0, 0, -h3, 0, 0, 0], acc=0.1)

        #sleep before measurement
        time.sleep(2)
        #Take measurement
        SALT.getNextReading()
        #Take the sensor up from eggs
        if if_retract_more == "False":
            robot.movel_tool([0, 0, h3, 0, 0, 0], acc=0.1)
            # Sensor back to middle of the pan
            GenericMoves.move_to_sensor_above_eggs(robot)
        else:
            robot.movel_tool([0, 0, h3, 0, 0, 0], acc=0.1)
            robot.movel_tool([0, 0, h2 / 3, 0, 0, 0], acc=0.1)
            # Sensor back to middle of the pan
            GenericMoves.move_to_sensor_above_eggs_high(robot)


    if if_retract_more == "False":
        robot.movel_tool([0, 0, h2, 0, 0, 0], acc=0.2)
    else:
        robot.movel_tool([0, 0, 2*h2/3, 0, 0, 0], acc=0.2)

    robot.movel_tool([0, 0, h1, 0, 0, 0], acc=0.2)
    robot.movej_rel([0, 0, 0, 0, -3.14, 0])
    data = SALT.returnData()
    # print(data)
    GenericMoves.move_to_mixing_home(robot)
    return data

def mask_for_actually_measured_values(radius, no_samples, radius_ratio = 1.0):
    test_points = []
    for n in range(no_samples):
        sq_side_in_samples = np.sqrt(no_samples)
        sample_grid_side = 2*radius/sq_side_in_samples
        print("Sample grid Size: " + str(sample_grid_side))
        starting_point_x = - radius + sample_grid_side/2.0 # takes into account that sampling point should be in the middle of sampling square
        print("Starting Point X: " + str(starting_point_x))
        starting_point_y = starting_point_x
        print("Starting Point X: " + str(starting_point_y))

        # adjust x
        x = starting_point_x + (n % sq_side_in_samples) * sample_grid_side
        # adjust y
        y = starting_point_y + (n // sq_side_in_samples) * sample_grid_side


        #Curde adjustment to make the map fit with a picture
        x = -x
        y = -y

        point = [x, y]
        #print("Point: " + str(point))
        test_points.append(point)

        mask = []
        # now sequence for every test point
        for test_point in test_points:
            #print("Current Test Point: " + str(starting_point_x))
            x = test_point[0]
            y = test_point[1]
            if x * x + y * y > radius * radius * radius_ratio *radius_ratio:
                mask.append(0)
            else:
                mask.append(1)

    return mask



# Works same as mass_salinity_test, but it now samples in a grid-like pattern. the grid is a square of side sqrt(no_samples). samples outside a circle are set to 0
# hight set for paper plate
def mass_salinity_test_mapping(robot, SALT, radius, no_samples, if_retract_more = "False", if_plate = "False"):
    GenericMoves.move_to_mixing_home(robot)
    SALT.resetData()
    # h1 - down to work from mixing home
    # h2 - down to pan
    # h3 - down to test eggs (dip movement)
    # h5 - up to brush
    h1 = 0.32
    h2 = 0.0974
    h3 = 0.02

    # plate adjustment
    if if_plate != "False":
        h2 = h2 - 0.005

    # Check if the required square size is an intager
    if np.sqrt(no_samples) % 1 != 0:
        print("The number of samples requested is not a square of an intager - fix that!")
        return

    ##generating testpoints
    #empty array for the points
    test_points = []
    for n in range(no_samples):
        sq_side_in_samples = np.sqrt(no_samples)
        sample_grid_side = 2*radius/sq_side_in_samples
        print("Sample grid Size: " + str(sample_grid_side))
        starting_point_x = - radius + sample_grid_side/2.0 # takes into account that sampling point should be in the middle of sampling square
        print("Starting Point X: " + str(starting_point_x))
        starting_point_y = starting_point_x
        print("Starting Point X: " + str(starting_point_y))

        # adjust x
        x = starting_point_x + (n % sq_side_in_samples) * sample_grid_side
        # adjust y
        y = starting_point_y + (n // sq_side_in_samples) * sample_grid_side


        #Curde adjustment to make the map fit with a picture
        x = -x
        y = -y

        point = [x, y]
        #print("Point: " + str(point))
        test_points.append(point)

    print("Test points: " + str(test_points))

    #Move to mixing home, which is high enough for safe spatula rotation
    GenericMoves.move_to_mixing_home(robot)
    #rotate wrist - spatula up, sensor sown
    robot.movej_rel([0, 0, 0, 0, 3.14, 0])
    # go down to work area, two moves to make it more accurate
    robot.movel_tool([0, 0, -h1, 0, 0, 0], acc = 0.2)
    if if_retract_more == "False":
        #robot.movel_tool([0, 0, -h2, 0, 0, 0], acc = 0.1)
        GenericMoves.move_to_sensor_above_eggs(robot)
    else:
        #robot.movel_tool([0, 0, -2*h2/3, 0, 0, 0], acc=0.1)
        GenericMoves.move_to_sensor_above_eggs_high(robot)
    print(robot.getl())

    #now sequence for every test point
    counter = 0
    start = time.time()
    for test_point in test_points:
        print("Points done: " + str(counter) + "/" + str(len(test_points)) + ".")
        end = time.time()
        print("Time elapsed: " + str(end - start) + " seconds.")
        counter = counter + 1
        #print("Current Test Point: " + str(starting_point_x))
        x = test_point[0]
        y = test_point[1]
        if x * x + y * y > radius * radius:
            SALT.getNextReading()

        else:
            #Make an offset from the middle of the pan
            robot.movel_tool([test_point[0], test_point[1], 0, 0, 0, 0], acc=0.2)
            #dip the sensor
            if if_retract_more == "False":
                robot.movel_tool([0, 0, -h3, 0, 0, 0], acc=0.1)
            else:
                robot.movel_tool([0, 0, -h2 / 3, 0, 0, 0], acc=0.1)
                robot.movel_tool([0, 0, -h3, 0, 0, 0], acc=0.1)

            #sleep before measurement
            time.sleep(2)
            #Take measurement
            SALT.getNextReading()
            #Take the sensor up from eggs
            if if_retract_more == "False":
                robot.movel_tool([0, 0, h3, 0, 0, 0], acc=0.1)
                # Sensor back to middle of the pan
                GenericMoves.move_to_sensor_above_eggs(robot)
            else:
                robot.movel_tool([0, 0, h3, 0, 0, 0], acc=0.1)
                robot.movel_tool([0, 0, h2 / 3, 0, 0, 0], acc=0.1)
                # Sensor back to middle of the pan
                GenericMoves.move_to_sensor_above_eggs_high(robot)


    if if_retract_more == "False":
        robot.movel_tool([0, 0, h2, 0, 0, 0], acc=0.2)
    else:
        robot.movel_tool([0, 0, 2*h2/3, 0, 0, 0], acc=0.2)

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

if __name__ == '__main__':
    mask = mask_for_actually_measured_values(0.09, 400)


