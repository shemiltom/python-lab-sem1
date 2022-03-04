"2.Generate Fibonacci series of N terms"

n=int(input("Enter the limit : "))
a=0
b=1
print("\n Fibnocci Series : ")
print("\t",a,"\t",b,"\t",end="")
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c,"\t",end="")