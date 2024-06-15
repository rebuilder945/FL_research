def isprime(nums):
    for num in range(nums):
        for i in range(2,num):
            if num%i==0:
                return False
            else:
                return True
nums=eval(input())
res=isprime(nums)
print(res)
