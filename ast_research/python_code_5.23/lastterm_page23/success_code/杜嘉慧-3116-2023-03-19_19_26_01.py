x1, y1 = int(input()) or float(input())
x2, y2 = int(input()) or float(input())
a = ((x1 - x2) ^ 2 + (y1 - y2) ^ 2) ^ 1 / 2
print("%.2f"%a)
