import math
a = float(input("Enter side a of Triangle"))
b = float(input("Enter side b of Triangle"))
c = float(input("Enter side c of Triangle"))
s = float((a+b+c)/2)
print("Area of Triangle is:: ",math.sqrt(s*(s-a)*(s-b)*(s-c)))
