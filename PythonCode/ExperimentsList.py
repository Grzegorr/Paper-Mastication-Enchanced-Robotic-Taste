#Load in repository of mixing moves
import CookingMoves.MixingMoves as MIX

#Load a script containing various ways to sample the salinity
import CookingMoves.SalinitySamplingMoves as SALINITY_SAMPLING

#Load a script containing various ways to sample the salinity
import CookingMoves.CameraControl as CAM

#Functions to save data
import DataHandling.SavingExperimentData as DATA


def test_mix_picture_measure(robot, SALT):

    MIX.zigzag_stir_scramble_HOME(robot, 0.13, 0.12)
    salt_data = SALINITY_SAMPLING.mass_salinity_test(robot, SALT, r=0.08, no_samples=1)
    img = CAM.returnPanPicture(robot)
    DATA.nextEntrySave("Test2", 0, img, salt_data, "Hope it works!")

def first_actual_mixing(robot, SALT):
    n = 20  #no. of measurements
    m = 2   #mixes between measurement
    k = 1   #no. of attempts

    for attempt in range(k):
        for measurement in range(n):
            for mix in range(m):
                MIX.zigzag_stir_scramble_HOME(robot, 0.13, 0.12)
            salt_data = SALINITY_SAMPLING.mass_salinity_test(robot, SALT, r=0.08, no_samples=1)
            img = CAM.returnPanPicture(robot)
            DATA.nextEntrySave("First_Actual_Mixing", attempt, img, salt_data, "Two zigzag mixes between any next measurement")

def first_egg_mixing(robot, SALT):
    n = 50  #no. of measurements
    m = 2   #mixes between measurement
    k = 1   #attempt number

    for measurement in range(n):
        for mix in range(m):
            MIX.zigzag_stir_scramble_HOME(robot, 0.13, 0.12)
        salt_data = SALINITY_SAMPLING.mass_salinity_test(robot, SALT, r=0.08, no_samples=50)
        img = CAM.returnPanPicture(robot)
        DATA.nextEntrySave("First_Egg_Mixing", k, img, salt_data, "Two zigzag mixes between any next measurement, 6 Eggs")

