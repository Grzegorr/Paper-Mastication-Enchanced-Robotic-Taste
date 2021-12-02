#These usually need to be to run from the top directory for the path to work usually

import statistics as stats
import os
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

from skimage.filters.rank import entropy
from skimage.morphology import disk
import skimage


def print_mean_and_variance(data):
    print(data)
    print(stats.mean(data))
    print(stats.variance(data))

def show_image(img):
    cv.imshow("Image", img)
    cv.waitKey(0)

def colour_img_entropy_map(img):
    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    cv.imshow("Image", img_gray)
    cv.waitKey(0)
    entr_img = entropy(img_gray, disk(100))
    entr_img = 10*entr_img
    entr_img = entr_img.astype(np.uint8)
    print(img_gray)
    cv.imshow("Image", entr_img)
    cv.waitKey(0)
    return entr_img

def colour_img_entropy(img):
    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    cv.imshow("Image", img_gray)
    cv.waitKey(0)
    entropy = skimage.measure.shannon_entropy(img_gray)
    #print(img_gray)
    return entropy

def colour_img_canny(img):
    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    #cv.imshow("Image", img_gray)
    #cv.waitKey(0)
    img_canny = cv.Canny(img_gray,30,200)

    return img_canny

def colour_img_fft(img):
    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    fft = np.fft.fft2(img_gray)
    fft = np.fft.fftshift(fft)
    #print(fft.shape[0])
    FFT = np.zeros((fft.shape[0], fft.shape[1]))
    FFT[:,:] = abs(fft[:,:])
    #print(np.amax(FFT))
    scaling = np.average(FFT)
    FFT = FFT * 0.4 / scaling
    #print(FFT)
    cv.imshow("Image", FFT)
    cv.waitKey(0)

def colour_img_fft_10(img_arr):
    # Figure Params
    fig = plt.figure(figsize=(80, 80))
    columns = 10
    rows = 2

    for i in range(10):
        img_gray = cv.cvtColor(img_arr[i], cv.COLOR_RGB2GRAY)
        fft = np.fft.fft2(img_gray)
        fft = np.fft.fftshift(fft)
        #print(fft.shape[0])
        FFT = np.zeros((fft.shape[0], fft.shape[1]))
        FFT[:,:] = abs(fft[:,:])
        #print(np.amax(FFT))
        scaling = np.average(FFT)
        FFT = FFT * 0.4/ scaling
        #FFT = FFT.astype(int)
        print(FFT)
        cv.imshow("Image", FFT)
        cv.waitKey(0)
        #Adding picture and information
        fig.add_subplot(rows, columns, i+1)
        #plt.annotate('Mean:' + str(stats.mean(data_arr[i]))[0:7], xy=(0.05, -0.4), xycoords='axes fraction')
        #plt.annotate('Variance:' + str(stats.variance(data_arr[i]))[0:7], xy=(0.05, -0.6), xycoords='axes fraction')
        plt.imshow(cv.cvtColor(img_arr[i], cv.COLOR_BGR2RGB))
        #Canny image and measures
        fig.add_subplot(rows, columns, i + 11)
        plt.imshow(FFT, cmap="gray")
        #plt.annotate('Canny count:' + str(count), xy=(0.05, -0.4), xycoords='axes fraction')
    plt.show()




def colour_img_canny_display_10(img_arr,data_arr):
    #Figure Params
    fig = plt.figure(figsize=(80, 80))
    columns = 10
    rows = 2

    #FOr later plots
    variances = np.zeros(10)
    canny = np.zeros(10)

    #Running for each of the measurements
    for i in range(10):
        #Compute canny
        img_gray = cv.cvtColor(img_arr[i], cv.COLOR_RGB2GRAY)
        img_canny = cv.Canny(img_gray,30,200)
        #Adding picture and information
        fig.add_subplot(rows, columns, i+1)
        plt.annotate('Mean:' + str(stats.mean(data_arr[i]))[0:7], xy=(0.05, -0.4), xycoords='axes fraction')
        plt.annotate('Variance:' + str(stats.variance(data_arr[i]))[0:7], xy=(0.05, -0.6), xycoords='axes fraction')
        plt.imshow(cv.cvtColor(img_arr[i], cv.COLOR_BGR2RGB))
        #Canny image and measures
        fig.add_subplot(rows, columns, i + 11)
        count = np.count_nonzero(img_canny == 255)
        plt.imshow(img_canny)
        plt.annotate('Canny count:' + str(count), xy=(0.05, -0.4), xycoords='axes fraction')
        #update date for a future plot
        variances[i] = stats.variance(data_arr[i])
        canny[i] = count
    plt.show()

    ##Adjusting to same axis
    n = variances[0]/canny[0]
    for t in range(len(variances)):
        canny[t] = canny[t] * n

    plt.title("No. mixes vs canny/sensor measurement")
    plt.plot(range(len(variances)), variances, color='r', marker='.', label="Conductance sensor")
    plt.plot(range(len(canny)), canny, color='b', marker='.', label="canny count")
    plt.xlabel("Number of Measurement")
    plt.ylabel("Adjusted Conductance/Canny count")
    plt.legend()
    # plt.savefig("saltVsTime.png")
    plt.show()
    plt.clf()




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