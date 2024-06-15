def search(a):
    b=False
    for x in a:
        if a.count(x)>len(a)//2:
            b=x
    return b





nums = eval(input())
y = search(nums)
print(y)


