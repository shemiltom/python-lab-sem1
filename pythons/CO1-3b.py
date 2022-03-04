#Square of N numbers

list=[]
square=[]
n=int(input("Enter a limit : "))
print("Enter the numbers")
for i in range(n):
    list.append(int(input()))
print("Square of given numbers")
for x in list:
    a=x**2
    square.append(a)
print(square)
