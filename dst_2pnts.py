#compute distance between two points (x1,y1) and (x2,y2)
x1=float(input("Enter the x1 value"))
y1=float(input("Enter the y1 value"))
x2=float(input("Enter the x2 value"))
y2=float(input("Enter the y2 value"))
distance=((x2-x1)**2+(y2-y1)**2)**0.5
print("The distance between two points is",distance)
