#These usually need to be to run from the top directory for the path to work usually

import statistics as stats
import os
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def read_attempt(experiment_name, attempt_no):
    #arrays for the data
    Salinity_array = []
    Img_array = []

    n = 1  #standard starting point for measurements is 1
    while True:
        if not os.path.exists("Data/" + str(experiment_name) + "/Attempt_" + str(attempt_no) + "/" + str(n)):
            break
        n =  n + 1
    n = n - 1 # to subtract the last terted measurement
    print("There is "  + str(n) + " measurements in  this attempt.")

    #Loop over mesurements to read them in
    for d in range(n):
        img, data = read_measurement(experiment_name, attempt_no, d+1)
        Salinity_array.append(data)
        Img_array.append(img)
    return Salinity_array, Img_array


def read_measurement(experiment_name, attempt_no, measurement_number):
     data = np.load("Data/" + str(experiment_name) + "/Attempt_" + str(attempt_no) + "/" + str(measurement_number) + "/SalinityData.npy", allow_pickle=True)
     img = cv.imread("Data/" + str(experiment_name) + "/Attempt_" + str(attempt_no) + "/" + str(measurement_number) + "/PanImage.png")
     return img, data

def display_single_measurement(img, data):
    cv.imshow("Data", img)
    cv.waitKey(0)
    print("Salinity Measurements are:")
    print(data)

def display_all_measurements(img_arr, data_arr):
    for n in range(len(data_arr)):
        display_single_measurement(img_arr[n], data_arr[n])

def mean_and_variance(salinity_array, ifPrint):
    variances = []
    means = []
    for n in range(len(salinity_array)):
        variances.append(stats.variance(salinity_array[n]))
        means.append(stats.mean(salinity_array[n]))
    if ifPrint == True:
        print("Means: " + str(means))
        print("Variances: " + str(variances))
    return means, variances

def plot_means_vars(means, vars):
    plt.title("Salinity Mean and Variance")
    plt.plot(range(len(means)), means, color='r', marker='.', label="Mean")
    plt.plot(range(len(vars)), vars, color='b', marker='.', label="Variances")
    plt.xlabel("Number of Measurement")
    plt.ylabel("Conductance [mS]")
    plt.legend()
    #plt.savefig("saltVsTime.png")
    plt.show()
    plt.clf()


if __name__ == "__main__":
    read_attempt(experiment_name = "Eggs_With_Brush", attempt_no= 1, measurement_number=1)