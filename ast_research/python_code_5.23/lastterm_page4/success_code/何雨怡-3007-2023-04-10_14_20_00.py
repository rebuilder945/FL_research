lst=eval(input())
lst2=lst.copy
n,m=eval(input())
length=len(lst)
if n>m:
    print('error')
elif n>=length or m>=length:
    print('error')
elif n==m:
    del lst[n]
    print(lst)
elif n<m:
    cut1=lst[0:n]
    cut2=lst[m+1:]
    all=cut1+cut2
    print(all)

    

