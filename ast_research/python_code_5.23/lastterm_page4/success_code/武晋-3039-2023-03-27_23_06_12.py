nums = eval(input())
maxnum = max(nums)
minnum = min(nums)
b={}
for x in nums:
    if x == maxnum or x ==minnum:
        b.remove(x)
print(b)
