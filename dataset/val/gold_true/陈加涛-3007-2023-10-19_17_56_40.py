list1=eval(input())
n,m=eval(input())
if n<=len(list1) and m<=len(list1):
    if n<=m:
        del list1[n:m]
        print(list1)
    elif n>m:
        del list1[m:n]
        print(list1)
else:
    print('error')
