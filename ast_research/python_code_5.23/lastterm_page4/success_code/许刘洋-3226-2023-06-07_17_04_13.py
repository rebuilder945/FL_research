def search(a):
    for i in a:
        if len(i)>len(a)//2:
            return i
        break






nums = eval(input())
y = search(nums)
print(y)


