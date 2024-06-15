lst=eval(input())
n,m=eval(input())
c=len(lst)
if n not in range(c) or m not in range(c):
    print('error')
else:
    del lst[n:m+1]
    print(lst)

