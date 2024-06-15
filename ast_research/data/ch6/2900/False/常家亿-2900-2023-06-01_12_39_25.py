def huisu(x):
    for i in range(2,x):
        if x%i ==0:
            return -1
    str1 = str(x)#不能放在上一个循环中，因为执行是一个一个执行的，而我要的结果是执行完所有i之后的
    for t in range(len(str1)):
        m = len(str1)
        if str1[t] == str1[m-t-1]:
            return x
        else:
            return -1
n = eval(input())
lst =[]
if n < 0 or type(n) == float:
    print('illegal input')
else:
    for c in range(2,n+1):
        if huisu(c) != -1:
            lst.append(c)
    print(' '.join(str(x) for x in lst))






