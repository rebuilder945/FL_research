def search(nums):
    y=[]
    b=[]
    for i in nums:
        if nums.count(i)>len(nums)//2:
            b.append(i)
            if i not in y:
                y.append(i)
            else:
                pass
        else:
            pass
    if len(y)==1:
        return i
    else:
        return False
    return y





nums = eval(input())
y = search(nums)
print(y)


