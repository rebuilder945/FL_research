def Fibonacci(n):
    num = [1,1]
    a=num[0]
    b=num[1]
    fibnext=1
    for i in range(n):
        if i<2:fibnext=1
        else:fibnext=a+b
        a=b
        b=fibnext
    return fibnext
n = eval(input())
list1 = []
for i in range(n+3):
    number = Fibonacci(i)
    list1.append(number)
del list1[0:2]
list2 = list1.copy()
del list1[-1]
del list2[0]
answer = 0
for i in range(len(list1)):
    a = list2[i]/list1[i]
    answer = answer + a
print("%.4f"%(answer))
