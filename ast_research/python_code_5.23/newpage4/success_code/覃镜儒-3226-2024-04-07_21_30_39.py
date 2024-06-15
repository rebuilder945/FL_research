def search(nums):
    y=[]
    for i in nums:
        if nums.count(i)>1 and i not in y:
            y.append(i)
        else:
            pass
    if len(y)>1:
        y=y[0]
    else:
        y="False"
    return y





nums = eval(input())
y = search(nums)
print(y)


