lst=list(eval(input()))
n,m=eval(input())
if n>=len(lst):
    print('error')
else:
    if n>=0:
        for i in range(m):
            a=lst[n]
            lst.append(a)
    else:
        a=lst[n]
        for i in range(m):
            lst.append(a)
    print(lst)
