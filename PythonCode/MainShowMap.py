import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import *

import DataHandling.DataReadAndPreprocess as DATA
import CookingMoves.SalinitySamplingMoves as SALT

#entry_to_map = 14 #high res example map

entry_to_map = 19 #mixing test - not mixed
#entry_to_map = 22 #mixing test - halfly mixed
#entry_to_map = 24 #mixing test - fully mixed

entry_to_map = 0

Salinity_array, Img_array = DATA.read_attempt(experiment_name = "ResistanceSpreadingMaps", attempt_no = 0)
#Salinity_array, Img_array = DATA.read_attempt(experiment_name = "Maps", attempt_no = 1)
Salinity_array, Img_array = DATA.read_attempt(experiment_name = "Accurate_Tests", attempt_no = 3)
data = Salinity_array[entry_to_map]
#data = [1,2,3,4,5,6,7,8,9]
data_len = len(data)
side = np.sqrt(data_len)

# array to display
display = np.zeros((side.astype(int),side.astype(int)))

#fill the display in
#display = np.array([[1,2],[3,4]]) # test display for no_samples = 4

for n in range(data_len):
    x = n // side
    y = n % side
    display[int(x),int(y)] = data[n]

print(display)


fig, ax = plt.subplots()
set_cmap('gray')
im = ax.pcolor(display, vmin= 0, vmax=10)
#ax.set_title("Egg map")
plot = fig.colorbar(im, ax=ax)
plot.set_label('Conductance[mS]', rotation=270)
plt.show()


