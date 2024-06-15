def search(x):
    for y in x:
        if x.count(y) > len(x)//2:
            return x
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)


