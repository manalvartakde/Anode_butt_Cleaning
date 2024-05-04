import time
###### Right side ############
### Similar code only the plane variable is changed ###########

(x_pts1, y_pts1,z_pts1, rx1, ry1, rz1) = ([],[],[],[],[],[])
lim_dist = 200
file = open("points4.txt") # Insert text file name, which is to be read and sorted
content = file.readlines()

for values in content:
    try:
        val = values.split(",")
        x_pts1.append(float(val[0]))
        y_pts1.append(float(val[1]))
        z_pts1.append(float(val[2]))

        # rx1.append("0.0")
        # ry1.append(float(val[4]))
        # rz1.append(float(val[5])) 


# Insert angular restrictions here!
        rx1.append("0.0")
        if(float(val[4])>-20 and float(val[4])<20):  # rx restriction
            ry1.append(float(val[4]))
        elif(float(val[4])>20):
            ry1.append("20.0")
        else:
            ry1.append("-20")
                
        if(float(val[5])>10 and float(val[5])<30): # ry restriction
            rz1.append(float(val[5]))
        elif(float(val[5])<10):   # rz restriction
            rz1.append("10.0")
        else:
            rz1.append("30")
    except:
        pass
print("Reading right side points...")
time.sleep(2)
(x_pts, y_pts, z_pts, rx, ry, rz) = ([],[],[],[],[],[])

for i in range(len(rx1)):

### INSERT SLICING VALUE WRT Y AXIS ###

    if(int(x_pts1[i]) < 810):
        continue

#####################################

    else:
        x_pts.append(x_pts1[i])
        y_pts.append(y_pts1[i])
        z_pts.append(z_pts1[i])
        rx.append(rx1[i])
        ry.append(ry1[i])
        rz.append(rz1[i])

z_pt_max_index = z_pts.index(max(z_pts))
z_pt_min_index = z_pts.index(min(z_pts))
y_pt_max_index = y_pts.index(max(y_pts))
y_pt_min_index = y_pts.index(min(y_pts))
pt_S = z_pts[z_pt_max_index], y_pts[y_pt_min_index]
pt_T = z_pts[z_pt_max_index], y_pts[y_pt_max_index]
max_z = float(z_pts[z_pt_max_index]) 
d = 50
z = max_z
new_dec = float(z_pts[z_pt_max_index]) 
c = 0
final_count = 0
new_dec = max_z - d
start_pt = float(pt_S[0])
while(z>0):
    top_arr_1 = []
    count = 0
    if(c%2 == 0):
        for i in range(len(rx)):
            if((float(z_pts[i]) <= start_pt) and (float(z_pts[i]) > new_dec)):
                top_arr_1.append(( y_pts[i], i))
                count += 1
                final_count += 1
        top_arr_1.sort()
        top_arr_sorted_1 = [[sub[1], sub[0]] for sub in top_arr_1]
        final_arr = []
        for i in top_arr_sorted_1:
            pos = i[0]
            lst = []
            # lst.append(x_pts[pos])
            lst.append(int(x_pts[pos]) + lim_dist) ############
            lst.append(y_pts[pos])
            lst.append(z_pts[pos])
            lst.append(rx[pos])
            lst.append(ry[pos])
            lst.append(rz[pos])

            # lst.append(x_pts[pos])
            # lst.append(y_pts[pos])
            # lst.append(z_pts[pos])
            # #lst.append(rx[pos])
            # lst.append("0")
            # lst.append(-1 * rx[pos])
            # lst.append(-1 * rz[pos])
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
    elif(c%2 != 0):
        for i in range(len(rx)):
            if((float(z_pts[i]) <= start_pt) and (float(z_pts[i]) > new_dec)):
                top_arr_1.append(( y_pts[i], i))
                count += 1
                final_count += 1
        top_arr_1.sort(reverse = True)
        top_arr_sorted_1 = [[sub[1], sub[0]] for sub in top_arr_1]
        final_arr = []
        for i in top_arr_sorted_1:
            pos = i[0]
            lst = []
            # lst.append(x_pts[pos])
            lst.append(int(x_pts[pos]) + lim_dist) ############
            lst.append(y_pts[pos])
            lst.append(z_pts[pos])
            lst.append(rx[pos])
            lst.append(ry[pos])
            lst.append(rz[pos])
            
            # lst.append(x_pts[pos])
            # lst.append(y_pts[pos])
            # lst.append(z_pts[pos])
            # #lst.append(rx[pos])
            # lst.append("0")
            # lst.append(-1 * rx[pos])
            # lst.append(-1 * rz[pos])
            
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
    z -= d
    new_dec -= d
    start_pt -= d
with open('output.txt', 'a') as outfile:
    outfile.write("####################################################################\n TOTAL PTS: RIGHT: ")
    outfile.write(str(final_count))
    outfile.write("\n")
    outfile.write("####################################################################\n") 
print("RIGHT SIDE POINTS SORTED SUCCESSFULLY")
for i in range(3):
    print("...")    
    time.sleep(1)
print("ALL POINTS SLICED AND SORTED SUCCESSFULLY!!!")
print("PLEASE ACCESS output.txt FILE")