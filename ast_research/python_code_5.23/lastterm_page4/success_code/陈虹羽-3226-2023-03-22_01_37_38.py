def search(x):
    y=len(x)
    for i in x:
        a=x.count(i)
        if a>=i//2:
            h=i
            break
        else:
            i="False"
    return h
          





nums = eval(input())
y = search(nums)
print(y)


