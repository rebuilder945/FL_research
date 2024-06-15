def search(a):
    for x in a:
        b=a.count(x)
        c=[]
        d=[]
        if b>len(a)/2:
            c.append(x)
        else:
            d.append(x)
        if len(c)==0:
            print("False")
        else:
            print(x)





nums = eval(input())
y = search(nums)
print(y)


