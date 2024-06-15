def search(a):
    c = len(a)//2
    for x in a:
        b = a.count(x)
        if b > c:
            return x
        else:
            return 0





nums = eval(input())
y = search(nums)
print(y)


