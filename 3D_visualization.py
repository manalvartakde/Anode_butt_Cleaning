import pandas as pd
import numpy as np

from mpl_toolkits import mplot3d

# %matplotlib inline
import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = plt.axes(projection='3d')

data = pd.read_csv('Final_ABC\points4.txt') 

# Reads the csv file
X_data = data['X']
Y_data = data['Y']
Z_data = data['Z']
RX_data = data['RX']
RY_data = data['RY']
RZ_data = data['RZ']

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('x_axis')
ax.set_ylabel('y_axis')
ax.set_zlabel('z_axis')

xline = np.array(X_data)
yline = np.array(Y_data)
zline = np.array(Z_data)
ax.plot3D(xline, yline, zline, 'gray')


# plots the points along with the path
ax = plt.axes(projection = '3d')
#ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5)
ax.scatter(xline, yline, zline, 'blue')
#ax.plot(xline, yline, zline, "r")

plt.show()