#26 Joyal Jose

import csv

colum_name=input("Enter Column name:")

with open('username.csv','r') as csvf:
    data=csv.DictReader(csvf,delimiter=";")
    print("conten of "+colum_name+" is ")
    for row in data:
        print(row[colum_name])