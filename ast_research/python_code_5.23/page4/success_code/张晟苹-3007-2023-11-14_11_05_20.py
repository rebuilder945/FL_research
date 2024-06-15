lst=eval(input())
n,m=eval(input())
if n>m or n>=len(lst):
    print('error')
else:
    lst1=lst[0:n]
    lst2=lst[m::]
    lst3=lst1+lst2
    print(lst3)
