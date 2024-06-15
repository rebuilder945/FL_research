def search(y):
    for x in y:
        if(y.count(x)>(len(y)/2)):
            h=x
        else:
       h=False
print(h)





nums = eval(input())
y = search(nums)
print(y)


