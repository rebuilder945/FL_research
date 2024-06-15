def Fibonacci(num,  n):
    last=num[0];
    now=num[1];
    fibnext=1for i in range(n):
        if i<2:
            fibnext=1
        else:
            fibnext=last+nowlast=nownow=fibnextreturn fibnext




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


