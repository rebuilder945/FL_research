def search(nums):
    a=len(nums)//2
    c=[]
    for i in nums:
        b=nums.count(i)
        if b>a:
            c.append(i)
            return c
        elif len(c)==0:
            return('False'






nums = eval(input())
y = search(nums)
print(y)


