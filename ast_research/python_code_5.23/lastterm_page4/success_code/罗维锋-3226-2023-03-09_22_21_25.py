def search(num):
    n=len(num)
    m=[]
    for i in range(n):
        if num.count(num[i])>(n/2):
            m.append(num[i])
            m=list(set(m))
    if m==[]:
        x='False'
    else:
        x=m[0]
    return x





nums = eval(input())
y = search(nums)
print(y)


