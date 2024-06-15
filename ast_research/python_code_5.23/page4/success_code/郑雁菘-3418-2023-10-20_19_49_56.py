def maxsum(nums):
     import random
     X = eval(input())
     A = random.sample(X,2)
     for i in A:
        if i in X:
            X.remove(i)
     list.sort(A)
     list.sort(X)
     SUM = A[0] + X[0]


    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

