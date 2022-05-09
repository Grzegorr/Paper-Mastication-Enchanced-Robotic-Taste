import statistics
import numpy
import matplotlib.pyplot as plt


import DataHandling.DataReadAndPreprocess as DATA
import CookingMoves.SalinitySamplingMoves as SALT

#stores mean and variance
mean_variance_array = []

#prepare data for Y
for attempt_to_read in [1,2,3,4,5,6,7,8,9]:
    Salinity_array, Img_array = DATA.read_attempt(experiment_name="Accurate_Tests", attempt_no=attempt_to_read)
    #mask out the out of plate area
    mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=0.9)
    for i in [0, 1, 2]:
        dummy = []
        for j in range(len(Salinity_array[i])):
            if mask[j] == 1:
                dummy.append(Salinity_array[i][j])
        Salinity_array[i] = dummy
    # extract mean, variance
    dummy = []
    for i in [0, 1, 2]:
        dummy.append(statistics.mean(Salinity_array[i]))
        dummy.append(statistics.variance(Salinity_array[i]))
    mean_variance_array.append(dummy)
mean_variance_array = numpy.asarray(mean_variance_array)
print()
print(mean_variance_array)

###################### Adjust for dish number in the paper #############################
mean_variance_array_dummy = []
mean_variance_array_dummy.append(mean_variance_array[0])
mean_variance_array_dummy.append(mean_variance_array[1])
mean_variance_array_dummy.append(mean_variance_array[7])
mean_variance_array_dummy.append(mean_variance_array[3])
mean_variance_array_dummy.append(mean_variance_array[2])
mean_variance_array_dummy.append(mean_variance_array[4])
mean_variance_array_dummy.append(mean_variance_array[6])
mean_variance_array_dummy.append(mean_variance_array[5])
mean_variance_array_dummy.append(mean_variance_array[8])
mean_variance_array = numpy.asarray(mean_variance_array_dummy)
print()
print(mean_variance_array)
print()







plt.figure()
# set width of bars
barWidth = 0.8
# set heights of bars
bars = [mean_variance_array[:,5][0], mean_variance_array[:,5][3], mean_variance_array[:,5][6],mean_variance_array[:,5][1], mean_variance_array[:,5][2], mean_variance_array[:,5][5], mean_variance_array[:,5][4], mean_variance_array[:,5][7], mean_variance_array[:,5][8]]
print(bars)
# Set position of bar on X axis
r1 = numpy.arange(len(bars))
# Make the plot
plt.bar([0,1,2,3,4,5,6,7,8], bars, color='navy', width=barWidth, edgecolor='white', label='F1 score - post-chewing mean')

# Add xticks on the middle of the group bars
#plt.ylim(0.5,1)
plt.xlabel('Dish Variety', fontweight='bold')
plt.ylabel('Post Chewing Variance', fontweight='bold')
plt.xticks(range(len(bars)), ['pure_eggs','1.2 g of salt','2.4g salt','3 tomatoes','3 tomaatoes, 1.2g salt','3 tomatoes, 2.4g salt','6 tomatoes, 1.2g salt','6 tomatoes','6 tomatoes, 2.4g salt'])

# Create legend & Show graphic
#plt.legend()
plt.show()




#################################################################################################
#                                       SLOPE OF MEAN                                           #
#################################################################################################

plt.figure()
# set width of bars
barWidth = 0.8
# set heights of bars
bars = [mean_variance_array[:,4][0]-mean_variance_array[:,0][0], mean_variance_array[:,4][1]-mean_variance_array[:,0][1], mean_variance_array[:,4][2]-mean_variance_array[:,0][2] ,mean_variance_array[:,4][3]-mean_variance_array[:,0][3], mean_variance_array[:,4][4]-mean_variance_array[:,0][4], mean_variance_array[:,4][5]-mean_variance_array[:,0][5], mean_variance_array[:,4][6]-mean_variance_array[:,0][6], mean_variance_array[:,4][7]-mean_variance_array[:,0][7], mean_variance_array[:,4][8]-mean_variance_array[:,0][8]]
print(bars)
# Set position of bar on X axis
r1 = numpy.arange(len(bars))
# Make the plot
plt.bar([0,1,2,3,4,5,6,7,8], bars, color='navy', width=barWidth, edgecolor='white', label='F1 score - post-chewing mean')

# Add xticks on the middle of the group bars
#plt.ylim(0.5,1)
plt.xlabel('Dish Variety', fontweight='bold')
plt.ylabel('Change in Conductance from Chewing', fontweight='bold')
plt.xticks(range(len(bars)), ['No additives','1.2g salt','2.4g salt','3 tomatoes','3 tomatoes\n1.2g salt','3 tomatoes\n2.4g salt','6 tomatoes\n1.2g salt','6 tomatoes','6 tomatoes\n2.4g salt'])

# Create legend & Show graphic
#plt.legend()
plt.show()




#################################################################################################
#                                       SLOPE OF MEAN IMPROVED                                  #
#################################################################################################

plt.figure(figsize=(10, 20))

# set width of bars
barWidth = 0.8
# set heights of bars
bars = [mean_variance_array[:,0][0], mean_variance_array[:,0][1], mean_variance_array[:,0][2], mean_variance_array[:,0][3], mean_variance_array[:,0][4], mean_variance_array[:,0][5], mean_variance_array[:,0][6], mean_variance_array[:,0][7], mean_variance_array[:,0][8]]
print(bars)
# Set position of bar on X axis
r1 = numpy.arange(len(bars))
# Make the plot
plt.subplot(3,1,1)
plt.bar([0,1,2,3,4,5,6,7,8], bars, color='black', width=barWidth, edgecolor='white', label='F1 score - post-chewing mean')

# Add xticks on the middle of the group bars
#plt.ylim(0.5,1)
#plt.xlabel('Dish Variety', fontweight='bold', fontsize = 14)
plt.ylabel('Conductance Average\nBefore Mixing [mS/cm]', fontweight='bold', fontsize = 14)
#plt.xticks(range(len(bars)), ['No additives','1.2g salt','2.4g salt','3 tomatoes','3 tomatoes\n1.2g salt','3 tomatoes\n2.4g salt','6 tomatoes\n1.2g salt','6 tomatoes','6 tomatoes\n2.4g salt'])
plt.xticks(range(len(bars)), ['Dish 1','Dish 2','Dish 3','Dish 4','Dish 5','Dish 6','Dish 7','Dish 8','Dish 9'], fontsize = 14)

# Create legend & Show graphic
#plt.legend()
#plt.show()



# set width of bars
barWidth = 0.8
# set heights of bars
bars = [mean_variance_array[:,4][0], mean_variance_array[:,4][1], mean_variance_array[:,4][2], mean_variance_array[:,4][3], mean_variance_array[:,4][4], mean_variance_array[:,4][5], mean_variance_array[:,4][6], mean_variance_array[:,4][7], mean_variance_array[:,4][8]]
print(bars)
# Set position of bar on X axis
r1 = numpy.arange(len(bars))
# Make the plot
plt.subplot(3,1,2)
plt.bar([0,1,2,3,4,5,6,7,8], bars, color='navy', width=barWidth, edgecolor='white', label='F1 score - post-chewing mean')

# Add xticks on the middle of the group bars
#plt.ylim(0.5,1)
#plt.xlabel('Dish Variety', fontweight='bold', fontsize = 14)
plt.ylabel('Conductance Average\nAfter Mixing [mS/cm]', fontweight='bold', fontsize = 14)
plt.xticks(range(len(bars)), ['Dish 1','Dish 2','Dish 3','Dish 4','Dish 5','Dish 6','Dish 7','Dish 8','Dish 9'], fontsize = 14)

# Create legend & Show graphic
#plt.legend()
#plt.show()



# set width of bars
barWidth = 0.8
# set heights of bars
bars = [mean_variance_array[:,4][0]-mean_variance_array[:,0][0], mean_variance_array[:,4][1]-mean_variance_array[:,0][1], mean_variance_array[:,4][2]-mean_variance_array[:,0][2] ,mean_variance_array[:,4][3]-mean_variance_array[:,0][3], mean_variance_array[:,4][4]-mean_variance_array[:,0][4], mean_variance_array[:,4][5]-mean_variance_array[:,0][5], mean_variance_array[:,4][6]-mean_variance_array[:,0][6], mean_variance_array[:,4][7]-mean_variance_array[:,0][7], mean_variance_array[:,4][8]-mean_variance_array[:,0][8]]
print(bars)
# Set position of bar on X axis
r1 = numpy.arange(len(bars))
# bar colors
color_array = ['green', 'red', 'red', 'green', 'red', 'red', 'green', 'red', 'red']
# Make the plot
plt.subplot(3,1,3)
plt.bar([0,1,2,3,4,5,6,7,8], bars, color=color_array, width=barWidth, edgecolor='white', label='F1 score - post-chewing mean')

# Add xticks on the middle of the group bars
#plt.ylim(0.5,1)
plt.xlabel('Dish Variety', fontweight='bold', fontsize = 14)
plt.ylabel('Change in Conductance\nFrom Mixing [mS/cm]', fontweight='bold', fontsize = 14)
plt.xticks(range(len(bars)), ['Dish 1','Dish 2','Dish 3','Dish 4','Dish 5','Dish 6','Dish 7','Dish 8','Dish 9'], fontsize = 14)

# Create legend & Show graphic
#plt.legend()
plt.show()






#################################################################################################
#                                     VARIANCE DECREAED BY TOMATO ADDITION                      #
#################################################################################################

plt.figure(figsize=(10, 20))

# set width of bars
barWidth = 0.8
# set heights of bars
bars = [mean_variance_array[:,1][0], mean_variance_array[:,1][1], mean_variance_array[:,1][2], mean_variance_array[:,1][3], mean_variance_array[:,1][4], mean_variance_array[:,1][5], mean_variance_array[:,1][6], mean_variance_array[:,1][7], mean_variance_array[:,1][8]]
print(bars)
# Set position of bar on X axis
r1 = numpy.arange(len(bars))
# Make the plot
plt.subplot(2,1,1)
plt.bar([0,1,2,3,4,5,6,7,8], bars, color='black', width=barWidth, edgecolor='white', label='F1 score - post-chewing mean')

# Add xticks on the middle of the group bars
#plt.ylim(0.5,1)
#plt.xlabel('Dish Variety', fontweight='bold', fontsize = 14)
plt.ylabel('Conductance Variance\nBefore Mixing [$(mS/cm)^2$]', fontweight='bold', fontsize = 14)
#plt.xticks(range(len(bars)), ['No additives','1.2g salt','2.4g salt','3 tomatoes','3 tomatoes\n1.2g salt','3 tomatoes\n2.4g salt','6 tomatoes\n1.2g salt','6 tomatoes','6 tomatoes\n2.4g salt'])
plt.xticks(range(len(bars)), ['Dish 1','Dish 2','Dish 3','Dish 4','Dish 5','Dish 6','Dish 7','Dish 8','Dish 9'], fontsize = 14)

# Create legend & Show graphic
#plt.legend()
#plt.show()


# set width of bars
barWidth = 0.8
# set heights of bars
bars = [mean_variance_array[:,5][0], mean_variance_array[:,5][1], mean_variance_array[:,5][2], mean_variance_array[:,5][3], mean_variance_array[:,5][4], mean_variance_array[:,5][5], mean_variance_array[:,5][6], mean_variance_array[:,5][7], mean_variance_array[:,5][8]]
print(bars)
# Set position of bar on X axis
r1 = numpy.arange(len(bars))
# bar colors
color_array = ['green', 'red', 'red', 'green', 'red', 'red', 'green', 'red', 'red']
# Make the plot
plt.subplot(2,1,2)
plt.bar([0,1,2,3,4,5,6,7,8], bars, color=color_array, width=barWidth, edgecolor='white', label='F1 score - post-chewing mean')

# Add xticks on the middle of the group bars
#plt.ylim(0.5,1)
plt.xlabel('Dish Variety', fontweight='bold', fontsize = 14)
plt.ylabel('Conductance Variance\nAfter Mixing [$(mS/cm)^2$]', fontweight='bold', fontsize = 14)
plt.xticks(range(len(bars)), ['Dish 1','Dish 2','Dish 3','Dish 4','Dish 5','Dish 6','Dish 7','Dish 8','Dish 9'], fontsize = 14)

# Create legend & Show graphic
#plt.legend()
plt.show()
















#################################################################################################
#                                       WATER ADDED EXPERIMENT                                  #
#################################################################################################



#################################################
Salinity_array, Img_array = DATA.read_attempt(experiment_name="Accurate_Tests", attempt_no=4)
first = 1
second = 2
third = 3
extra = 4
if_mask = "True"

##ADJUSTMENT FOR PYTHON INDEXING ONLY
first = first - 1
second = second - 1
third = third - 1
extra = extra - 1

if if_mask == "True":
    mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=0.9)
    for i in [first, second, third, extra]:
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

mean_added_water = statistics.mean(Salinity_array[extra])
print(mean_fully_mixed)
variance_added_water = statistics.variance(Salinity_array[extra])
print(variance_fully_mixed)

x = ["Not Mixed", "Half Mixed", "Mixed","Water Addition"]
y9 = [mean_unmixed, mean_half_mixed, mean_fully_mixed, mean_added_water]
y10 = [variance_unmixed, variance_half_mixed, variance_fully_mixed, variance_added_water]


plt.plot(x, y9, label="Mean [mS/cm]", color="navy", marker="v")
plt.plot(x, y10, label="Variance [$(mS/cm)^2$]", color="red", marker="o")

plt.xlabel('Mixing State', fontweight='bold', fontsize = 12)
plt.ylabel('Dish 4 - Conductance', fontweight='bold', fontsize = 12)
#ax.set(xlabel='mixing state', ylabel='conductance (mS)', title='Effect of mixing on the conductance', fontsize = 14)
plt.legend()
plt.grid()
plt.show()