def search(x):
    y=len(x)
    for i in x:
        a=x.count(i)
        if a>y//2:
            return i
    return False





nums = eval(input())
y = search(nums)
print(y)


