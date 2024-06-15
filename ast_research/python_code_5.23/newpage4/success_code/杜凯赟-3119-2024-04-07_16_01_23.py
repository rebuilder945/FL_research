nums = eval(input())
nums.reverse()
res = []
for num in nums:
    if num not in res:
     res.append(num)
res.reverse()

