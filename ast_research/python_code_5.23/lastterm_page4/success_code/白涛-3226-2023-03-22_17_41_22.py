def search(n):
    a=list(n)
    b=max(a,key=a.count)
    c=a.count(b)
    if c>len(a)/2:
        print(b)
    else:
        print("False")
            





nums = eval(input())
y = search(nums)
print(y)


