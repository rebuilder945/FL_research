lst=list(eval(input()))
n,m=eval(input())
if n>=len(lst):
    print('error')
else:
    if n>=0:
        for i in range(m):
            a=lst[n-1]
            lst.append(a)
    else:
        for i in range(m):
            a=lst[n]
            lst.append(a)
    print(lst)
