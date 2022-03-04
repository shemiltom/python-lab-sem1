"8. Accept a list of words and return length of longest word "

word_list=[]
limit=int(input("Enter size of list : "))
print('Enter words')
for i in range(limit):
  word_list.append(input())
for i in word_list:
  a=max(word_list)
print("\n",a ," is the longest word and its size is ",len(a))