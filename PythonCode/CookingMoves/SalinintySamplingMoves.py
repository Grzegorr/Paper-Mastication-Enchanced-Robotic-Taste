#This is a function to sample solenity in a circle of raduis r, with no_sample number of samples
def mass_salinity_test(robot, SALT):
    move_to_mixing_home(robot)
    SALT.resetData()
    # h1 - down to work
    # h2 - down to pan
    # h3 - down to test eggs
    # h4 - dip into water
    # h5 - up to brush
    h1 = 0.32
    h2 = 0.0945
    h3 = 0.025
    h4 = 0.062
    h5 = 0.22

    offsets = [
        #[0.05, 0.05]
        [-0.06, -0.05], [-0.04, -0.05], [-0.02, -0.05], [0, -0.05], [0.02, -0.05], [0.04, -0.05], [0.06, -0.05]
    ]

    move_to_mixing_home(robot)
    robot.movej_rel([0, 0, 0, 0, 3.14, 0])
    # go down to work area
    #input("Syopped")
    robot.movel_tool([0, 0, -h1, 0, 0, 0], acc = 0.2)

    for offset in offsets:
        # test sequence start
        robot.movel_tool([0, 0, -h2, 0, 0, 0], acc = 0.2)
        robot.movel_tool([offset[0], offset[1], 0, 0, 0, 0], acc = 0.2)
        robot.movel_tool([0, 0, -h3, 0, 0, 0], acc = 0.2)
        #########
        time.sleep(1)
        for i in range(10):
            SALT.getNextReading()
            robot.translatel_rel([0, 0, 0.01, 0, 0, 0])
            robot.movel_tool([0, abs(offset[1])/9.0, 0, 0, 0, 0])
            robot.translatel_rel([0, 0, -0.01, 0, 0, 0])

        #########
        robot.movel_tool([0, 0, h3, 0, 0, 0], acc = 0.2)
        robot.movel_tool([0, -2 * 5.0 / 9.0 * abs(offset[1]), 0, 0, 0, 0], acc = 0.2)
        robot.movel_tool([-offset[0], -offset[1], 0, 0, 0, 0], acc = 0.2)
        robot.movel_tool([0, 0, h2, 0, 0, 0], acc = 0.2)
        # brush
        robot.movel_tool([0, 0, h5, 0, 0, 0], acc = 0.2)
        robot.translatel_rel([0.05, -0.22, 0, 0, 0, 0])
        robot.translatel_rel([-0.05, 0.22, 0, 0, 0, 0])
        move_to_mixing_sensor_down_home(robot)
        robot.movel_tool([0, 0, -h1, 0, 0, 0])

    robot.movel_tool([0, 0, h2, 0, 0, 0], acc = 0.2)
    robot.movel_tool([0, 0, h1, 0, 0, 0], acc = 0.2)
    robot.movej_rel([0, 0, 0, 0, -3.14, 0])
    data = SALT.returnData()
    # print(data)
    move_to_mixing_home(robot)
    return data