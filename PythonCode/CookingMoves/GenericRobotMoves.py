#Load UR5 conroller
import UR5Controller.waypoints as wp

#Mixing home is over top left hob, high enough, so spatula does not colide with anything on the stove
def move_to_mixing_home(robot):
    robot.movel(wp.mixing_home_l)
    print("Move: Mixing Home")

#Moves to chewing-ready position - same as onl mixing atm
def move_to_chewing_home(robot):
    robot.movel(wp.chewing_home_l)
    print("Move: Chewing Home")

#It is mixing_home but with wrist twisted in a way spatula is up and sensor down
def move_to_mixing_sensor_down_home(robot):
    robot.movel(wp.mixing_sensor_down_home_l)
    print("Move: Sensor Down")


#It places the sensor above the eggs - middle of the pan
def move_to_sensor_above_eggs(robot):
    robot.movel(wp.sensing_above_the_eggs)
    #print("Move: Sensor Above the eggs")

#It places the sensor above the eggs - middle of the pan
def move_to_sensor_above_eggs_high(robot):
    robot.movel(wp.sensing_above_the_eggs_high)
    print("Move: Sensor Above the eggs")