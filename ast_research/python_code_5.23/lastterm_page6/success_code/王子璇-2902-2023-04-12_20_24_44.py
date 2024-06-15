def f(n):
    if n<=2:
        return(n)
    return f(n-1)+f(n-2)
n=eval(input())
a=0
for i in range(1,n+1):
    a+=f(i+1)/f(i)
print('%.4f'%a)

