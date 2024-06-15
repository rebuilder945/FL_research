def search(x):
    
    for x1 in x:
        if x.count(x1)>len(x):
            print(x1)
        else:
            print(False)






nums = eval(input())
y = search(nums)
print(y)


