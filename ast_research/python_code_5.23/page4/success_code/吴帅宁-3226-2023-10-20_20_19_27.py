def search(a):
    z=1
    for x in a:
        if a.count(x)>=z:
            y=a.count(x)
        else:
           print("False.")
        return x





nums = eval(input())
y = search(nums)
print(y)


