#Functions to save data
import DataHandling.DataReadAndPreprocess as read_ans_process

#Everything about neural net training
import DataHandling.NNtraining as NNTraining



data_arr, img_arr = read_ans_process.read_attempt(experiment_name="Eggs_With_Brush_room_temp", attempt_no=1)
means, variances = read_ans_process.mean_and_variance(salinity_array=data_arr, ifPrint=False)
read_ans_process.plot_means_vars(means, variances)

NN = NNTraining.NeuralNet()
NN.train_model(salinity_arr=data_arr, img_arr=img_arr, model_name="SuperNaiveFirstTest")
