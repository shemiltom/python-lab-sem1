""""4. Generate a list of four digit numbers in a given range with all their digits even and the
 number is a perfect square. """

a=int(input("Enter the range-1 : "))
b=int(input("Enter the range-2 : "))
for i in range(a,b):
    for j in range(32,100,1):
        if i==j*j:
            string=str(i)
            if int(string[0])%2==0 and int(string[1])%2==0 and int(string[2])%2==0 and int(string[3])%2==0:
               print(i)
