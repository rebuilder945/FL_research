def search(nums):
    n=len(nums)
    counts={}
    degree=0
    for num in nums:
        if num in counts:
            counts[num]+=1
        else:
            counts[num]=1
    degree=max(degree,counts[num])
    if degree>n/2
        return degree
    else:
        False





nums = eval(input())
y = search(nums)
print(y)


