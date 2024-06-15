x1,y1=map(eval,input().split(","))
x2,y2=map(eval,input().split(","))
d=((abs(x1-x2))**2+(abs(y1-y2))**2)**1/2
print("%.2f"%(d))
