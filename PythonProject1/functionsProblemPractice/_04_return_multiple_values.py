import math

radius = int(input("enter radius:-"))

def circle_stats(radius):
    circumference = math.floor(2 * math.pi * radius)
    area = math.floor(math.pi * radius ** 2)
    return  circumference, area

c,a = circle_stats(radius)

print("circumference of circle is ",c,"area of circle is ",a)