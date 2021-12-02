import statistics
import matplotlib.pyplot as plt
import numpy as np

import DataHandling.DataReadAndPreprocess as DATA
import CookingMoves.SalinitySamplingMoves as SALT

#Salinity_array, Img_array = DATA.read_attempt(experiment_name = "ResistanceSpreadingMaps", attempt_no = 1)
Salinity_array, Img_array = DATA.read_attempt(experiment_name = "Maps", attempt_no = 1)
first = 1
second = 2
third = 3
if_mask = "True"


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

# plt.style.use('ggplot')
# x = range(len(Salinity_array[2]))
# y = Salinity_array[2]
# plt.bar(x, y, color='green')
# plt.xlabel("Measurement Number")
# plt.ylabel("Conductance(mS/cm)")
# plt.title("Bar plot of sorted sensor measurements")
# plt.xticks(x, x)
# #plt.show()

# plt.style.use('ggplot')
# x = range(len(Salinity_array[3]))
# y = Salinity_array[3]
# plt.bar(x, y, color='green')
# plt.xlabel("Measurement Number")
# plt.ylabel("Conductance(mS/cm)")
# plt.title("Bar plot of sorted sensor measurements")
# plt.xticks(x, x)
# #plt.show()

# plt.style.use('ggplot')
# x = range(len(Salinity_array[4]))
# y = Salinity_array[4]
# plt.bar(x, y, color='green')
# plt.xlabel("Measurement Number")
# plt.ylabel("Conductance(mS/cm)")
# plt.title("Bar plot of sorted sensor measurements")
# plt.xticks(x, x)
# #plt.show()



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






x = Salinity_array[first]
y = Salinity_array[second]
z = Salinity_array[third]

bins = np.linspace(0, 10, 40)
plt.hist(x, bins, label="unmixed")
plt.ylim([0, 15])
plt.xlabel("Conductance(mS/cm)")
plt.ylabel("Frequency")
plt.title("Histogram of conductance measurements")
plt.legend(loc='upper right')
plt.show()

bins = np.linspace(0, 10, 40)
plt.hist(y, bins, label="slightly mixed")
plt.ylim([0, 15])
plt.xlabel("Conductance(mS/cm)")
plt.ylabel("Frequency")
plt.title("Histogram of conductance measurements")
plt.legend(loc='upper right')
plt.show()

bins = np.linspace(0, 10, 40)
plt.hist(z, bins, label="mixed")
plt.ylim([0, 15])
plt.xlabel("Conductance(mS/cm)")
plt.ylabel("Frequency")
plt.title("Histogram of conductance measurements")
plt.legend(loc='upper right')
plt.show()













####################################################################
# SPECIFIC PLOT HERE

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
        mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=0.9)
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
        mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=0.9)
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

    mean_half_mixed = statistics.mean(Salinity_array[second])
    print(mean_half_mixed)
    variance_half_mixed = statistics.variance(Salinity_array[second])
    print(variance_half_mixed)

    mean_fully_mixed = statistics.mean(Salinity_array[third])
    print(mean_fully_mixed)
    variance_fully_mixed = statistics.variance(Salinity_array[third])
    print(variance_fully_mixed)

    x = ["unmixed", "half-mixed", "fully-mixed"]
    y3 = [mean_unmixed, mean_half_mixed, mean_fully_mixed]
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
        mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=0.9)
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

    mean_half_mixed = statistics.mean(Salinity_array[second])
    print(mean_half_mixed)
    variance_half_mixed = statistics.variance(Salinity_array[second])
    print(variance_half_mixed)

    mean_fully_mixed = statistics.mean(Salinity_array[third])
    print(mean_fully_mixed)
    variance_fully_mixed = statistics.variance(Salinity_array[third])
    print(variance_fully_mixed)

    x = ["unmixed", "half-mixed", "fully-mixed"]
    y5 = [mean_unmixed, mean_half_mixed, mean_fully_mixed]
    y6 = [variance_unmixed, variance_half_mixed, variance_fully_mixed]








    fig, ax = plt.subplots()
    ax.plot(x, y, label = "No tomato - mean")
    ax.plot(x, y2, label = "No tomato - variance")
    ax.plot(x, y3, label = "Some tomato - mean")
    ax.plot(x, y4, label = "Some tomato - variance")
    ax.plot(x, y5, label = "Some tomato, 3g salt - mean")
    ax.plot(x, y6, label = "Some tomato, 3g salt - variance")
    ax.set(xlabel='mixing state', ylabel='conductance (mS)', title='Effect of mixing on the conductance')
    ax.legend()
    ax.grid()
    fig.savefig("test.png")
    plt.show()



