def Fibonacci(num,n):
    save=num
    for i in range(2,n):
        save.append(save[-1]+save[-2])#save加的时候加上前两项之和
    return save[-1]
num  =  [1,  1]
n  =  int(input())
print(Fibonacci(num,  n))