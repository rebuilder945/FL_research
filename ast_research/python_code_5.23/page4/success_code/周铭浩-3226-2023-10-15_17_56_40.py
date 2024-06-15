def search(a):
    for x in a:
        if a.count(x)>len(a)/2:
            print(a)
        else:
            print('False')





nums = eval(input())
y = search(nums)
print(y)


