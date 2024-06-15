def search(x):
    num = 0
    for x1 in x:
        if x.count(x1) > len(x)/2:
            num = x1
    if num == 0:
        return "False"
    else:
        return num





nums = eval(input())
y = search(nums)
print(y)


