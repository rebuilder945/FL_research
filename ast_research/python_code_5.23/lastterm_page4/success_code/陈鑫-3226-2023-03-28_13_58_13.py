def search(a):
    for i in range(len(a)):
        if a.count(a[i])>len(a)/2:
            b=a[i]
        else:
            b=bool(a.count(a[i])<=len(a)/2)

    return b





nums = eval(input())
y = search(nums)
print(y)


