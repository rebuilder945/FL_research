def search(x):
    l=len(x)/2
    for i in x:
        if x.count(i)>l:
            return i
    else:
        return False






nums = eval(input())
y = search(nums)
print(y)


