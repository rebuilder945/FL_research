def search(x):
    for i in range(0,len(x)):
        a=x.count(x[i])
        if a>len(x)/2:
            return x[i]
            break
        else:
            return 'False'





nums = eval(input())
y = search(nums)
print(y)


