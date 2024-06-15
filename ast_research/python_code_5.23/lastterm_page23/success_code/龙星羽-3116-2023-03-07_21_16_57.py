x1,y1=map(eval,input().split(","))
x2,y2=map(eval,input().split(","))
d=((x1-x2)**2+(y1-y2)**2)**0.5
print('{:.2f}'.format(d))
