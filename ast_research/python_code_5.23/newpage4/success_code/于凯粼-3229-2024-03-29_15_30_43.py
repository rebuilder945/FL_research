nums=eval(input())
res=[]
for num in nums:
    if num not in res:
        res.append(num)
print(res)
