def search(a):
    c=[]
    for x in a:
        b=a.count(x)
        if b>len(a)/2:
            c.append(x)
            if len(c)!=0:
                print(c)
            else:
                print("False")
        





nums = eval(input())
y = search(nums)
print(y)


