import numpy as np
import os
from datetime import datetime

#openCV import
import cv2 as cv

#It is mainly used as a help function
def saveSingleEntry(ExperimentName, AttemptNumber, MeasurementNumber, PanImage, SalinityData):
    cv.imwrite("Data/" + str(ExperimentName) + "/Attempt_" + str(AttemptNumber) + "/" + str(MeasurementNumber) + "/PanImage.png", PanImage)
    np.save("Data/" + str(ExperimentName) + "/Attempt_" + str(AttemptNumber) + "/" + str(MeasurementNumber) + "/SalinityData.npy", SalinityData)

#Save next instance of data
#Starts with checks if infrastructure for the experiment exists
#Will not updte ReadMe after first creation - for updte you need to delete
def nextEntrySave(ExperimentName, AttemptNumber, PanImage, SalinityData, ReadMeString):
    #Check if overall "Data" directory exists
    if not(os.path.exists("Data")):
        os.mkdir("Data")

    #Check if experiment name exists
    if not(os.path.exists("Data/" + ExperimentName)):
        os.mkdir("Data/" + ExperimentName)

    # Check if experiment name exists
    if not (os.path.exists("Data/" + str(ExperimentName) + "/ReadMe.txt")):
        #current time
        now = datetime.now()
        #print(now)
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        text_file = open("Data/" + str(ExperimentName) + "/ReadMe.txt", "w")
        text_file.write("Experiment first run at " + date_time + "\n\n" + str(ReadMeString))
        text_file.close()

    # Check if file for the current attempt exists
    if not (os.path.exists("Data/" + str(ExperimentName) + "/Attempt_" + str(AttemptNumber))):
        os.mkdir("Data/" + str(ExperimentName) + "/Attempt_" + str(AttemptNumber))

    #Search for next measurement number which is not populated
    n = 1
    while True:
        if not (os.path.exists("Data/" + str(ExperimentName) + "/Attempt_" + str(AttemptNumber) + "/" + str(n))):
            os.mkdir("Data/" + str(ExperimentName) + "/Attempt_" + str(AttemptNumber) + "/" + str(n))
            break
        else:
            n = n + 1

    saveSingleEntry(ExperimentName, AttemptNumber=AttemptNumber, MeasurementNumber=n, PanImage=PanImage, SalinityData=SalinityData)






if __name__ == "__main__":
    nextEntrySave("Test", "Raz Dwa Trzy")