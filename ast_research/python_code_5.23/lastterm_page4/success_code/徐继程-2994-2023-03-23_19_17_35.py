lst=list(eval(input()))
n,m=eval(input())
if n>=len(lst):
    print('error')
else:
    for i in range(m):
        lst.append(n+1)
    print(lst)
