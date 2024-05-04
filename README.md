# Anode_butt_Cleaning
Path planning for Robotic arm to clean the anode block in a sequential path

# The code accepts points in a csv file 
# The points are sequenced in X, Y, Z, Rx, Ry, Rz 

- The algorithm slices the corrosponding section based on the side of the anode block and sorts the points in the sequential manner 
- In order to avoid multiple variations average of points can also be done in the code(uncomment the required code)
- The code also restricts the excess roation movement of the tool. Based on the requirement the values of the angle can be modified

- Finally the points are stored in the _output.txt file_ in the same input sequence(X, Y, Z, Rx, Ry, Rz)

- These points can be directly given as a input to the robotic arm
