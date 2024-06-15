def search(nums):
    maxcount = []
    for x in range(nums):
        C=count(x)
        maxcount.append(C)
    if max(maxcount)>len(nums)/2:
        M=max(maxcount)
        return M
    else:
    M = False
    return M
    





nums = eval(input())
y = search(nums)
print(y)


