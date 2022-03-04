#Display future leap years from current year to a final year entered by user.
from datetime import date
a = date.today()
b = int(input("Enter a finishing Year : "))
print("The future leap years : ")
for yr in range(a.year, b):
   if (0 == yr % 4) and (0 != yr % 100) or (0 == yr % 400):
       print(yr)
