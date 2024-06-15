def search(a):
    for x in a:
        while a.count(x)> len(a)//2:
            x=x
        else:
            x=int(False)
    return x





nums = eval(input())
y = search(nums)
print(y)


