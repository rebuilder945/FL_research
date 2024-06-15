x1,y1 = input().split(',')
x1 = atof(x1)
y1 = atof(y1)
x2,y2 = input().split(',')
x2 = atof(x2)
y2 = atof(y2)
e = ((x1-x2)**2+(y1-y2)**2)**0.5
print("%.2f"%(e))


