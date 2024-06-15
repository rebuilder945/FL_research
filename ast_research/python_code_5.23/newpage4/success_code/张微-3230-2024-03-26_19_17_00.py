nums = input()
a=[]
for num in nums:
    if num.isdigit():
        a.append(num)
b=sorted(a,reverse=True)
c=''.join(b)
print(c)
