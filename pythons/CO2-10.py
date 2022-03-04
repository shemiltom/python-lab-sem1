"10. Generate all factors of a number."

number=int(input('Enter a number : '))
factors=[i for i in range(1,number+1) if number%i==0]
print("Factors of {} are {}".format(number,factors))