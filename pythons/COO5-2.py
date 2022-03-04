#26 Joyal Jose

with open("text.txt",'r') as file:
    output=file.readlines()

print("\n Content of first file is          :",output)

with open("text.txt",'w') as file:
    file.write(str(output[::2])[1:-1])
print("\n Content of second file is          :",str(output[::2])[1:-1])


