import statistics
import matplotlib.pyplot as plt
import numpy as np

import DataHandling.DataReadAndPreprocess as DATA
import CookingMoves.SalinitySamplingMoves as SALT


#######################################################
#              CONTROL INPUTS                         #
#######################################################
if_print_water_added = "True"
if_mask = "True"
#These are numbered as in the repo
first = 1
second = 2
third = 3


#######################################################
#          SINGLE ATTEMPT ANALYSIS                    #
#######################################################
#Salinity_array, Img_array = DATA.read_attempt(experiment_name = "ResistanceSpreadingMaps", attempt_no = 1)
#Salinity_array, Img_array = DATA.read_attempt(experiment_name = "Maps", attempt_no = 1)
Salinity_array, Img_array = DATA.read_attempt(experiment_name = "Accurate_Tests", attempt_no = 3)
print(Salinity_array)



##ADJUSTMENT FOR PYTHON INDEXING ONLY
first = first -1
second = second -1
third = third -1


if if_mask == "True":
    mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=0.9)
    for i in [first,second,third]:
        dummy = []
        for j in range(len(Salinity_array[i])):
            if mask[j] == 1:
                dummy.append(Salinity_array[i][j])
        Salinity_array[i] = dummy


mean_unmixed = statistics.mean(Salinity_array[first])
print(mean_unmixed)
variance_unmixed = statistics.variance(Salinity_array[first])
print(variance_unmixed)

mean_half_mixed = statistics.mean(Salinity_array[second])
print(mean_half_mixed)
variance_half_mixed = statistics.variance(Salinity_array[second])
print(variance_half_mixed)


mean_fully_mixed = statistics.mean(Salinity_array[third])
print(mean_fully_mixed)
variance_fully_mixed = statistics.variance(Salinity_array[third])
print(variance_fully_mixed)


x = ["unmixed", "half-mixed", "fully-mixed"]
y = [mean_unmixed, mean_half_mixed, mean_fully_mixed]
y2 = [variance_unmixed, variance_half_mixed, variance_fully_mixed]
fig, ax = plt.subplots()
ax.plot(x, y, label = "Mean")
ax.plot(x, y2, label = "Variance")
ax.set(xlabel='Mixing Stage', ylabel='Conductance (mS)', title='Effects of Mixing on the Conductance Measurements')
ax.grid()
ax.legend()
fig.savefig("test.png")
plt.show()



N = 3
w = 0.3
ind = np.arange(N)

plt.style.use('ggplot')
x = np.array(range(len(Salinity_array[first])))
y = sorted(Salinity_array[first])
plt.bar(x-w, y, width = w, color='red', label = "unmixed")
x = np.array(range(len(Salinity_array[second])))
y = sorted(Salinity_array[second])
plt.bar(x, y, width = w, color='blue', label = "slightly mixed")
x = np.array(range(len(Salinity_array[third])))
y = sorted(Salinity_array[third])
plt.bar(x+w, y, width = w, color='black', label = "full mixed")
plt.xlabel("Measurement Number")
plt.ylabel("Conductance(mS/cm)")
plt.title("Bar Plot of Conductance Measurements Sorted in Ascending Order")
plt.xticks(x, x)
plt.legend(loc='best')
plt.show()




#######################################################
#                  HISTOGRAMS                         #
#######################################################
color = 'red'

x = Salinity_array[first]
y = Salinity_array[second]
z = Salinity_array[third]

figure2, (ax1, ax2, ax3) = plt.subplots(3, 1)

bins = np.linspace(0, 15, 100)
ax1.hist(x, bins, label="unmixed", color = color)
ax1.set_ylim([0, 100])
ax1.set_xlabel("Conductance(mS/cm)")
ax1.set_ylabel("Frequency")
ax1.set_title("Histogram of conductance measurements")
ax1.legend(loc='upper right')
#plt.show()

bins = np.linspace(0, 15, 100)
ax2.hist(y, bins, label="slightly mixed", color = color)
ax2.set_ylim([0, 100])
ax2.set_xlabel("Conductance(mS/cm)")
ax2.set_ylabel("Frequency")
ax2.set_title("Histogram of conductance measurements")
ax2.legend(loc='upper right')
#plt.show()

bins = np.linspace(0, 15, 100)
ax3.hist(z, bins, label="mixed", color = color)
ax3.set_ylim([0, 100])
ax3.set_xlabel("Conductance(mS/cm)")
ax3.set_ylabel("Frequency")
ax3.set_title("Histogram of conductance measurements")
ax3.legend(loc='upper right')
figure2.subplots_adjust(hspace=0.5)
figure2.set_size_inches(5, 8)
plt.show()












##########################################################################
#                     ALL DISHES THREE STATES                            #
##########################################################################

if True:
    Salinity_array, Img_array = DATA.read_attempt(experiment_name="Accurate_Tests", attempt_no=1)
    # Salinity_array, Img_array = DATA.read_attempt(experiment_name = "Maps", attempt_no = 1)
    first = 1
    second = 2
    third = 3
    if_mask = "True"

    ##ADJUSTMENT FOR PYTHON INDEXING ONLY
    first = first - 1
    second = second - 1
    third = third - 1

    if if_mask == "True":
        mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=1)
        for i in [first, second, third]:
            dummy = []
            for j in range(len(Salinity_array[i])):
                if mask[j] == 1:
                    dummy.append(Salinity_array[i][j])
            Salinity_array[i] = dummy

    mean_unmixed = statistics.mean(Salinity_array[first])
    print(mean_unmixed)
    variance_unmixed = statistics.variance(Salinity_array[first])
    print(variance_unmixed)
    median_unmixed = statistics.median(Salinity_array[first])
    print(median_unmixed)

    mean_half_mixed = statistics.mean(Salinity_array[second])
    print(mean_half_mixed)
    variance_half_mixed = statistics.variance(Salinity_array[second])
    print(variance_half_mixed)
    median_half_mixed = statistics.median(Salinity_array[second])
    print(median_half_mixed)

    mean_fully_mixed = statistics.mean(Salinity_array[third])
    print(mean_fully_mixed)
    variance_fully_mixed = statistics.variance(Salinity_array[third])
    print(variance_fully_mixed)
    median_fully_mixed = statistics.median(Salinity_array[third])
    print(median_fully_mixed)

    x = ["unmixed", "half-mixed", "fully-mixed"]
    y1 = [mean_unmixed, mean_half_mixed, mean_fully_mixed]
    y1_1 = [median_unmixed, median_half_mixed, median_fully_mixed]
    y2 = [variance_unmixed, variance_half_mixed, variance_fully_mixed]

#################################################
    Salinity_array, Img_array = DATA.read_attempt(experiment_name="Accurate_Tests", attempt_no=2)
    first = 1
    second = 2
    third = 3
    if_mask = "True"

    ##ADJUSTMENT FOR PYTHON INDEXING ONLY
    first = first - 1
    second = second - 1
    third = third - 1

    if if_mask == "True":
        mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=1)
        for i in [first, second, third]:
            dummy = []
            for j in range(len(Salinity_array[i])):
                if mask[j] == 1:
                    dummy.append(Salinity_array[i][j])
            Salinity_array[i] = dummy

    mean_unmixed = statistics.mean(Salinity_array[first])
    print(mean_unmixed)
    variance_unmixed = statistics.variance(Salinity_array[first])
    print(variance_unmixed)
    median_unmixed = statistics.median(Salinity_array[first])
    print(median_unmixed)

    mean_half_mixed = statistics.mean(Salinity_array[second])
    print(mean_half_mixed)
    variance_half_mixed = statistics.variance(Salinity_array[second])
    print(variance_half_mixed)
    median_half_mixed = statistics.median(Salinity_array[second])
    print(median_half_mixed)

    mean_fully_mixed = statistics.mean(Salinity_array[third])
    print(mean_fully_mixed)
    variance_fully_mixed = statistics.variance(Salinity_array[third])
    print(variance_fully_mixed)
    median_fully_mixed = statistics.median(Salinity_array[third])
    print(median_fully_mixed)

    x = ["unmixed", "half-mixed", "fully-mixed"]
    y3 = [mean_unmixed, mean_half_mixed, mean_fully_mixed]
    y3_1 = [median_unmixed, median_half_mixed, median_fully_mixed]
    y4 = [variance_unmixed, variance_half_mixed, variance_fully_mixed]

    #################################################
    Salinity_array, Img_array = DATA.read_attempt(experiment_name="Accurate_Tests", attempt_no=3)
    first = 1
    second = 2
    third = 3
    if_mask = "True"

    ##ADJUSTMENT FOR PYTHON INDEXING ONLY
    first = first - 1
    second = second - 1
    third = third - 1

    if if_mask == "True":
        mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=1)
        for i in [first, second, third]:
            dummy = []
            for j in range(len(Salinity_array[i])):
                if mask[j] == 1:
                    dummy.append(Salinity_array[i][j])
            Salinity_array[i] = dummy

    mean_unmixed = statistics.mean(Salinity_array[first])
    print(mean_unmixed)
    variance_unmixed = statistics.variance(Salinity_array[first])
    print(variance_unmixed)
    median_unmixed = statistics.median(Salinity_array[first])
    print(median_unmixed)

    mean_half_mixed = statistics.mean(Salinity_array[second])
    print(mean_half_mixed)
    variance_half_mixed = statistics.variance(Salinity_array[second])
    print(variance_half_mixed)
    median_half_mixed = statistics.median(Salinity_array[second])
    print(median_half_mixed)

    mean_fully_mixed = statistics.mean(Salinity_array[third])
    print(mean_fully_mixed)
    variance_fully_mixed = statistics.variance(Salinity_array[third])
    print(variance_fully_mixed)
    median_fully_mixed = statistics.median(Salinity_array[third])
    print(median_fully_mixed)

    x = ["unmixed", "half-mixed", "fully-mixed"]
    y5 = [mean_unmixed, mean_half_mixed, mean_fully_mixed]
    y5_1 = [median_unmixed, median_half_mixed, median_fully_mixed]
    y6 = [variance_unmixed, variance_half_mixed, variance_fully_mixed]



    #################################################
    Salinity_array, Img_array = DATA.read_attempt(experiment_name="Accurate_Tests", attempt_no=4)
    first = 1
    second = 2
    third = 3
    if_mask = "True"

    ##ADJUSTMENT FOR PYTHON INDEXING ONLY
    first = first - 1
    second = second - 1
    third = third - 1

    if if_mask == "True":
        mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=1)
        for i in [first, second, third]:
            dummy = []
            for j in range(len(Salinity_array[i])):
                if mask[j] == 1:
                    dummy.append(Salinity_array[i][j])
            Salinity_array[i] = dummy

    mean_unmixed = statistics.mean(Salinity_array[first])
    print(mean_unmixed)
    variance_unmixed = statistics.variance(Salinity_array[first])
    print(variance_unmixed)
    median_unmixed = statistics.median(Salinity_array[first])
    print(median_unmixed)

    mean_half_mixed = statistics.mean(Salinity_array[second])
    print(mean_half_mixed)
    variance_half_mixed = statistics.variance(Salinity_array[second])
    print(variance_half_mixed)
    median_half_mixed = statistics.median(Salinity_array[second])
    print(median_half_mixed)

    mean_fully_mixed = statistics.mean(Salinity_array[third])
    print(mean_fully_mixed)
    variance_fully_mixed = statistics.variance(Salinity_array[third])
    print(variance_fully_mixed)
    median_fully_mixed = statistics.median(Salinity_array[third])
    print(median_fully_mixed)

    x = ["unmixed", "half-mixed", "fully-mixed"]
    y7 = [mean_unmixed, mean_half_mixed, mean_fully_mixed]
    y7_1 = [median_unmixed, median_half_mixed, median_fully_mixed]
    y8 = [variance_unmixed, variance_half_mixed, variance_fully_mixed]




    #################################################
    Salinity_array, Img_array = DATA.read_attempt(experiment_name="Accurate_Tests", attempt_no=5)
    first = 1
    second = 2
    third = 3
    if_mask = "True"

    ##ADJUSTMENT FOR PYTHON INDEXING ONLY
    first = first - 1
    second = second - 1
    third = third - 1

    if if_mask == "True":
        mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=1)
        for i in [first, second, third]:
            dummy = []
            for j in range(len(Salinity_array[i])):
                if mask[j] == 1:
                    dummy.append(Salinity_array[i][j])
            Salinity_array[i] = dummy

    mean_unmixed = statistics.mean(Salinity_array[first])
    print(mean_unmixed)
    variance_unmixed = statistics.variance(Salinity_array[first])
    print(variance_unmixed)
    median_unmixed = statistics.median(Salinity_array[first])
    print(median_unmixed)

    mean_half_mixed = statistics.mean(Salinity_array[second])
    print(mean_half_mixed)
    variance_half_mixed = statistics.variance(Salinity_array[second])
    print(variance_half_mixed)
    median_half_mixed = statistics.median(Salinity_array[second])
    print(median_half_mixed)

    mean_fully_mixed = statistics.mean(Salinity_array[third])
    print(mean_fully_mixed)
    variance_fully_mixed = statistics.variance(Salinity_array[third])
    print(variance_fully_mixed)
    median_fully_mixed = statistics.median(Salinity_array[third])
    print(median_fully_mixed)

    x = ["unmixed", "half-mixed", "fully-mixed"]
    y9 = [mean_unmixed, mean_half_mixed, mean_fully_mixed]
    y9_1 = [median_unmixed, median_half_mixed, median_fully_mixed]
    y10 = [variance_unmixed, variance_half_mixed, variance_fully_mixed]




    #################################################
    Salinity_array, Img_array = DATA.read_attempt(experiment_name="Accurate_Tests", attempt_no=6)
    first = 1
    second = 2
    third = 3
    if_mask = "True"

    ##ADJUSTMENT FOR PYTHON INDEXING ONLY
    first = first - 1
    second = second - 1
    third = third - 1

    if if_mask == "True":
        mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=1)
        for i in [first, second, third]:
            dummy = []
            for j in range(len(Salinity_array[i])):
                if mask[j] == 1:
                    dummy.append(Salinity_array[i][j])
            Salinity_array[i] = dummy

    mean_unmixed = statistics.mean(Salinity_array[first])
    print(mean_unmixed)
    variance_unmixed = statistics.variance(Salinity_array[first])
    print(variance_unmixed)
    median_unmixed = statistics.median(Salinity_array[first])
    print(median_unmixed)

    mean_half_mixed = statistics.mean(Salinity_array[second])
    print(mean_half_mixed)
    variance_half_mixed = statistics.variance(Salinity_array[second])
    print(variance_half_mixed)
    median_half_mixed = statistics.median(Salinity_array[second])
    print(median_half_mixed)

    mean_fully_mixed = statistics.mean(Salinity_array[third])
    print(mean_fully_mixed)
    variance_fully_mixed = statistics.variance(Salinity_array[third])
    print(variance_fully_mixed)
    median_fully_mixed = statistics.median(Salinity_array[third])
    print(median_fully_mixed)

    x = ["unmixed", "half-mixed", "fully-mixed"]
    y11 = [mean_unmixed, mean_half_mixed, mean_fully_mixed]
    y11_1 = [median_unmixed, median_half_mixed, median_fully_mixed]
    y12 = [variance_unmixed, variance_half_mixed, variance_fully_mixed]

    #################################################
    Salinity_array, Img_array = DATA.read_attempt(experiment_name="Accurate_Tests", attempt_no=7)
    first = 1
    second = 2
    third = 3
    if_mask = "True"

    ##ADJUSTMENT FOR PYTHON INDEXING ONLY
    first = first - 1
    second = second - 1
    third = third - 1

    if if_mask == "True":
        mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=1)
        for i in [first, second, third]:
            dummy = []
            for j in range(len(Salinity_array[i])):
                if mask[j] == 1:
                    dummy.append(Salinity_array[i][j])
            Salinity_array[i] = dummy

    mean_unmixed = statistics.mean(Salinity_array[first])
    print(mean_unmixed)
    variance_unmixed = statistics.variance(Salinity_array[first])
    print(variance_unmixed)
    median_unmixed = statistics.median(Salinity_array[first])
    print(median_unmixed)

    mean_half_mixed = statistics.mean(Salinity_array[second])
    print(mean_half_mixed)
    variance_half_mixed = statistics.variance(Salinity_array[second])
    print(variance_half_mixed)
    median_half_mixed = statistics.median(Salinity_array[second])
    print(median_half_mixed)

    mean_fully_mixed = statistics.mean(Salinity_array[third])
    print(mean_fully_mixed)
    variance_fully_mixed = statistics.variance(Salinity_array[third])
    print(variance_fully_mixed)
    median_fully_mixed = statistics.median(Salinity_array[third])
    print(median_fully_mixed)

    x = ["unmixed", "half-mixed", "fully-mixed"]
    y13 = [mean_unmixed, mean_half_mixed, mean_fully_mixed]
    y13_1 = [median_unmixed, median_half_mixed, median_fully_mixed]
    y14 = [variance_unmixed, variance_half_mixed, variance_fully_mixed]





    #################################################
    Salinity_array, Img_array = DATA.read_attempt(experiment_name="Accurate_Tests", attempt_no=8)
    first = 1
    second = 2
    third = 3
    if_mask = "True"

    ##ADJUSTMENT FOR PYTHON INDEXING ONLY
    first = first - 1
    second = second - 1
    third = third - 1

    if if_mask == "True":
        mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=1)
        for i in [first, second, third]:
            dummy = []
            for j in range(len(Salinity_array[i])):
                if mask[j] == 1:
                    dummy.append(Salinity_array[i][j])
            Salinity_array[i] = dummy

    mean_unmixed = statistics.mean(Salinity_array[first])
    print(mean_unmixed)
    variance_unmixed = statistics.variance(Salinity_array[first])
    print(variance_unmixed)
    median_unmixed = statistics.median(Salinity_array[first])
    print(median_unmixed)

    mean_half_mixed = statistics.mean(Salinity_array[second])
    print(mean_half_mixed)
    variance_half_mixed = statistics.variance(Salinity_array[second])
    print(variance_half_mixed)
    median_half_mixed = statistics.median(Salinity_array[second])
    print(median_half_mixed)

    mean_fully_mixed = statistics.mean(Salinity_array[third])
    print(mean_fully_mixed)
    variance_fully_mixed = statistics.variance(Salinity_array[third])
    print(variance_fully_mixed)
    median_fully_mixed = statistics.median(Salinity_array[third])
    print(median_fully_mixed)

    x = ["unmixed", "half-mixed", "fully-mixed"]
    y15 = [mean_unmixed, mean_half_mixed, mean_fully_mixed]
    y15_1 = [median_unmixed, median_half_mixed, median_fully_mixed]
    y16 = [variance_unmixed, variance_half_mixed, variance_fully_mixed]

    #################################################
    Salinity_array, Img_array = DATA.read_attempt(experiment_name="Accurate_Tests", attempt_no=9)
    first = 1
    second = 2
    third = 3
    if_mask = "True"

    ##ADJUSTMENT FOR PYTHON INDEXING ONLY
    first = first - 1
    second = second - 1
    third = third - 1

    if if_mask == "True":
        mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=1)
        for i in [first, second, third]:
            dummy = []
            for j in range(len(Salinity_array[i])):
                if mask[j] == 1:
                    dummy.append(Salinity_array[i][j])
            Salinity_array[i] = dummy

    mean_unmixed = statistics.mean(Salinity_array[first])
    print(mean_unmixed)
    variance_unmixed = statistics.variance(Salinity_array[first])
    print(variance_unmixed)
    median_unmixed = statistics.median(Salinity_array[first])
    print(median_unmixed)

    mean_half_mixed = statistics.mean(Salinity_array[second])
    print(mean_half_mixed)
    variance_half_mixed = statistics.variance(Salinity_array[second])
    print(variance_half_mixed)
    median_half_mixed = statistics.median(Salinity_array[second])
    print(median_half_mixed)

    mean_fully_mixed = statistics.mean(Salinity_array[third])
    print(mean_fully_mixed)
    variance_fully_mixed = statistics.variance(Salinity_array[third])
    print(variance_fully_mixed)
    median_fully_mixed = statistics.median(Salinity_array[third])
    print(median_fully_mixed)

    x = ["unmixed", "half-mixed", "fully-mixed"]
    y17 = [mean_unmixed, mean_half_mixed, mean_fully_mixed]
    y17_1 = [median_unmixed, median_half_mixed, median_fully_mixed]
    y18 = [variance_unmixed, variance_half_mixed, variance_fully_mixed]





    fig, ax = plt.subplots()
    ax.plot(x, y1, label = "No additives - mean", color = "green", marker = "v")
    #ax.plot(x, y1_1, label="No additives - median", color="green", marker="v", linestyle = "--")
    ax.plot(x, y2, label = "No additives - variance", color = "green", marker = "o", linestyle = "dotted")

    ax.plot(x, y3, label = "3 tomatoes - mean", color = "red", marker = "v")
    #ax.plot(x, y3_1, label="3 tomatoes - mean", color="red", marker="v", linestyle = "--")
    ax.plot(x, y4, label = "3 tomatoes - variance", color = "red", marker = "o", linestyle = "dotted")

    ax.plot(x, y5, label = "3 tomatoes, 1.2g salt - mean", color = "blue", marker = "v")
    #ax.plot(x, y5_1, label="3 tomatoes, 1.2g salt - mean", color="blue", marker="v", linestyle = "--")
    ax.plot(x, y6, label = "3 tomatoes, 1.2g salt - variance", color = "blue", marker = "o", linestyle = "dotted")

    ax.plot(x, y7, label = "1.2g salt - mean", color = "black", marker = "v")
    #ax.plot(x, y7_1, label="1.2g salt - mean", color="black", marker="v", linestyle = "--")
    ax.plot(x, y8, label = "1.2g salt - variance", color = "black", marker = "o", linestyle = "dotted")

    ax.plot(x, y9, label="1.2g salt, 6 tomatoes - mean", color="yellow", marker="v")
    #ax.plot(x, y9_1, label="1.2g salt, 6 tomatoes - mean", color="yellow", marker="v", linestyle = "--")
    ax.plot(x, y10, label="1.2g salt, 6 tomatoes - variance", color="yellow", marker="o", linestyle = "dotted")

    ax.plot(x, y11, label="2.4g salt, 3 tomatoes - mean", color="orange", marker="v")
    # ax.plot(x, y11_1, label="2.4g salt, 3 tomatoes - mean", color="yellow", marker="v", linestyle = "--")
    ax.plot(x, y12, label="2.4g salt, 3 tomatoes - variance", color="orange", marker="o", linestyle="dotted")

    ax.plot(x, y13, label="2.4g salt - mean", color="orchid", marker="v")
    # ax.plot(x, y13_1, label="2.4g salt - mean", color="orchid", marker="v", linestyle = "--")
    ax.plot(x, y14, label="2.4g salt - variance", color="orchid", marker="o", linestyle="dotted")

    ax.plot(x, y15, label="6 tomatoes - mean", color="cyan", marker="v")
    # ax.plot(x, y15_1, label="2.4g salt - mean", color="syan", marker="v", linestyle = "--")
    ax.plot(x, y16, label="6 tomatoes - variance", color="cyan", marker="o", linestyle="dotted")

    ax.plot(x, y17, label="2.4g salt, 6 tomatoes - mean", color="navy", marker="v")
    # ax.plot(x, y17_1, label="2.4g salt - mean", color="syan", marker="v", linestyle = "--")
    ax.plot(x, y18, label="2.4g salt, 6 tomatoes - variance", color="navy", marker="o", linestyle="dotted")

    ax.set(xlabel='mixing state', ylabel='conductance (mS)', title='Effect of mixing on the conductance')
    ax.legend(bbox_to_anchor=(1, 1))
    ax.grid()
    fig.savefig("test.png")
    plt.show()


