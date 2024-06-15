def search(num):
    m=0
    long=len(num)//2
    for i in num:
        if num.count(i)>long:
            m==i
    if m=0:
        return False
    else:
        return m





nums = eval(input())
y = search(nums)
print(y)


