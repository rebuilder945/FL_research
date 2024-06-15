def search(a):
    for x in a:
        if a.count(x) > len(a)//2:
            b=x
        else:
            b="False"
    return b






nums = eval(input())
y = search(nums)
print(y)


