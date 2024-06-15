nums = eval(input())
nums.reverse()
res = []
for num in nums:
    if nums not in res:
        res.append(num)
res.reverse()
print(res)
