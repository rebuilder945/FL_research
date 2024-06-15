def search(x):
    for i in x:
        while x.count(i)>len(x)//2:
            return i
        else: 
            return "Flase"






nums = eval(input())
y = search(nums)
print(y)


