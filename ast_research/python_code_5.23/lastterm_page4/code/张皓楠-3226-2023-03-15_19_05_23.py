def search(a)
    for i in a:
        if a.count(i)>len(a)/2:
            return i





nums = eval(input())
y = search(nums)
print(y)


