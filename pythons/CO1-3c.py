# Form a list of vowels selected from a given word
vowels=[]
vow={"a","A","e","E","i","I","o","O","u","U"}
str=input("Enter a word : ")
for i in str:
    for x in vow:
        if(i==x):
            vowels.append(i)
print("Vowels are")
print(vowels)