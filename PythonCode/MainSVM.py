from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np
import math
import random
import statistics
from sklearn import metrics as metrics

import DataHandling.DataReadAndPreprocess as DATA
import CookingMoves.SalinitySamplingMoves as SALT

if_mask = "True"
population_count = 20 # how many samples to generate from each dish
ration_of_samples = 0.3 # how many measurements should be included in one sample? range 0-1

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
    plt.show()


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
    plt.show()

#mode is what classification u do
def OneVsAllSVM(class_no, all_class_list = [1,2,3,4,5], mode = "pre_chewing"):
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
        if len(X_train) == 0:
            X_train = X1[0:last_train_index]
            y_train = y1[0:last_train_index]
            X_test = X1[last_train_index:]
            y_test = y1[last_train_index:]
        else:
            X_train = np.concatenate((X_train, X1[0:last_train_index]))
            y_train = np.concatenate((y_train, y1[0:last_train_index]))
            X_test = np.concatenate((X_test, X1[last_train_index:]))
            y_test = np.concatenate((y_test, y1[last_train_index:]))



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

        clf = svm.SVC(class_weight='balanced') # class weight added here
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
        plt.show()


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


        clf = svm.SVC(class_weight='balanced')  # class weight added here
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
        plt.show()

    if mode == "full_info":
        # FOR initial 2 D play
        X_train_mode = X_train
        X_train_mode = np.asarray(X_train_mode)

        X_test_mode = X_test
        X_test_mode = np.asarray(X_test_mode)


        clf = svm.SVC(class_weight='balanced')  # class weight added here
        clf.fit(X_train_mode, y_train)  # fits the model, learning happens here

    # Assesing the classifier
    predictions = clf.predict(X_test_mode)
    #print("Predicted labels: " + str(predictions))
    #print("Ground truth labels: " + str(y_test))
    accuracy = metrics.accuracy_score(y_test, predictions)
    print("Accuracy: " +str(accuracy))
    recall = metrics.recall_score(y_test, predictions)
    print("Recall: " + str(recall))
    f1 = metrics.f1_score(y_test, predictions)
    print("F1: " + str(f1))



if __name__ == "__main__":
    #scatter_plot_all_variables()
    #two_class_svm(1,2)
    for class_number in [1,2,3,4,5]:
        print("Next class:")
        print("__pre_chewing__:")
        OneVsAllSVM(class_no=class_number, all_class_list=[1,2,3,4,5], mode = "pre_chewing")
        print("__post_chewing__:")
        OneVsAllSVM(class_no=class_number, all_class_list=[1,2,3,4,5], mode="post_chewing")
        print("__full_info__:")
        OneVsAllSVM(class_no=class_number, all_class_list=[1,2,3,4,5], mode="full_info")
        print("\n")



