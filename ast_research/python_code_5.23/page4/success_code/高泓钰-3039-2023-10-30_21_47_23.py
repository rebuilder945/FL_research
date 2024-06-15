ls=eval(input())
max=max(ls)
min=min(ls)
nums=ls[:]
for i in nums:
    if i==max or i==min:
        ls.remove(i)
print(ls)
