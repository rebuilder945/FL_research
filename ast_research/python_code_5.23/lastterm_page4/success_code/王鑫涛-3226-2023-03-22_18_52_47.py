def search(a):
    n=len(a)
    i=n//2
    for x in a:
        if a.count(x)>i:
            return x
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)


