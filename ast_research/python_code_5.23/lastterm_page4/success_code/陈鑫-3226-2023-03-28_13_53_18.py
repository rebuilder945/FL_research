def search(a):
    for i in range(len(a)):
        if a.count(a[i])>len(a)/2:
            b=a[i]
        elif a.count(a[i])<=len(a)/2:
            pass
        else:
            b="False"
    return b





nums = eval(input())
y = search(nums)
print(y)


