AcoordinateX,AcoordinateY = eval(input())
BcoordinateX,BcoordinateY = eval(input())
Distance = ((AcoordinateX - BcoordinateX)**2 + (AcoordinateY - BcoordinateY)**2)**0.5
print("%.2f"%Distance)

