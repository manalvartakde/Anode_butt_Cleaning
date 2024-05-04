import time
#### Code for path planning in Anode Butt Cleaning #######
#### FRONT SIDE ######

(x_pts1, y_pts1,z_pts1, rx1, ry1, rz1) = ([],[],[],[],[],[])

file = open("points4.txt") # Insert text file name, which is to be read and sorted
content = file.readlines() # Reads the text file

lim_dist = 100  # Insert distance that is to be limited from the anode butt // The tool will be that distance away from the anode

for values in content:
    try:
        val = values.split(",")
        x_pts1.append(float(val[0]))
        y_pts1.append(float(val[1]))
        z_pts1.append(float(val[2]))
        
        # rx1.append(float(val[3]))
        # ry1.append("0.0")
        # rz1.append(float(val[5]))


        # Limits the rotation of the tool to a certain angle
        # For reference
        # val[3] --> rx
        # val[4] --> ry
        # val[5] --> rz

        ry1.append("0.0")
        if(float(val[3])>-10 and float(val[3])<15):
            rx1.append(float(val[3]))
        elif(float(val[3])>15):
            rx1.append("15.0")
        else:
            rx1.append("-10")

        if(float(val[5])>-30 and float(val[5])<30):
            rz1.append(float(val[5]))
        elif(float(val[5])>30):
            rz1.append("30.0")
        else:
            rz1.append("-30")

    except:
        pass

(x_pts, y_pts,z_pts, rx, ry, rz) = ([],[],[],[],[],[])

for i in range(len(rx1)):

### INSERT SLICING VALUE WRT Y AXIS ###

    if(int(y_pts1[i]) > 200): # insert the slicing value here
        continue

#############################################

    else:
        x_pts.append(x_pts1[i])
        y_pts.append(y_pts1[i])
        z_pts.append(z_pts1[i])
        rx.append(rx1[i])
        ry.append(ry1[i])
        rz.append(rz1[i])
# Selects top corner points   index no   
z_pt_max_index = z_pts.index(max(z_pts))
z_pt_min_index = z_pts.index(min(z_pts))
#########################################
# Selects bottom corner points index no
x_pt_max_index = x_pts.index(max(x_pts))
x_pt_min_index = x_pts.index(min(x_pts))
#########################################

print("Reading Front side points...")
time.sleep(2)
#print((z_pts[z_pt_min_index]+z_pts[z_pt_max_index])//2 , (x_pts[x_pt_min_index]+x_pts[x_pt_max_index])//2)

# Selects top corner points
pt_S = z_pts[z_pt_max_index], x_pts[x_pt_min_index]
# Selects bottom corner points
pt_T = z_pts[z_pt_max_index], x_pts[x_pt_max_index]


max_z = float(z_pts[z_pt_max_index]) 

decrement = 50    # This is the distance(mm) by which tool moves down at the end of the anode block                

z = max_z
new_dec = float(z_pts[z_pt_max_index]) 
c = 0
final_count = 0
new_dec = max_z - decrement
start_pt = float(pt_S[0])


while(z>0):
    top_arr_1 = []
    top_arr_3 = [] 
    top_arr_4 = []  

    # Variable count, counts the number of divisions in one face
    count = 0

    if(c%2 == 0):
        for i in range(len(rx)):

            # Selects the points in an interval
            if((float(z_pts[i]) <= start_pt) and (float(z_pts[i]) > new_dec)):
                top_arr_1.append(( x_pts[i], i))
                top_arr_3.append(y_pts[i]) ####
                count += 1
                final_count += 1

        # Takes average along y axis
        if(len(top_arr_3) != 0):
            y_avg = sum(top_arr_3) // len(top_arr_3)
            # print(y_avg)


        # sorts the points for the interval in ascending order
        top_arr_1.sort()
        top_arr_sorted_1 = [[sub[1], sub[0]] for sub in top_arr_1]
        final_arr = []

        for i in top_arr_sorted_1:
            pos = i[0]
            lst = []
            lst.append(x_pts[pos])
            # lst.append(y_pts[pos])
            #lst.append(int(y_pts[pos])- lim_dist) ##################
            if(y_pts[pos] > y_avg -10 and y_pts[pos] < y_avg + 10):
                lst.append(y_pts[pos])
            else:
                lst.append(y_avg)
            lst.append(z_pts[pos])
            lst.append(rx[pos])
            lst.append(ry[pos])
            lst.append(rz[pos]) 
        # Sorted points are appended to the final array
            final_arr.append(lst)

        # Writes the sorted array points in the text file named "output.txt"
        for i in final_arr:
            for j in range(len(i)):
                if(j != 5):
                    with open('output.txt', 'a') as outfile:
                        outfile.write(str(i[j]))
                        outfile.write(", ")
                else:
                    with open('output.txt', 'a') as outfile:
                        outfile.write(str(i[j]))
                        outfile.write("\n")

    # Similar code as above 
    # The points are sorted in descending order

    elif(c%2 != 0):
        for i in range(len(rx)):
            if((float(z_pts[i]) <= start_pt) and (float(z_pts[i]) > new_dec)):
                top_arr_1.append(( x_pts[i], i))
                count += 1
                final_count += 1
                top_arr_3.append(y_pts[i]) ####

        if(len(top_arr_3) != 0):
            y_avg = sum(top_arr_3) // len(top_arr_3)
            # print(y_avg)

        # Sorts the array in descending order
        top_arr_1.sort(reverse = True)
        top_arr_sorted_1 = [[sub[1], sub[0]] for sub in top_arr_1]
        final_arr = []

        for i in top_arr_sorted_1:
            pos = i[0]
            lst = []
            lst.append(x_pts[pos])
            # lst.append(y_pts[pos])
            #lst.append(int(y_pts[pos])- lim_dist) ##################
            if(y_pts[pos] > y_avg -10 and y_pts[pos] < y_avg + 10):
                lst.append(y_pts[pos])
            else:
                lst.append(y_avg)
            lst.append(z_pts[pos])
            lst.append(rx[pos])
            lst.append(ry[pos])
            lst.append(rz[pos])

            final_arr.append(lst)
        for i in final_arr:
            for j in range(len(i)):
                if(j != 5):
                    with open('output.txt', 'a') as outfile:
                        outfile.write(str(i[j]))
                        outfile.write(", ")
                else:
                    with open('output.txt', 'a') as outfile:
                        outfile.write(str(i[j]))
                        outfile.write("\n")
    c += 1
    z -= decrement
    new_dec -= decrement
    start_pt -= decrement
with open('output.txt', 'a') as outfile:
    outfile.write("####################################################################\n TOTAL PTS: FRONT: ")
    outfile.write(str(final_count))
    outfile.write("\n")
    outfile.write("####################################################################\n")
print("FRONT SIDE POINTS SORTED SUCCESSFULLY")

