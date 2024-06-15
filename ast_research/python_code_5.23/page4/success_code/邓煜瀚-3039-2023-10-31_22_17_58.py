nums=eval(input())
a=max(nums)
b=min(nums)
tmp = nums.copy()
for num in nums:
    if num == a or num == b:
        tmp.remove(num)
print(nums)
