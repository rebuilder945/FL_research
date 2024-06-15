def search(nums):
    n=len(nums)//2
    ls=[]
    ls2=[]
    for i in nums:
        d=0
        for x in nums:
            if x==1:
                d+=1
        if d>n:
            ls2.append(i)
        for i in ls2:
            x=1       
    





nums = eval(input())
y = search(nums)
print(y)


