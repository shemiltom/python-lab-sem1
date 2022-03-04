"""
1.Program to find the factorial of a number
"""

n = int(input("Enter number : "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(n,"!=",fact)