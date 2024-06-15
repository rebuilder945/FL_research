A=input('x1,y1')
B=input('x2,y2')
date1=A.split(',')
date2=B.split(',')
date1=[float(x) for x in date1]
date2=[float(y) for y in date2]
s1=(date1[0]-date2[0])**2
s2=(date1[1]-date2[1])**2
s=(s1+s2)**(1/2)
print('%.2f'%(s))
