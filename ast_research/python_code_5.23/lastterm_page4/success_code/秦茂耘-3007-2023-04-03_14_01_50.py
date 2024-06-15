A=eval(input())
a,b=eval(input())
if  a > len(A):
    print('error')
else:
    del A[a:b]
    print(A)

