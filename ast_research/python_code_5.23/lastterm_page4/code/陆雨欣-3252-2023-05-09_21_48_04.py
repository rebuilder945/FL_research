def sushu(1st):
    1st2=[]
    for i in 1st:
        if i>=2:
            for j in range(2,i,1):
                if i % j==0:
                    break
            else：
                1st2.append(i)
     print(1st2)

1st=eval(input())
sushu(1st) 




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


