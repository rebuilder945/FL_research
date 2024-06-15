nums=eval(input())
for x in nums:
    if x==max(nums):
        nums.remove(x)
        while x in nums:
            nums.remove(x)
        break
for y in nums:
    if y ==min(nums):
        nums.remove(y)
        while y in nums:
            nums.remove(y)
        break
print(nums)
