import csv 
import matplotlib.pyplot as plt
import math
import random

def main():
    ##initilizes new centroids at random location 
    centroid1 = [random.uniform(0.0, 85.0), random.uniform(0.0, 85.0)]
    centroid2 = [random.uniform(0.0, 85.0), random.uniform(0.0, 85.0)]
    ##Initialize variables to hold old centroids position for comparison
    oldcent1 = [0,0]
    oldcent2 = [0,0]
    
    ##initialize min and max values for red cluster
    min1x = 100
    min1y = 100
    max1x = 0
    max1y = 0
    redcount = 0
    
    ##initialize min and max values for blk cluster
    min2x = 100
    min2y = 100
    max2x = 0
    max2y = 0
    blkcount = 0
    
    ##boolean variable to indicate when we have found a stopping point
    different = True
    b = [0,0]
    iteration = 0
    try:
        plt.ion()
        ##if false then centroids haven't changed and a stopping point is found
        while different == True:
            with open('datasetQ2.csv', mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
             
                for row in csv_reader:
                    ##checks if it is the first line which would have labels not data points 
                    if line_count == 0:
                        line_count += 1            
                    ##otherwise start processing data points
                    else:  
                        ##used reformat data from csv file          
                        line = ','.join(row)
                        ##place centroids first
                        plt.scatter(float(centroid1[0]), float(centroid1[1]), color="blue")
                        plt.scatter(float(centroid2[0]), float(centroid2[1]), color="blue")
                        plt.annotate('Centroid1', (float(centroid1[0]), float(centroid1[1])), color="blue")
                        plt.annotate('Centroid2', (float(centroid2[0]), float(centroid2[1])), color="blue")
                        ##splits line at (,), in this mode (1) it creates a list out of the splits
                        a = line.split(',', 1)
                        ##convert this to floating type for pyplot to work
                        b = [float(a[0]), float(a[1])]
                        ##calculates the distnace from each centroid to the current data point
                        e1 = euclid(centroid1, b)
                        e2 = euclid(centroid2, b)
                        ## if closer to centroid1 then it will become part of red cluster
                        if(e1 <= e2):
                            ## if its the first point in the cluster, initialize the min/max to it to avoid skewing the cluster bounds with randomly assigned values
                            if (redcount == 0):
                                min1x = b[0]
                                min1y = b[1]
                                max1x = b[0]
                                max1y = b[1] 
                            ##adds new to graph       
                            plt.scatter(b[0], b[1], color="red")
                            x_values = [b[0], centroid1[0]]
                            y_values = [b[1], centroid1[1]]
                            plt.plot(x_values, y_values, color="red", linewidth=0.5)
                            ##plots line connecting point to its nearest centroid
                            redcount += 1
                            if line_count == 1:
                                min1x = b[0]
                                min1y = b[1]
                                max1x = b[0]
                                max1y = b[1]
                            else:   
                                ## if its not the first point in the cluster, see if it is further away than current points
                                if b[0] < min1x:
                                    min1x = b[0]
                                elif b[1] < min1y:
                                    min1y = b[1]
                                elif b[0] > max1x:
                                    max1x = b[0]
                                elif b[1] > max1y:
                                    max1y = b[1]
                        
                        ## if closer to centroid2 then it will become part of blk cluster 
                        else:
                            ## if its the first point in the cluster, initialize the min/max to it to avoid skewing the cluster bounds with randomly assigned values
                            if (blkcount == 0):
                                min2x = b[0]
                                min2y = b[1]
                                max2x = b[0]
                                max2y = b[1]   
                            ##adds new black point
                            plt.scatter(b[0], b[1], color="black")
                            x_values = [b[0], centroid2[0]]
                            y_values = [b[1], centroid2[1]]
                            plt.plot(x_values, y_values, color="black", linewidth=0.5)
                            ## plots lines connecting points to their centroid
                            blkcount += 1
                            if line_count == 1:
                                min2x = b[0]
                                min2y = b[1]
                                max2x = b[0]
                                max2y = b[1]
                            else:  
                                ##sets min to b value if old min is higher
                                if b[0] < min2x:
                                    min2x = b[0]
                                elif b[1] < min2y:
                                    min2y = b[1]
                                elif b[0] > max2x:
                                    max2x = b[0]
                                elif b[1] > max2y:
                                    max2y = b[1]
                        ##iterate to keep track of the line in the file           
                        line_count += 1

                print("========================================================") 
                print(f'[{iteration}]  centroid1 [ {centroid1[0]} , {centroid1[1]} ] | centroid2 [ {centroid2[0]} , {centroid2[1]} ]')

                plt.xlim(0, 85)
                plt.ylim(0, 85)
                ##check if the coordinates of both centroids are the same as their previous ones
                if ((oldcent1[0] == centroid1[0]) and (oldcent1[1] == centroid1[1]) and (oldcent2[0] == centroid2[0]) and (oldcent2[1] == centroid2[1])):
                    different = False
                else:
                    ##changes centroids if they are not equal and create new centroids based on centre point of current cluster
                    oldcent1 = centroid1
                    oldcent2 = centroid2
                    centroid1 = [(max1x + min1x)/2, (max1y + min1y)/2]
                    centroid2 = [(max2x + min2x)/2, (max2y + min2y)/2]
                
                if different != False:
                    ##delay changing the data points so the user can see how they change
                    plt.pause(0.5)
                    plt.cla()
                   ##once there are no new values it can finish and show the result
                else:
                    ##pause on final configuration of points and centroids before closing
                    plt.pause(2)
                    plt.close('all')
                    ##output final centroid placement
                    print("========================================================") 
                    print("[Final]")
                    print(f'(RED) Centroid1 : {centroid1}  |  Cluster Size: {redcount} \n(Blk) Centroid2 : {centroid2}  |  Cluster Size: {blkcount}')
            ##reset cluster size counters 
            redcount = 0
            blkcount = 0
            iteration += 1
         
        plt.ioff()
        plt.show()
        ##displays graph to the user
                
    except:
        print("Something isn't working")
        

def euclid(cent, A):
    ##performs the euclidean distance calculation between points and their centroid
    x = ((A[0] - cent[0])**2)
    y = ((A[1] - cent[1])**2)
    return math.sqrt(x+y)
main()
