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
    if bool(ls2)==False:
        print("False")
    else:
        for i in ls2:
            print(i)
     return        
    





nums = eval(input())
y = search(nums)
print(y)


