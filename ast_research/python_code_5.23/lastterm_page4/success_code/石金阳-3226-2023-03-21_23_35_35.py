def search(y):
    n=len(y)
    for x in y:
        if y.count(x)>n/2:
          z=x
        else:
           False
    return z






nums = eval(input())
y = search(nums)
print(y)


