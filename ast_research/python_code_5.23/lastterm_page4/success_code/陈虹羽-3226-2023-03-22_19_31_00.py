def search(x):
    y=len(x)
    for i in x:
        a=x.count(i)
        if a>=i//2:
            return i
        else:
            return False
          





nums = eval(input())
y = search(nums)
print(y)


