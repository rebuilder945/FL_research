x1,y1 = eval(input())
x2,y2 = eval(input())
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
distance = float((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
distance1 = distance**0.5
print("%.2f"%distance1) 
