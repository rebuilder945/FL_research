n=int(input())
nums=list(range(n))
for i in nums:
    if i==1:
        nums.remove(1)
        nums.append(1)
    else:
        pass
print(nums)
