a=int(input())
for b in range(100,a+1):
    A=b[0]
    B=b[1]
    C=b[2]
    if int(A)**3+int(B)**3+int(C)**3==int(b):
        print('b\n')
    else:
        print('none')
