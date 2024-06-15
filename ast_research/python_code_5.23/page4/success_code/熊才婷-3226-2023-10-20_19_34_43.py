def search(nums):
    n=len(nums)//2
    ls=[]
    for i in nums:
        d=0
        for x in nums:
            if x==1:
                d+=1
        if d>n:
            ls.append(i)
    ls2=[]
    for i in ls:
        if i not in ls2:
            ls2.append(i)
    a=ls2[0]
    return a





nums = eval(input())
y = search(nums)
print(y)


