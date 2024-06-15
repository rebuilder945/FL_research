lst=eval(input())
nums=[]
for x in lst:
    if x not in nums:
        nums.append(x)
nums.sort(reverse=True)
a="".join(map(str,nums))
print(a)



