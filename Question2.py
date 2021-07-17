import csv 
import matplotlib.pyplot as plt

try:
    with open('datasetQ2.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line = ','.join(row)
            if line_count == 0:
                print(f'Features:\n {"  ,  ".join(row)}')
                line_count += 1
            else:
                a = line.split(',', 1)
                plt.scatter(float(a[0]), float(a[1]))
                print(a)
                line_count += 1
        print(f'There Are {line_count-1} Data Entries.')
    plt.show()
except:
    print("something broke")
