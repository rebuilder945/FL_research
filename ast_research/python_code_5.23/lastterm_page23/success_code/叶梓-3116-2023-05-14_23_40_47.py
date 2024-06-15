import math
A=input()
B=input()
A=A.split(',') 
B=B.split(',')
x1=float(A[0]) #坐标数值不一定是整数，float表示小数，小数也可表示整数
y1=float(A[1])
x2=float(B[0])
y2=float(B[1])
d=math.sqrt((x1-x2)**2+(y1-y2)**2) #sqrt()用来求给定值的平方根
print("%.2f"%d)
