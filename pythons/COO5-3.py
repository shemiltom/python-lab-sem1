#26 Joyal Jose

import csv

with open('username.csv','r') as csvf:
    data=csv.reader(csvf,delimiter=";")
    for i in data:
        print(i)
