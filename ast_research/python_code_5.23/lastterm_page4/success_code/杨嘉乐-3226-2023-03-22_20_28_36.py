def search(a):
    for i in a:
        if i>0.5*a.count(i):
            return i





nums = eval(input())
y = search(nums)
print(y)


