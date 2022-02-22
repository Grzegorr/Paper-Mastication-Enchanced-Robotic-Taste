from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np
import math
import random
import statistics
from sklearn import metrics as metrics
import sklearn

import DataHandling.DataReadAndPreprocess as DATA
import CookingMoves.SalinitySamplingMoves as SALT

#Default
#if_normalize = "False"
#if_mask = "True"
#population_count = 40 # how many samples to generate from each dish
#ration_of_samples = 0.4 # how many measurements should be included in one sample? range 0-1

#scarce
if_normalize = "True"
if_mask = "True"
population_count = 15 # how many samples to generate from each dish
ration_of_samples = 0.25 # how many measurements should be included in one sample? range 0-1

if_normalize = "True"
if_mask = "True"
population_count = 40 # how many samples to generate from each dish
ration_of_samples = 0.4 # how many measurements should be included in one sample? range 0-1

#Which maps to load?
first = 1
second = 2
third = 3
##ADJUSTMENT FOR PYTHON INDEXING ONLY
first = first -1
second = second -1
third = third -1

###############
#########SVM example
#########
#X = [[0, 0], [1, 1]] # each [] is a sample, while i i [] are features values
#y = [0, 1] # labels for each sample
#change ot numpy array
#X = np.asarray(X)
#y = np.asarray(y)

#clf = svm.SVC()
#clf.fit(X, y) # fits the model, learning happens here
#predictions = clf.predict([[0,0], [1,1],[-1,-1],[2,2]])
#print(predictions)

def generate_samples(population_count, ration_of_samples, class_number, class_label = 0):
    Salinity_array, Img_array = DATA.read_attempt(experiment_name = "Accurate_Tests", attempt_no = class_number)

    not_chewed_samples = []
    half_chewed_samples = []
    chewed_samples = []

    if if_mask == "True":
        mask = SALT.mask_for_actually_measured_values(0.09, 400, radius_ratio=1)
        for i in [first,second,third]:
            dummy = []
            for j in range(len(Salinity_array[i])):
                if mask[j] == 1:
                    dummy.append(Salinity_array[i][j])
            Salinity_array[i] = dummy

    total_samples = len(Salinity_array[0])
    #print("Length of salinity array(samples): " + str(total_samples))

    no_samples_to_generate = math.floor(ration_of_samples * len(Salinity_array[0]))
    #print("no_samples_to_generate: " + str(no_samples_to_generate))
    for i in range(population_count):
        sample_indexes = random.sample(range(total_samples), no_samples_to_generate)
        #print(sample_indexes)
        dummy = []
        for j in sample_indexes:
            dummy.append(Salinity_array[first][j])
        #dummy = np.array(dummy)
        #print(dummy)
        mean = statistics.mean(dummy)
        variance = statistics.variance(dummy)
        entry = [mean, variance]
        not_chewed_samples.append(entry)

        sample_indexes = random.sample(range(total_samples), no_samples_to_generate)
        #print(sample_indexes)
        dummy = []
        for j in sample_indexes:
            dummy.append(Salinity_array[second][j])
        mean = statistics.mean(dummy)
        variance = statistics.variance(dummy)
        entry = [mean, variance]
        half_chewed_samples.append(entry)

        sample_indexes = random.sample(range(total_samples), no_samples_to_generate)
        #print(sample_indexes)
        dummy = []
        for j in sample_indexes:
            dummy.append(Salinity_array[third][j])
        mean = statistics.mean(dummy)
        variance = statistics.variance(dummy)
        entry = [mean, variance]
        chewed_samples.append(entry)

    X = []
    for t in range(population_count):
        entry = [not_chewed_samples[t][0], not_chewed_samples[t][1], chewed_samples[t][0], chewed_samples[t][1]]
        #print(entry)
        X.append(entry)

    y = []
    for t in range(population_count):
        y.append(class_label)

    return X, y



def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    return xx, yy

def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

# shows all data on one scatter plot
# only 2D
def scatter_plot_all_variables():
    dim1 = 2
    dim2 = 3

    fig, ax = plt.subplots()

    X, y = generate_samples(population_count, ration_of_samples, 1, class_label=0)
    X = np.asarray(X)
    a = X[:,dim1]
    b = X[:,dim2]
    plt.scatter(a,b)

    X, y = generate_samples(population_count, ration_of_samples, 2, class_label=0)
    X = np.asarray(X)
    a = X[:, dim1]
    b = X[:, dim2]
    plt.scatter(a, b)

    X, y = generate_samples(population_count, ration_of_samples, 3, class_label=0)
    X = np.asarray(X)
    a = X[:, dim1]
    b = X[:, dim2]
    plt.scatter(a, b)

    X, y = generate_samples(population_count, ration_of_samples, 4, class_label=0)
    X = np.asarray(X)
    a = X[:, dim1]
    b = X[:, dim2]
    plt.scatter(a, b)

    X, y = generate_samples(population_count, ration_of_samples, 5, class_label=0)
    X = np.asarray(X)
    a = X[:, dim1]
    b = X[:, dim2]
    plt.scatter(a, b)

    if dim1 == 0:
        ax.set_xlabel('pre-chewing mean')
    if dim1 == 1:
        ax.set_xlabel('pre-chewing variance')
    if dim1 == 2:
        ax.set_xlabel('post-chewing mean')
    if dim1 == 3:
        ax.set_xlabel('post-chewing variance')

    if dim2 == 0:
        ax.set_ylabel('pre-chewing mean')
    if dim2 == 1:
        ax.set_ylabel('pre-chewing variance')
    if dim2 == 2:
        ax.set_ylabel('post-chewing mean')
    if dim2 == 3:
        ax.set_ylabel('post-chewing variance')
    #plt.show()


def two_class_svm(class1, class2):
    X1, y1 = generate_samples(population_count, ration_of_samples, class_number=class1, class_label=0)
    X2, y2 = generate_samples(population_count, ration_of_samples, class_number=class2, class_label=1)
    #concatinate arrays
    X_full = np.concatenate((X1, X2))
    y = np.concatenate((y1, y2))

    # FOR initial 2 D play
    X = []
    for t in range(len(X_full)):
        entry = [X_full[t][0], X_full[t][3]]
        #print(entry)
        X.append(entry)
    X = np.asarray(X)
    #print(X)

    clf = svm.SVC()
    clf.fit(X, y) # fits the model, learning happens here
    # predictions = clf.predict([[0,0], [1,1],[-1,-1],[2,2]])
    # print(predictions)

    fig, ax = plt.subplots()
    # title for the plots
    title = ('Decision surface of linear SVC ')
    # Set-up grid for plotting.
    X0, X1 = X[:, 0], X[:, 1]
    xx, yy = make_meshgrid(X0, X1)

    plot_contours(ax, clf, xx, yy, cmap=plt.cm.coolwarm, alpha=0.8)
    ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
    ax.set_ylabel('pre-chewing variance')
    ax.set_xlabel('pre-chewing mean')
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(title)
    ax.legend()
    #plt.show()

#mode is what classification u do
def OneVsAllSVM(class_no, all_class_list = [1,2], mode = "pre_chewing", C = 1, tol = 1e-4, kernel = 'poly'):
    ### Error messages:
    if class_no not in all_class_list:
        print("The class selected for classification is not in the list of class for loading, it is all_class_list variable.")

    #how many samples from each population
    last_train_index = int(np.floor(population_count*4.0/5.0))

    X_train = []
    y_train = []
    X_test = []
    y_test = []
    for Class in all_class_list:
        #for the class we select for - set label to 1, otherwise label to 0
        if Class == class_no:
            X1, y1 = generate_samples(population_count, ration_of_samples, class_number=Class, class_label=1)
        else:
            X1, y1 = generate_samples(population_count, ration_of_samples, class_number=Class, class_label=0)

        #for the first entry set X and y to the arrays extractesd as u can concatinate with empty array
        if len(X_train) == 0:   #exception for the first sample - cannot append
            X_train = X1[0:last_train_index]
            y_train = y1[0:last_train_index]
            X_test = X1[last_train_index:]
            y_test = y1[last_train_index:]
        else:
            X_train = np.concatenate((X_train, X1[0:last_train_index]))
            y_train = np.concatenate((y_train, y1[0:last_train_index]))
            X_test = np.concatenate((X_test, X1[last_train_index:]))
            y_test = np.concatenate((y_test, y1[last_train_index:]))

    if if_normalize == "True":
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X_train samples shape:")
        print(np.shape(X_train))
        print("X samples:")
        print(X_train)
        #scaler = sklearn.preprocessing.StandardScaler() ##getting instance of a scaler
        scaler = sklearn.preprocessing.MaxAbsScaler()  ##getting instance of a scaler
        #scaler = sklearn.preprocessing.MinMaxScaler()  ##getting instance of a scaler
        scaler.fit(X_train)  ##gets min and max, will be applied to both train and test data
        print("Scaler data min:")
        #print(scaler.data_min_)
        print("Scaler data max:")
        #print(scaler.data_max_)
        #print(X)
        X_train = scaler.transform(X_train)
        print("Rescaled X_train:")
        print(X_train)
        X_test = scaler.transform(X_test)
        print("Rescaled X_test:")
        print(X_test)



    if mode == "homogeneous":
        # FOR initial 2 D play
        X_train_mode = []
        for t in range(len(X_train)):
            entry = [X_train[t][2]]
            # print(entry)
            X_train_mode.append(entry)
        X_train_mode = np.asarray(X_train_mode)

        X_test_mode = []
        for t in range(len(X_test)):
            entry = [X_test[t][2]]
            # print(entry)
            X_test_mode.append(entry)
        X_test_mode = np.asarray(X_test_mode)

        clf = svm.SVC(kernel = kernel, tol = tol, C = C, class_weight='balanced') # class weight added here
        clf.fit(X_train_mode, y_train)  # fits the model, learning happens here



    if mode == "pre_chewing":
        # FOR initial 2 D play
        X_train_mode = []
        for t in range(len(X_train)):
            entry = [X_train[t][0], X_train[t][1]]
            # print(entry)
            X_train_mode.append(entry)
        X_train_mode = np.asarray(X_train_mode)

        X_test_mode = []
        for t in range(len(X_test)):
            entry = [X_test[t][0], X_test[t][1]]
            # print(entry)
            X_test_mode.append(entry)
        X_test_mode = np.asarray(X_test_mode)

        clf = svm.SVC(kernel = kernel, tol = tol, C = C, class_weight='balanced') # class weight added here
        clf.fit(X_train_mode, y_train)  # fits the model, learning happens here

        fig, ax = plt.subplots()
        # title for the plots
        title = ('Decision surface of linear SVC ')
        # Set-up grid for plotting.
        X0, X1 = X_train_mode[:, 0], X_train_mode[:, 1]
        xx, yy = make_meshgrid(X0, X1)

        plot_contours(ax, clf, xx, yy, cmap=plt.cm.coolwarm, alpha=0.8)
        ax.scatter(X0, X1, c=y_train, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
        ax.set_ylabel('pre-chewing variance')
        ax.set_xlabel('pre-chewing mean')
        ax.set_xticks(())
        ax.set_yticks(())
        ax.set_title(title)
        #plt.show()


    if mode == "post_chewing":
        # FOR initial 2 D play
        X_train_mode = []
        for t in range(len(X_train)):
            entry = [X_train[t][2], X_train[t][3]]
            # print(entry)
            X_train_mode.append(entry)
        X_train_mode = np.asarray(X_train_mode)

        X_test_mode = []
        for t in range(len(X_test)):
            entry = [X_test[t][2], X_test[t][3]]
            # print(entry)
            X_test_mode.append(entry)
        X_test_mode = np.asarray(X_test_mode)


        clf = svm.SVC(kernel = kernel, tol = tol, C = C, class_weight='balanced')  # class weight added here
        clf.fit(X_train_mode, y_train)  # fits the model, learning happens here

        fig, ax = plt.subplots()
        # title for the plots
        title = ('Decision surface of linear SVC ')
        # Set-up grid for plotting.
        X0, X1 = X_train_mode[:, 0], X_train_mode[:, 1]
        xx, yy = make_meshgrid(X0, X1)

        plot_contours(ax, clf, xx, yy, cmap=plt.cm.coolwarm, alpha=0.8)
        ax.scatter(X0, X1, c=y_train, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
        ax.set_ylabel('post-chewing variance')
        ax.set_xlabel('post-chewing mean')
        ax.set_xticks(())
        ax.set_yticks(())
        ax.set_title(title)
        #plt.show()

    if mode == "full_info":
        # FOR initial 2 D play
        X_train_mode = X_train
        X_train_mode = np.asarray(X_train_mode)

        X_test_mode = X_test
        X_test_mode = np.asarray(X_test_mode)


        clf = svm.SVC(kernel = kernel, tol = tol, C = C, class_weight='balanced')  # class weight added here
        clf.fit(X_train_mode, y_train)  # fits the model, learning happens here

    # Assesing the classifier
    predictions = clf.predict(X_test_mode)
    #print("Predicted labels: " + str(predictions))
    #print("Ground truth labels: " + str(y_test))
    accuracy = metrics.accuracy_score(y_test, predictions)
    print("Accuracy: " + str(accuracy))
    recall = metrics.recall_score(y_test, predictions)
    print("Recall: " + str(recall))
    f1 = metrics.f1_score(y_test, predictions)
    print("F1: " + str(f1))
    return accuracy, recall, f1



if __name__ == "__main__":
    #scatter_plot_all_variables()
    #two_class_svm(1,2)
    results = []
    for class_number in [1,2,3,4,5,6,7,8,9]:
        print("Next class:")
        print("__pre_chewing__:")
        acc1, rec1, f11 = OneVsAllSVM(class_no=class_number, all_class_list=[1,2,3,4,5,6,7,8,9],mode="homogeneous")
        print("__post_chewing__:")
        acc2, rec2, f12 = OneVsAllSVM(class_no=class_number, all_class_list=[1,2,3,4,5,6,7,8,9], mode="post_chewing")
        print("__pre_chewing__:")
        acc3, rec3, f13 = OneVsAllSVM(class_no=class_number, all_class_list=[1,2,3,4,5,6,7,8,9], mode = "pre_chewing")
        print("__full_info__:")
        acc4, rec4, f14 = OneVsAllSVM(class_no=class_number, all_class_list=[1,2,3,4,5,6,7,8,9], mode="full_info")
        print("\n")
        result = [acc1, rec1, f11, acc2, rec2, f12, acc3, rec3, f13, acc4, rec4, f14]
        results.append(result)
    print(results)

    #plt.close('all')
    plt.figure()
    # set width of bars
    barWidth = 0.2

    # set heights of bars
    bars1 = np.asarray(results)[:,2]
    bars2 = np.asarray(results)[:,5]
    bars3 = np.asarray(results)[:,8]
    bars4 = np.asarray(results)[:,11]

    ######  Change no of attempt in database to dish numbering in the paper  #####
    bars_dummy = []
    bars_dummy.append(bars1[0])
    bars_dummy.append(bars1[1])
    bars_dummy.append(bars1[7])
    bars_dummy.append(bars1[3])
    bars_dummy.append(bars1[2])
    bars_dummy.append(bars1[4])
    bars_dummy.append(bars1[6])
    bars_dummy.append(bars1[5])
    bars_dummy.append(bars1[8])
    bars1 = np.asarray(bars_dummy)
    bars_dummy = []
    bars_dummy.append(bars2[0])
    bars_dummy.append(bars2[1])
    bars_dummy.append(bars2[7])
    bars_dummy.append(bars2[3])
    bars_dummy.append(bars2[2])
    bars_dummy.append(bars2[4])
    bars_dummy.append(bars2[6])
    bars_dummy.append(bars2[5])
    bars_dummy.append(bars2[8])
    bars2 = np.asarray(bars_dummy)
    bars_dummy = []
    bars_dummy.append(bars3[0])
    bars_dummy.append(bars3[1])
    bars_dummy.append(bars3[7])
    bars_dummy.append(bars3[3])
    bars_dummy.append(bars3[2])
    bars_dummy.append(bars3[4])
    bars_dummy.append(bars3[6])
    bars_dummy.append(bars3[5])
    bars_dummy.append(bars3[8])
    bars3 = np.asarray(bars_dummy)
    bars_dummy = []
    bars_dummy.append(bars4[0])
    bars_dummy.append(bars4[1])
    bars_dummy.append(bars4[7])
    bars_dummy.append(bars4[3])
    bars_dummy.append(bars4[2])
    bars_dummy.append(bars4[4])
    bars_dummy.append(bars4[6])
    bars_dummy.append(bars4[5])
    bars_dummy.append(bars4[8])
    bars4 = np.asarray(bars_dummy)



    print("Bars 2:")
    print(bars2)
    print("Bars 3:")
    print(bars3)

    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]

    # Make the plot
    #plt.bar(r1, bars1, color='olive', width=barWidth, edgecolor='white', label='Homogenized Sample')
    #plt.bar(r2, bars2, color='#7f6d5f', width=barWidth, edgecolor='white', label='Chewed Sample')
    #plt.bar(r3, bars3, color='#557f2d', width=barWidth, edgecolor='white', label='Un-Chewed Sample')
    #plt.bar(r4, bars4, color='#2d7f5e', width=barWidth, edgecolor='white', label='Pre- and Post-\nChewing Data')
    plt.bar(r1, bars1, color='olive', width=barWidth, edgecolor='white', label='Classification Method 1')
    plt.bar(r2, bars2, color='#7f6d5f', width=barWidth, edgecolor='white', label='Classification Method 2')
    plt.bar(r3, bars3, color='#557f2d', width=barWidth, edgecolor='white', label='Classification Method 3')
    plt.bar(r4, bars4, color='#2d7f5e', width=barWidth, edgecolor='white', label='Classification Method 4')

    # Add xticks on the middle of the group bars
    #plt.xlabel('Dish Variety', fontweight='bold')
    plt.ylabel('One vs All classification F1 score', fontweight='bold')
    #plt.xticks([r + 2 * barWidth for r in range(len(bars1))], ['No Salt\nNo Tomato', 'No Salt\nMedium Tomato', 'Medium Salt\nMedium Tomato', 'Medium Salt\nNo Tomato', 'Medium Salt\nHigh Tomato', 'High Salt\nMedium Tomato', 'High Salt\nNo Tomato', 'No Salt\nHigh Tomato', 'High Salt\nHigh Tomato'])
    plt.xticks([r + 2 * barWidth for r in range(len(bars1))], ['Dish 1', 'Dish 2', 'Dish 3', 'Dish 4', 'Dish 5', 'Dish 6', 'Dish 7', 'Dish 8', 'Dish 9'])


    # Create legend & Show graphic
    plt.legend(loc = 'lower left')
    plt.show()


    #Average F1 scores printout:
    print("Average F1 score for post-chewed mean-only data: " + str(statistics.mean(bars4)))
    print("Average F1 score for post-chewed data: " + str(statistics.mean(bars1)))
    print("Average F1 score for pre-chewed data: " + str(statistics.mean(bars2)))
    print("Average F1 score for full data: " + str(statistics.mean(bars3)))

    averageF1_homo = statistics.mean(bars1)
    averageF1_post = statistics.mean(bars2)
    averageF1_pre = statistics.mean(bars3)
    averageF1_all = statistics.mean(bars4)

    plt.figure()
    # set width of bars
    barWidth = 0.8

    # set heights of bars
    bars = [averageF1_homo, averageF1_post, averageF1_pre, averageF1_all]

    # Set position of bar on X axis
    r1 = np.arange(len(bars))

    # Make the plot
    plt.bar([0,1,2,3], bars, color='navy', width=barWidth, edgecolor='white', label='F1 score - post-chewing mean')


    # Add xticks on the middle of the group bars
    plt.ylim(0.5,1)
    plt.xlabel('Available Taste Information', fontweight='bold')
    plt.ylabel('Average 9-class classification F1 score', fontweight='bold')
    plt.xticks(range(len(bars)), ['Homogenized\nSample', 'Post-Chewing', 'Pre-Chewing', 'Pre- and\nPost-Chewing'])

    # Create legend & Show graphic
    #plt.legend()
    plt.show()





