lst=list(eval(input()))
n,m=eval(input())
a=lst[n]
if n<=len(lst)+1:
    for i in range(m):
        lst.append(a)
    print(lst)
else:
    print('error')
