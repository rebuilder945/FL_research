def search(nums):
    n=len(nums)
    b=[]
    for a in nums:
        if a>=n//2:
            b.append(a)
        else:
            pass
    if b==[]:
        c="Error"
    else:
        c=max(b)
    return c





nums = eval(input())
y = search(nums)
print(y)


