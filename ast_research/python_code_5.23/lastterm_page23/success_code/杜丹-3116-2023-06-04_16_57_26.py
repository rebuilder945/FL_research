A=input()
B=input()
A=A.split(",")
B=B.split(",")
x1=eval(A[0])
y1=eval(A[1])
x2=eval(B[0])
y2=eval(B[1])
distance=(((x1-x2)**2+(y1-y2)**2)**0.5)
print(distance)


