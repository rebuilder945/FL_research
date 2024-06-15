nums=eval(input())
a=max(nums)
b=min(nums)
for num in nums:
    if num == a or num == b:
        nums.remove(num)
print(nums)
