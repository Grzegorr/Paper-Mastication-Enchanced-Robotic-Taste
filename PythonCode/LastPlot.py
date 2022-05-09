import numpy as np
import matplotlib.pyplot as plt

#Data for final plot(F1):[0.5662551440329218, 0.8417965476789007, 0.7490128455040735, 0.9141917975767305]
#Data for final plot(Acc):[0.7438271604938271, 0.9398148148148148, 0.8996913580246914, 0.9753086419753086]
#Data for final plot(Prec):[0.45265700483091786, 0.7811016144349477, 0.6534231200897868, 0.857351290684624]
#Data for final plot(Rec):[1.0, 0.9861111111111112, 0.9861111111111112, 1.0]

F1 = [0.5662551440329218, 0.8417965476789007, 0.7490128455040735, 0.9141917975767305]
acc = [0.7438271604938271, 0.9398148148148148, 0.8996913580246914, 0.9753086419753086]
prec = [0.45265700483091786, 0.7811016144349477, 0.6534231200897868, 0.857351290684624]
rec = [1.0, 0.9861111111111112, 0.9861111111111112, 1.0]


X = ['Method 1', 'Method 2', 'Method 3', 'Method 4']
Y1 = acc
Y2 = prec
Y3 = rec

X_axis = np.arange(len(X))

#plt.bar(X_axis - 0.3, Y1, 0.3, label='Accuracy', color = "moccasin")
#plt.bar(X_axis , Y2, 0.3, label='Precision', color = "goldenrod")
#plt.bar(X_axis + 0.3, Y3, 0.3, label='Recall', color = "darkgoldenrod")

plt.bar(X_axis - 0.3, Y1, 0.27, label='Accuracy', color = "lightskyblue")
plt.bar(X_axis , Y2, 0.27, label='Precision', color = "palegoldenrod")
plt.bar(X_axis + 0.3, Y3, 0.27, label='Recall', color = "orange")

plt.xticks(X_axis, X)
plt.xlabel("Classification Method", fontweight='bold')
plt.ylabel("Score", fontweight='bold')
plt.title("Performance of the classification methods", fontweight='bold')
plt.legend()
plt.show()




