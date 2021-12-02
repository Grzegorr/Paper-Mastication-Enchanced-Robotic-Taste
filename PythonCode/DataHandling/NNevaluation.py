import tensorflow as tf
import statistics as stats
import numpy as np
import matplotlib.pyplot as plt


def load_a_model(model_name):
    model = tf.keras.models.load_model('Trained_Models/' + str(model_name))
    return model


def read_in_data(self, data_arr, img_arr):
    self.data_x = np.array(img_arr)
    for n in range(len(data_arr)):
        self.data_y.append(stats.variance(data_arr[n]))
    #print(self.data_x)
    #print(self.data_y)


def data_prep(data_arr, img_arr, to_learn):
    y_test = []
    for n in range(len(data_arr)):
        if to_learn == "Variance":
            y_test.append(stats.variance(data_arr[n]))
        else:
            y_test.append(stats.mean(data_arr[n]))
    x_test = np.array(img_arr, dtype=np.float32)
    x_test /= 255
    # Now y is taken care of
    y_test = np.array(y_test, dtype=np.float32)
    #Downscaling the data, so it's in 0-1 range, factor of 30 used here
    y_test /= 30.
    return x_test, y_test

def plot_actual_vs_pred(actual_variance, predicted_variance):
    plt.title("Actual and Predicted Variance vs Measurement no.")
    plt.plot(range(len(actual_variance)), actual_variance, color='r', marker='.', label="Measured")
    plt.plot(range(len(predicted_variance)), predicted_variance, color='b', marker='.', label="Predicted")
    plt.xlabel("Number of Measurement")
    plt.ylabel("Conductance [mS]")
    plt.legend()
    # plt.savefig("saltVsTime.png")
    plt.show()
    plt.clf()



def evaluate_model(model_name, test_images, test_data, to_learn):
    model = load_a_model(model_name=model_name)
    print(model.summary())

    x, y = data_prep(test_data, test_images, to_learn)

    loss, acc = model.evaluate(x, y)
    print(loss)
    print(acc)

    y_pred = model.predict(x)
    y_pred *= 30
    y *= 30
    print(y_pred)

    plot_actual_vs_pred(y, y_pred)
