#Functions to save data
import DataHandling.DataReadAndPreprocess as read_and_process

#Everything about neural net training
import DataHandling.NNtraining as NNTraining

#Model Evaluation
import DataHandling.NNevaluation as NNeval



import cv2 as cv
import matplotlib.pyplot as plt

task = "try_VGG_network"
task = "try_entropy"
task = "try_canny"
#task = "try_fft"
task = "try_pasta_screenshot"
task = "try_paint_screenshot"


if task == "try_paint_screenshot":
    img1 = cv.imread("Data/Paint/paint1.png")
    img2 = cv.imread("Data/Paint/paint2.png")
    img3 = cv.imread("Data/Paint/paint3.png")
    img4 = cv.imread("Data/Paint/paint4.png")
    img5 = cv.imread("Data/Paint/paint5.png")
    img6 = cv.imread("Data/Paint/paint6.png")
    images = [img1, img2, img3, img4, img5, img6]
    images_canny = images.copy()

    # print(img1)
    # cv.imshow("Pasta 1", img1)
    # cv.waitKey(0)

    for i in range(6):
        img_gray = cv.cvtColor(images[i], cv.COLOR_RGB2GRAY)
        #images_canny[i] = cv.Canny(img_gray, 30, 200)
        images_canny[i] = cv.Canny(img_gray, 30, 200)
        cv.imshow("Canny Pasta", images_canny[i])
        cv.waitKey(0)

    fig = plt.figure(figsize=(160, 160))
    columns = 6
    rows = 2

    for i in range(6):
        fig.add_subplot(rows, columns, i + 1)
        plt.imshow(cv.cvtColor(images[i], cv.COLOR_BGR2RGB))
        # Canny image and measures
        fig.add_subplot(rows, columns, i + 7)
        plt.imshow(images_canny[i], cmap="gray")
    plt.show()



if task == "try_pasta_screenshot":
    img1 = cv.imread("Data/Pasta_canny_screenshot/pasta1.png")
    img2 = cv.imread("Data/Pasta_canny_screenshot/pasta2.png")
    img3 = cv.imread("Data/Pasta_canny_screenshot/pasta3.png")
    img4 = cv.imread("Data/Pasta_canny_screenshot/pasta4.png")
    img5 = cv.imread("Data/Pasta_canny_screenshot/pasta5.png")
    images = [img1, img2, img3, img4, img5]
    images_canny = images.copy()

    #print(img1)
    #cv.imshow("Pasta 1", img1)
    #cv.waitKey(0)

    for i in range(5):
        img_gray = cv.cvtColor(images[i], cv.COLOR_RGB2GRAY)
        images_canny[i] = cv.Canny(img_gray, 200, 600)
        #images_canny[i] = cv.Canny(img_gray, 30, 200)
        cv.imshow("Canny Pasta", images_canny[i])
        cv.waitKey(0)

    fig = plt.figure(figsize=(160, 160))
    columns = 5
    rows = 2

    for i in range(5):
        fig.add_subplot(rows, columns, i + 1)
        plt.imshow(cv.cvtColor(images[i], cv.COLOR_BGR2RGB))
        # Canny image and measures
        fig.add_subplot(rows, columns, i + 6)
        plt.imshow(images_canny[i], cmap="gray")
    plt.show()



if task == "try_fft":
    data_arr, img_arr = read_and_process.read_attempt(experiment_name="Eggs_With_Brush_room_temp", attempt_no=1)
    read_and_process.colour_img_fft_10(img_arr)


if task == "try_VGG_network":
    data_arr, img_arr = read_and_process.read_attempt(experiment_name="Eggs_With_Brush_room_temp", attempt_no=1)
    means, variances = read_and_process.mean_and_variance(salinity_array=data_arr, ifPrint=False)
    read_and_process.plot_means_vars(means, variances)

    NN = NNTraining.NeuralNet()
    NN.train_model(salinity_arr=data_arr, img_arr=img_arr, model_name="SuperNaiveFirstTest2_Mean", to_learn="Mean")

    NNeval.evaluate_model("SuperNaiveFirstTest2_Mean.h5", img_arr, data_arr,to_learn="Mean")

if task == "try_entropy":
    data_arr, img_arr = read_and_process.read_attempt(experiment_name="Eggs_With_Brush_room_temp", attempt_no=1)
    print(data_arr[0])
    #print(img_arr[0])
    #read_and_process.show_image(img_arr[0])
    for i in range(10):
        entropy = read_and_process.colour_img_entropy(img_arr[i])
        print(entropy)

if task == "try_canny":
    data_arr, img_arr = read_and_process.read_attempt(experiment_name="Eggs_With_Brush_room_temp", attempt_no=1)
    read_and_process.colour_img_canny_display_10(img_arr,data_arr)





