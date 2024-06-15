x1,y1=map(int,input().split(','))
x2,y2=map(int,input().split(','))
length=((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))**1/2
print("%.2f"%length)
