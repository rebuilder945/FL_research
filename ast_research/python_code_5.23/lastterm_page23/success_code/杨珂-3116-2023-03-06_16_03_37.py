A=input()
B=input()
date=A.split(',')
date=[eval(x) for x in date]
date2=B.split(',')
date2=[eval(x) for x in date2]
L=((date[0]-date2[0])**2+(date2[1]-date[1])**2)**(1/2)
print("%.2f"%L)
