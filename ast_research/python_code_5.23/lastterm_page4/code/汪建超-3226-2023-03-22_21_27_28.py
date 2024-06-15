def search(nums):
    maxcount = []
    for x in range(nums):
        C=count(x)
        maxcount.append(C)
    if max(maxcount)>len(nums):
        M=max(maxcount)
        return M
    else:
    return False
    





nums = eval(input())
y = search(nums)
print(y)


