n=eval(input())
nums=[x for x in range(1,n+1)]
a=nums.pop(0)
nums.append(a)
print(nums)
