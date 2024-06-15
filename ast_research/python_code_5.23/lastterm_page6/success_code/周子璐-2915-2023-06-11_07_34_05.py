a=int(input())
for b in range(150,a+1):
    B=str(b)
    A=B[0]
    B=B[1]
    C=B[-1]
    if int(A)**3+int(B)**3+int(C)**3==int(b):
        print(str(b))
print('none')
