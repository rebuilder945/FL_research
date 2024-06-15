def search(a):
    for x in a:
        if a.count(x)<=len(a)//2:
            continue
        else:
            return x





nums = eval(input())
y = search(nums)
print(y)


