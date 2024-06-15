def search(nums):
    n=len(nums)//2
    ls=[]
    for i in nums:
        d=0
        for x in nums:
            if x==i:
                d+=1
        if d>n:
            ls.append(i) 
    if bool(ls)==False:
        print("False")
        else:
            x=ls[0]
            print(x)
    





nums = eval(input())
y = search(nums)
print(y)


