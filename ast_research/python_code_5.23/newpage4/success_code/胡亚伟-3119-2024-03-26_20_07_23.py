nums=eval(input())
nums.revese()
res=[]
for num in nums:
    if num not in res:
        res.append(num)
res.reverse()
print(res)
