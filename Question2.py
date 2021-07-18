import csv 
import matplotlib.pyplot as plt
import math



def main():
    
    #probably add an outer loop here so that when kmean is calculated outside file processing it can be used again above
    #I think we should create a function to open file, read contents, convert to float, and then add it's [f1,f2] to a list
    centroid1 = [30.0, 50.0]
    centroid2 = [60.0, 50.0]
    #old1 = centroid1
    #old2 = centroid1
    mean1x = 0.0
    mean1y = 0
    mean2x = 0
    mean2y = 0
    redcount = 0
    blkcount = 0
    try:
        
        with open('datasetQ2.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            
            for row in csv_reader:
                line = ','.join(row)
                plt.scatter(float(centroid1[0]), float(centroid1[1]), color="blue")
                plt.scatter(float(centroid2[0]), float(centroid2[1]), color="blue")
                if line_count == 0:
                    print(f'Features:\n {"  ,  ".join(row)}')
                    line_count += 1
                else:
                    a = line.split(',', 1)
                    e1 = euclid(centroid1, a)
                    e2 = euclid(centroid2, a)
                    
                    if(e1 <= e2):
                        
                        plt.scatter(float(a[0]), float(a[1]), color="red")
                        redcount += 1
                        mean1x += float(a[0])
                        mean1y += float(a[1])
                        #oldcentR = centroid1
                        
                    else:
                        
                        plt.scatter(float(a[0]), float(a[1]), color="black")
                        blkcount += 1
                        mean2x += float(a[0])
                        mean2y += float(a[1])
                        #oldcentB = centroid2
                    #B[line_count][2] = [float(a[0]), float([1])]
                    print(a)
                    line_count += 1
                
               
            print(f'There Are {line_count-1} Data Points.')
            plt.show()
            
    except:
        print(" Make sure you are calling index values with float() ")

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
    print(f'(x) centroid: {cent[0]} A: {A[0]}')
    print(f'(y) centroid: {cent[1]} A: {A[1]}')
    x = ((float(A[0]) - cent[0])**2)
    y = ((float(A[1]) - cent[1])**2)
    print(f'euclid: {math.sqrt(x+y)}')
    return math.sqrt(x+y)
main()
