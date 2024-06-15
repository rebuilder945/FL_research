def search(x):
    a=len(x)
    b=a//2
    for i in range(a):
        c=x.count(x[i])
        if c>b:
            print(c)
            break





nums = eval(input())
y = search(nums)
print(y)


