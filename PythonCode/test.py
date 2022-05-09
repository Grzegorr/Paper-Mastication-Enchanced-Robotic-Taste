import numpy as np
import matplotlib.pyplot as plt
import time

data = [1,2,3,5,6,7,1,2,3]
#data = [0,0,0,0,0,0,0,0,0]

data_len = len(data)
side = np.sqrt(data_len)

# array to display
display = np.zeros((side.astype(int), side.astype(int)))

# fill the display in
# display = np.array([[1,2],[3,4]]) # test display for no_samples = 4

for n in range(data_len):
    x = n // side
    y = n % side
    display[int(x), int(y)] = data[n]



plt.ion()
plt.figure(figsize=(7, 6))
plt.show()
plt.pcolormesh(np.array(display))
plt.colorbar()


for r in range(10):

    #plt.pcolormesh(np.array(display))
    #plt.colorbar()
    #plt.draw()
    #plt.pause(0.002)

    subplot = plt.subplot()
    image = subplot.imshow(display)
    plt.colorbar(image)
    time.sleep(1)


