ls=eval(input())
a=max(ls)
b=min(ls)
nums=ls.copy()
for num in nums:
    if num ==a or b:
        ls.remove(num)
print(ls)
