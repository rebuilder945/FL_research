def search(nums):
    y=[]
    b=[]
    for i in nums:
        if nums.count(i)>(len(i)//2):
            b.append(i)
            if i not in y:
                y.append(i)
        else:
            pass
    if len(y)==1:
        y=y[0]
    else:
        y="False"
    return y





nums = eval(input())
y = search(nums)
print(y)


