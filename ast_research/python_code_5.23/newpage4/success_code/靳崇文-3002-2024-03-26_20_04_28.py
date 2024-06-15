# from ctypes.wintypes import INT


A=list(eval(input()))
B=len(A)
C=sum(A)
D=C/B
if D%1==0:
    print("%d"%D)
else:
    print("%.2f"%D)
