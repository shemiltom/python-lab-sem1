"""3. Create a class Rectangle with private attributes length and width. Overload ‘<’ operator to
compare the area of 2 rectangles."""

class Rectangle:
    __length = 0
    __width = 0
    __area = 0

    def __init__(self):
        self.length = int(input("Enter length : "))
        self.width = int(input("Enter width   : "))
        self.area = self.length * self.width

    def __lt__(self, obj):
        print(self.area)
        print(obj.area)
        return self.area < obj.area

print(" Rectangle-1\n-------------")
obj1 = Rectangle()
print(" Rectangle-2\n-------------")
obj2 = Rectangle()
if (obj1 < obj2):
    print("second rectangle have larger area ", obj2.area)
else:
    print("first rectangle have larger area ", obj1.area)
