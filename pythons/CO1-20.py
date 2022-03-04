#26 JOYAL JOSE
"20. From a list of integers, create a list removing even numbers. "

size=int(input("Enter size of list : "))
lst_int=[]
print("Enter numberS : ")
for i in range(size):
    lst_int.append(int(input()))
lst_rm_int=[]
lst_rm_int=[ i for i in lst_int if i%2==1]
print("list removing even numbers : ",lst_rm_int)