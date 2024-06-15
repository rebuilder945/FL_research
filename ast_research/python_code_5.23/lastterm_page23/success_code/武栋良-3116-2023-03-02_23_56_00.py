x1,y1 = input().split(',')
x1 = x1-48
y1 = y1-48
x2,y2 = input().split(',')
x2 = x2-48
y2 = y2-48
e = ((x1-x2)**2+(y1-y2)**2)**0.5
print("%.2f"%(e))


