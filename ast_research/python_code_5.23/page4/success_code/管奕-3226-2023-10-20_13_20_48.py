def search(a):
    a=eval(input())
    n=len(a)
    for i in range(a):
        if a.count(i)>(n//2):
            print(i)
        else:
            print('False')
    return(a)
        





nums = eval(input())
y = search(nums)
print(y)


