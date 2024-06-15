def juli(x1,y1,x2,y2):
    length=((x1-x2)**2+(y1-y2)**2)**0.5
    return length
a=eval(input())
b=eval(input())
x1=a[0]
y1=a[1]
x2=b[0]
y2=b[1]
print("%.2f"%(juli(x1,y1,x2,y2)))
