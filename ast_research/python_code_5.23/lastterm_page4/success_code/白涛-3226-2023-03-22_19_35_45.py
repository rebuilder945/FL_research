def search(n):
    a=list(n)
    b=max(a,key=a.count)
    c=a.count(b)
    if c>len(a)/2:
        return(b)
    else:
        return('False')
            





nums = eval(input())
y = search(nums)
print(y)


