#26 JOYAL JOSE

"Create a list of colors from comma-separated color names entered by user. Display first and last colors."

n=input("enter the colours:")
splt1=n.split(",")
print(splt1)
fst=splt1[0]
lst=splt1[-1]
print(fst,lst)