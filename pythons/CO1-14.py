#26 JOYAL JOSE

"14. Accept an integer n and compute n+nn+nnn."
n=(input("enter the number: "))
a=int(input("Enter the limit : "))
sum=0
for i in range(1,a+1):
   sum=sum+int(n*i)
print(sum)