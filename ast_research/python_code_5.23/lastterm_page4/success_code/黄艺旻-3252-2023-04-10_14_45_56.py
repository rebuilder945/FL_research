def Fibonacci(nums,n):
     a=nums[0]
     b=nums[1]
     fibnext=1
     for i in range(n):
        if i<2:
            fibnext=1
        else:
            fibnext=a+b
            a=b
            b=fibnext
     return fibnext




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


