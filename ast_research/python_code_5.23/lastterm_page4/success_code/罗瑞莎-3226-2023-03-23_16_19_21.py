def search(x):
    for i in x:
        if (x.count(i))>(len(x)//2):
            return i
    else:
        return False





nums = eval(input())
y = search(nums)
print(y)


