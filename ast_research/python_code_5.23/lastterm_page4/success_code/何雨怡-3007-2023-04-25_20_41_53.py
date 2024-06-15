lst=eval(input())
n,m=eval(input())
lstcopy=lst.copy()
if n>m or m>=len(lst):
    print('error')
else:
    cut1=lst[0:n]
    cut2=lst[m:]
    final=cut1+cut2
    print(final)
