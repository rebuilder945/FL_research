nums = input()
a=[]
for num in nums:
    if num.isdigit():
        a.append(num)
b=sorted(a,reverse=True)
c=''.join(b)
if num[0]==0:
    c=0
print(c)
