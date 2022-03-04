"3. Find the sum of all items in a lis"

n=int(input("Enter range of list : "))

lst1=[]
for i in range(n):
    lst1.append(int(input()))

print("Sum of list is ",sum(lst1))