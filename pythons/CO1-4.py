str=input("Enter ascntance : ")
str1=str.split()
setstr=set(str1)
dict1={}
for x in setstr:
    i=0
    for y in str1:
        if(x==y):
            i=i+1
    dict1.update({x:i})
print(dict1)
