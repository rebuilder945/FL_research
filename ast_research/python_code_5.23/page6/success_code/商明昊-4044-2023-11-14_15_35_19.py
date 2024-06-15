def sxh(x):
    ls = list(str(x))
    n = 0
    for i in ls:
        i=int(i)
        n = n +i*i*i
    if n == x:
        print(n)
x = eval(input())
for i in range(1,x+1):
    sxh(i)


