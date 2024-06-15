A=input().split(",")
B=input().split(",")
x1=float(A[0])
x2=float(A[1])
y1=float(B[0])
y2=float(B[1])
s=((x1-x2)**2+(y1-y2)**2)**0.5
print(f"{s:.2f}")
