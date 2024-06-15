list=eval(input())
n,m=eval(input())
l=len(list)
if n>m:
    print('error')
elif n>=l or m>=l:
    print('error')
else:
    for i in range(n,m):
        del list[i]
    print(list)

