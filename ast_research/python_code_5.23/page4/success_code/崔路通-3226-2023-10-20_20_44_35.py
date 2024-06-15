def search(a):
    for i in range(len(a)):
        if a.count(a[i])>(len(a)//2):
            y=a[i]
        elif i==len(a):
            y="False"
    return y





nums = eval(input())
y = search(nums)
print(y)


