def search(x):
    for y in range(x):
        if (y.count(x)>(len(y)//2)):
            return x
    return False





nums = eval(input())
y = search(nums)
print(y)


