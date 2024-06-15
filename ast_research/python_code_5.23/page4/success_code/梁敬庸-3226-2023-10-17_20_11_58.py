def search(n):
    b=[]
    for x in n:
        if n.count(x)>len(n)/2:
            if n not in b:
                b.append(n)
    if len(b)>0:
        print(b[0])
    else:
        print("False")






nums = eval(input())
y = search(nums)
print(y)


