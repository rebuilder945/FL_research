lst=eval(input())
m=max(lst)
n=min(lst)
nums=lst.copy()
for num in nums:
    if num==m or num==n:
        lst.remove()
print(lst)

