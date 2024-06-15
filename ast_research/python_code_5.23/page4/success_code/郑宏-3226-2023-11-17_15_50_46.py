def search(x):
    a=len(x)
    b=a//2
    for i in x:
        c=x.count(i)
        if c>b:
            print(x[i])
            break





nums = eval(input())
y = search(nums)
print(y)


