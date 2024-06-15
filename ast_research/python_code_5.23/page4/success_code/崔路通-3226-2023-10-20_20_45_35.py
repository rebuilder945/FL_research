def search(a):
    for i in range(len(a)):
        if a.count(a[i])>(len(a)//2):
            c=a[i]
            break
        elif i==len(a):
            c="False"
    return c





nums = eval(input())
y = search(nums)
print(y)


