def search(nums):
    n=len(nums)//2
    ls=[]
    for i in nums:
        d=0
        for x in nums:
            if x==1:
                d+=1
        if d>n:
            break
    return i





nums = eval(input())
y = search(nums)
print(y)


