lst=eval(input())
maxnum=max(lst)
minnum=min(lst)
nums=lst.copy()
for num in nums:
    if num==maxnum or num==minnum:
        lst.remove(num)
print(lst)
