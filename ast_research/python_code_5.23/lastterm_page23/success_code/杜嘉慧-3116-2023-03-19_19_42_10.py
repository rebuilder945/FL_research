x1,y1 = map(int,input())
x2,y2 = map(int,input())
a = ((x1 - x2) ^ 2 + (y1 - y2) ^ 2) ^ 1 / 2
print("%.2f"%a)
