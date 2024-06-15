x1,y1 = map(int,input().split(','))
x2,y2 = map(int,input().split(','))
dis = ((x1-x2)**2+(y1-y2)**2)**(1/2)
print('%.2f'%dis)
