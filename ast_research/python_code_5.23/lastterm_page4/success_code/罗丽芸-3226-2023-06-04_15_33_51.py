def search(nums):
    a=[]
    b=len(nums)/2
    for x in nums:
        c=nums.count(x)
        if c>b:
            a.append(x)
    if a==[]:
        return False
   





nums = eval(input())
y = search(nums)
print(y)


