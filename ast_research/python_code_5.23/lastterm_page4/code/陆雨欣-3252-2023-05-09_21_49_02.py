def sushu(lst):
    lst2=[]
    for i in lst:
        if i>=2:
            for j in range(2,i,1):
                if i % j==0:
                    break
            else：
                lst2.append(i)
     print(lst2)

lst=eval(input())
sushu(lst) 




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


