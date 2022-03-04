#1. Generate positive list of numbers from a given list of integers

list1=[]
n=int(input("Enter the limit : "))
for i in range(0,n):
    list1.append(int(input()))
print("List of postive integers ")
for x in list1:
    if(x>0):
        print(x,"\t",end="")
