def search(x):
    return [i for i in x if x.count(i)>len(x)//2][0]





nums = eval(input())
y = search(nums)
print(y)


