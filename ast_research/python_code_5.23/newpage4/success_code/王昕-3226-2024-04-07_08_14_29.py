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
            return "False"#最开始这里使用的为print("False")
        else:
            return x#同上





nums = eval(input())
y = search(nums)
print(y)


