def search(a):
    b=[]
    for i in a:
        if a.count(i)>1:
            b.append(i)
        if a.count(i)==1:
            print("False")
    return b





nums = eval(input())
y = search(nums)
print(y)


