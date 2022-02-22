from sklearn import linear_model
import statistics
import numpy
from regressors import stats

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
#print(mean_variance_array)


#preparing X
if_tomato = [[0], [1], [1], [0], [1], [1], [0], [1], [1]]
salt_level = [[0], [0], [1], [1], [2], [1], [2], [0], [2]]
tomato_level = [[0], [1], [1], [0], [1], [2], [0], [2], [2]]

#Specific tomato levels
if_no_tomato = [[1], [0], [0], [1], [0], [0], [1], [0], [0]]
if_tomato_1 = [[0], [1], [1], [0], [1], [0], [0], [0], [0]]
if_tomato_2 = [[0], [0], [0], [0], [0], [1], [0], [1], [1]]






####################################################
# if adding tomato reduces the resulting variance
X = if_tomato
X = numpy.asarray(X)
mean_variance_array = numpy.array(mean_variance_array)
y = mean_variance_array[:,5]
regresor = linear_model.LinearRegression()
regresor.fit(X, y)
print("If adding tomato reduces the resulting variance(no tomato):")
print("Coefficients: ")
print(regresor.coef_)
# To calculate the p-values of beta coefficients:
print("Corresponding p values:\n", stats.coef_pval(regresor, X, y))
print("\n")

####################################################
# tomato lv 1
X = if_tomato_1
X = numpy.asarray(X)
mean_variance_array = numpy.array(mean_variance_array)
y = mean_variance_array[:,5]
regresor = linear_model.LinearRegression()
regresor.fit(X, y)
print("If adding tomato reduces the resulting variance(lv1):")
print("Coefficients: ")
print(regresor.coef_)
# To calculate the p-values of beta coefficients:
print("Corresponding p values:\n", stats.coef_pval(regresor, X, y))
print("\n")


####################################################
# tomato lv 2
X = if_tomato_2
X = numpy.asarray(X)
mean_variance_array = numpy.array(mean_variance_array)
y = mean_variance_array[:,5]
regresor = linear_model.LinearRegression()
regresor.fit(X, y)
print("If adding tomato reduces the resulting variance(lv2):")
print("Coefficients: ")
print(regresor.coef_)
# To calculate the p-values of beta coefficients:
print("Corresponding p values:\n", stats.coef_pval(regresor, X, y))
print("\n")


####################################################
# salt and tomato levels vs variance at the end
X = []
for row in range(len(if_tomato)):
    X.append([salt_level[row][0], tomato_level[row][0]])
X = numpy.asarray(X)
y = mean_variance_array[:,5]
regresor = linear_model.LinearRegression()
regresor.fit(X, y)
print("Salt and tomato levels vs variance at the end:")
print("Coefficients: ")
print(regresor.coef_)
print("Corresponding p values:\n", stats.coef_pval(regresor, X, y))
print("\n")




####################################################
# salt and tomato levels vs variance at the end
X = []
for row in range(len(if_tomato)):
    X.append([salt_level[row][0], if_tomato[row][0]])
X = numpy.asarray(X)
y = mean_variance_array[:,5]
regresor = linear_model.LinearRegression()
regresor.fit(X, y)
print("Variance at the end. Salt level as x1 and if_tomato as x2.:")
print("Coefficients: ")
print(regresor.coef_)
print("Corresponding p values:\n", stats.coef_pval(regresor, X, y))
print("\n")



####################################################
# Specific tomato levels regression
#X = []
#for row in range(len(if_tomato)):
#    X.append([if_no_tomato[row][0], if_tomato_1[row][0], if_tomato_2[row][0]])
#X = numpy.asarray(X)
#y = mean_variance_array[:,5]
#regresor = linear_model.LinearRegression()
#regresor.fit(X, y)
#print("Specific tomato levels:")
#print("Coefficients: ")
#print(regresor.coef_)
#print("Corresponding p values:\n", stats.coef_pval(regresor, X, y))
#print("\n")



####################################################
# if adding tomato causes rise of variance during mixing
X = []
for row in range(len(if_tomato)):
    X.append([salt_level[row][0], if_tomato[row][0]])
X = numpy.asarray(X)
mean_variance_array = numpy.array(mean_variance_array)
y = mean_variance_array[:,0] - mean_variance_array[:,4]
y = numpy.asarray(y)
regresor = linear_model.LinearRegression()
regresor.fit(X, y)
print("Change in the mean. Salt level as x1 and if_tomato as x2.:")
print("Coefficients: ")
print(regresor.coef_)
print("Corresponding p values:\n", stats.coef_pval(regresor, X, y))
print("\n")




####################################################
# Initial variance ingrediants
X = []
for row in range(len(if_tomato)):
    X.append([salt_level[row][0], tomato_level[row][0]])
X = numpy.asarray(X)
mean_variance_array = numpy.array(mean_variance_array)
y = mean_variance_array[:,1]
y = numpy.asarray(y)
regresor = linear_model.LinearRegression()
regresor.fit(X, y)
print("Initial Variance. Salt level as x1 and tomato level as x2.:")
print("Coefficients: ")
print(regresor.coef_)
print("Corresponding p values:\n", stats.coef_pval(regresor, X, y))
print("\n")

####################################################
# Initial mean ingrediants
X = []
for row in range(len(if_tomato)):
    X.append([salt_level[row][0], tomato_level[row][0]])
X = numpy.asarray(X)
mean_variance_array = numpy.array(mean_variance_array)
y = mean_variance_array[:,0]
y = numpy.asarray(y)
regresor = linear_model.LinearRegression()
regresor.fit(X, y)
print("Initial Mean. Salt level as x1 and tomato level as x2.:")
print("Coefficients: ")
print(regresor.coef_)
print("Corresponding p values:\n", stats.coef_pval(regresor, X, y))
print("\n")










