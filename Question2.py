import csv 
import matplotlib.pyplot as plt
import math
from time import sleep

def main():

    centroid1 = [20.0, 40.0]
    centroid2 = [50.0, 10.0]
    oldcent1 = [0,0]
    oldcent2 = [0,0]

    max1x = 0
    max1y = 0
    min1x = 100
    min1y = 100
    redcount = 0
    
    max2x = 0
    max2y = 0
    min2x = 100
    min2y = 100
    blkcount = 0
    
    different = True
    b = [0,0]

    try:
        plt.ion()
        while different == True:
            '''start loop above'''
            with open('datasetQ2.csv', mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
             
                for row in csv_reader:

                    if line_count == 0:
                        print(f'Features: {"  ,  ".join(row)}')
                        line_count += 1            
                    else:                   
                        line = ','.join(row)
                        
                        plt.scatter(float(centroid1[0]), float(centroid1[1]), color="blue")
                        plt.scatter(float(centroid2[0]), float(centroid2[1]), color="blue")
                        a = line.split(',', 1)
                        b = [float(a[0]), float(a[1])]
                        e1 = euclid(centroid1, b)
                        e2 = euclid(centroid2, b)
                       
                        print(f'line({line_count}) {b[0]} | {b[1]}')
                        if(e1 <= e2):

                            plt.scatter(b[0], b[1], color="red")
                            x_values = [b[0], centroid1[0]]
                            y_values = [b[1], centroid1[1]]
                            plt.plot(x_values, y_values, color="red")
                            
                            redcount += 1
                            if line_count == 1:
                                min1x = b[0]
                                min1y = b[1]
                                max1x = b[0]
                                max1y = b[1]
                            else:   
                                if b[0] < min1x:
                                    min1x = b[0]
                                elif b[1] < min1y:
                                    min1y = b[1]
                                elif b[0] > max1x:
                                    max1x = b[0]
                                elif b[1] > max1y:
                                    max1y = b[1]
                            
                        else:
                            plt.scatter(b[0], b[1], color="black")
                            x_values = [b[0], centroid2[0]]
                            y_values = [b[1], centroid2[1]]
                            plt.plot(x_values, y_values, color="black")
                            
                            blkcount += 1
                            if line_count == 1:
                                min2x = b[0]
                                min2y = b[1]
                                max2x = b[0]
                                max2y = b[1]
                            else:  
                                if b[0] < min2x:
                                    min2x = b[0]
                                elif b[1] < min2y:
                                    min2y = b[1]
                                elif b[0] > max2x:
                                    max2x = b[0]
                                elif b[1] > max2y:
                                    max2y = b[1]           
                        line_count += 1

                plt.xlim(0, 80)
                plt.ylim(0, 80)
                if ((oldcent1[0] == centroid1[0]) and (oldcent1[1] == centroid1[1]) and (oldcent2[0] == centroid2[0]) and (oldcent2[1] == centroid2[1])):
                    different = False
                else:
                    oldcent1 = centroid1
                    oldcent2 = centroid2
                    centroid1 = [(max1x + min1x)/2, (max1y + min1y)/2]
                    centroid2 = [(max2x + min2x)/2, (max2y + min2y)/2]
                plt.pause(0.25)
                if different != False:
                    plt.cla()
            redcount = 0
            blkcount = 0
        plt.ioff()
        plt.show()
        
    except:
        print("something broke")

def euclid(cent, A):
    
    x = ((A[0] - cent[0])**2)
    y = ((A[1] - cent[1])**2)
    #print(f'euclid: {math.sqrt(x+y)}')
    return math.sqrt(x+y)
main()
