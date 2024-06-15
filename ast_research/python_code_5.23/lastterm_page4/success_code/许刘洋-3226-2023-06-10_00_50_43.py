def search(a):
    for i in a:
        if a.count(i)>len(a)//2:
            return i
        else:print('False')
       






nums = eval(input())
y = search(nums)
print(y)


