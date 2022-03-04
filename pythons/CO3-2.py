""""2. Create a package graphics with modules rectangle, circle and sub-package 3D-graphics with
modules cuboid and sphere. Include methods to find area and perimeter of respective figures
in each module. Write programs that finds area and perimeter of figures by different importing
statements. (Include selective import of modules and import * statements)"""

from graphics import circle
from graphics.rectangle import *
from graphics.D_graphics import cuboid , sphere

r=int(input("Enter radius of circle : "))
print("Area of Circle      : ",circle.area(r))
print("Perimeter of Circle : ",circle.perimeter(r))
print("____________________________________________")
l=int(input("Enter length of rectangle  : "))
b=int(input("Enter breadth of rectangle : "))
print("Area of Rectangle       :",area(l,b))
print("perimeter  of Rectangle :",perimeter(l,b))
print("______________________________________________")
l=int(input("Enter length of cuboid  : "))
b=int(input("Enter breadth of cuboid : "))
h=int(input("Enter length of cuboid  : "))
print("Area of cuboid       : ",cuboid.area(l,b,h))
print("Perimeter of cuboid  : ", cuboid.perimeter(l,b,h))
print("__________________________________________________")
r=int(input("Enter radius of sphere : "))
print("Area of sphere         : ",sphere.area(r))
print("surface area of Sphere : ",sphere.perimeter(r))
print("_______________________________________________________")