def fibonacci(num,n):
    if n==1:
        return 2
    if n==2:
        return 3
    else:
        return fibonacci(num,n-1)+fibonacci(num,n-2)
def fibonacci2(num2,n):
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        return fibonacci2(num2,n-1)+fibonacci2(num2,n-2)
num=[2,3]
num2=[1,2]
n=eval(input())
a=0
for x in range(1,n+1):
    a+=fibonacci(num,x)/fibonacci2(num2,x)
print('%.4f'%(a))










