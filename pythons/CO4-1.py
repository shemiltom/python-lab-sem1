""""1. Create Rectangle class with attributes length and breadth and methods to find area and
perimeter. Compare two Rectangle objects by their area. """
class rectangle():
    length=0
    breadth=0
    def __init__(self):
        self.breadth=float(input("Enter the breadth : "))
        self.length=float(input("Enter the length   : "))
    def area(self):
        return self.breadth*self.length
    def peri(self):
        return 2*(self.breadth+self.length)
print(" Rectangle -1\n-------------")
rec1=rectangle()
print("\n Rectangle -2\n-------------")
rec2=rectangle()
print("\n Rectangle -1\n-------------")
print("Area of rectangle : ",rec1.area())
print("Perimeter of rectangle : ",rec1.peri())
print("\n Rectangle -2\n-------------")
print("Area of rectangle : ",rec2.area())
print("Perimeter of rectangle : ",rec2.peri())
if(rec1.area()>rec2.area()):
    print("Rectangle-1 have large area")
elif(rec1.area()<rec2.area()):
    print("Rectangle-2 have large area")
else:
    print("Both have same area")