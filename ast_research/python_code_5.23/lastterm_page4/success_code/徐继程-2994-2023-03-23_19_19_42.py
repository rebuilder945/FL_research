lst=list(eval(input()))
n,m=eval(input())
if n>=len(lst):
    print('error')
else:
    for i in range(m):
        a=lst(n+1)
        lst.append(a)
    print(lst)
