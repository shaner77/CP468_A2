import csv 
import matplotlib.pyplot as plt
import math
from time import sleep



def main():
    
    #probably add an outer loop here so that when kmean is calculated outside file processing it can be used again above
    #I think we should create a function to open file, read contents, convert to float, and then add it's [f1,f2] to a list
    centroid1 = [10.0, 10.0]
    centroid2 = [50.0, 10.0]
    oldcent1 = [0,0]
    oldcent2 = [0,0]
    depth = 60          #depth limited to stop countless inute iterations
    max1x = 0
    max1y = 0
    min1x = 0
    min1y = 0
    max2x = 0
    max2y = 0
    min2x = 0
    min2y = 0
    redcount = 0
    blkcount = 0
    different = True
    b = [0,0]
    #===========================================================================
    # min1 = [2]
    # min2 = [2]
    # min1[0] = centroid1[0]
    # min1[1] = centroid1[1]
    # min2[0] = centroid2[0]
    # min2[1] = centroid2[1]
    #===========================================================================
    try:
        
        
        plt.ion()
        while different == True:
            '''start loop above'''
            with open('datasetQ2.csv', mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
             
                for row in csv_reader:
                    line = ','.join(row)
                    plt.scatter(float(centroid1[0]), float(centroid1[1]), color="blue")
                    plt.scatter(float(centroid2[0]), float(centroid2[1]), color="blue")
                    #plt.annotate("Centroid 1", (centroid1[0], centroid1[1]))
                    #plt.annotate("Centroid 2", (centroid2[0], centroid2[1]))
                    if line_count == 0:
                        print(f'Features: {"  ,  ".join(row)}')
                        line_count += 1            
                    else:
                        a = line.split(',', 1)
                        e1 = euclid(centroid1, a)
                        e2 = euclid(centroid2, a)
                       
                        b = [float(a[0]), float(a[1])]
                        if(e1 <= e2):
                            
                            plt.scatter(b[0], b[1], color="red")
                            x_values = [b[0], centroid1[0]]
                            y_values = [b[1], centroid1[1]]
                            plt.plot(x_values, y_values, color="red")
                            
                            redcount += 1
                            if b[0] < min1x:
                                min1x = b[0]
                            elif b[1] < min1y:
                                min1y = b[1]
                            elif b[0] > max1x:
                                max1x = b[0]
                            elif b[1] > max2y:
                                max2y = b[1]
                            #oldcentR = centroid1
                            
                        else:
                            
                            plt.scatter(b[0], b[1], color="black")
                            x_values = [b[0], centroid2[0]]
                            y_values = [b[1], centroid2[1]]
                            plt.plot(x_values, y_values, color="black")
                            
                            blkcount += 1
                            if b[0] < min1x:
                                min1x = b[0]
                            elif b[1] < min1y:
                                min1y = b[1]
                            elif b[0] > max1x:
                                max1x = b[0]
                            elif b[1] > max2y:
                                max2y = b[1]
                                
                        line_count += 1

                    
                
                print("===============================") 
                print(f'There Are {line_count-1} Data Points.')
                print("===============================") 
                print(f'centroid1: (x){centroid1[0]} (y){centroid1[1]}')
                print(f'centroid2: (x){centroid2[0]} (y){centroid2[1]}')   
                
                
                
                #plt.xlim(0,82)    #use this to set X scale 
                #plt.ylim(0,82)    #use this to set Y scale 
                plt.autoscale(True, 'both')     #this makes the graph view scaled to the points
                '''end loop'''
                print(f'old(x){oldcent1[0]} old(y){oldcent1[1]} | old2(x){oldcent2[0]} old2(y) {oldcent2[1]}')
                print(f'curr(x){centroid1[0]} curr(y){centroid1[1]} | curr(x){centroid2[0]} curr(y) {centroid2[1]}')
                if ((oldcent1[0] == centroid1[0]) and (oldcent1[1] == centroid1[1]) and (oldcent2[0] == centroid2[0]) and (oldcent2[1] == centroid2[1])):
                    different = False
                else:
                    oldcent1 = centroid1
                    oldcent2 = centroid2
                    centroid1 = [(max1x - min1x)/2, (max1y - min1y)/2]
                    centroid2 = [(max2x - min2x)/2, (max2y - min2y)/2]
                plt.pause(0.5)
                if different != False:
                    plt.cla()
        plt.ioff()
        plt.show()
        
    except:
        print("something broke")

#===================================================================
# We need to implement something like this to check if centroids are the same.
# While the euclidean check runs, add up mean x and y, calculate new centroid after.
#===================================================================
# while old1 != centroid1 and old2 != centroid2:
#     print("above")
#         old1 = centroid1
#         old2 = centroid2
#         centroid1 = [(mean1x/redcount), (mean1y/redcount)]
#         centroid2 = [(mean2x/blkcount), (mean2y/blkcount)]
#     print("below")
#===================================================================

def euclid(cent, A):

    x = ((float(A[0]) - cent[0])**2)
    y = ((float(A[1]) - cent[1])**2)
    #print(f'euclid: {math.sqrt(x+y)}')
    return math.sqrt(x+y)
main()
