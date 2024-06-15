nums=eval(input())
for x in nums:
    if x==0:
        nums.append(0)
        nums.remove(0)
print(nums)
