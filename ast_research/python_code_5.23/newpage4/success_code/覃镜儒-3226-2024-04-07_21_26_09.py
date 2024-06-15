def search(nums):
    y=[]
    for i in nums:
        if nums.count(i)>1:
            y.append(i)
        else:
            pass
    if len(y)>1:
        return(y)
    else:
        y="False"





nums = eval(input())
y = search(nums)
print(y)


