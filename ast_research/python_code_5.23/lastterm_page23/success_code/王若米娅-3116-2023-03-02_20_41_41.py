x1,y1=map(int,input().split(','))
x2,y2=map(int,input().split(','))
n=((x1-x2)*2+(y1-y2)*2)**0.5
print('%.2f'%n)
