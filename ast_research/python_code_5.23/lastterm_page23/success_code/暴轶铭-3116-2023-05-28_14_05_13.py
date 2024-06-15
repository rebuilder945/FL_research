x1,y1 = eval(input().split(","))
x2,y2 = eval(input().split(","))
distance = ((x1-x2)**2+(y1-y2)**2)**0.5
print("%.2f"%(distance))
