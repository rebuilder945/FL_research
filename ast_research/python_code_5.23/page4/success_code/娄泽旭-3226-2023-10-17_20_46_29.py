def search(x):
    for i in x:
        while x.count(i)>len(x)//2:
            return i





nums = eval(input())
y = search(nums)
print(y)


