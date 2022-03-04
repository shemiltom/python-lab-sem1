"7. Add 'ing' at end of a given string . if already ends with 'ing' then add 'ly"

string=input("Enter a string : ")
if string.endswith('ing'):
  print(string+'ly')
else:
  print(string+'ing')