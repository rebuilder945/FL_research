nums=eval(input())
a=max(nums)
b=min(nums)
res=[]
for x in nums:
    if not (x==a or x==b):
        res.append(x)
print(res)
