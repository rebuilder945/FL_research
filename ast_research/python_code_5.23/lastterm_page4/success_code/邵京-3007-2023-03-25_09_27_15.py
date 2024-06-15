list1=eval(input())
n,m=eval(input())
if n<=m<=len(list1):
    for i in range(n,m,1):
        del list1[i]
        
elif m<n<=len(list1):
    for i in range(m,n,1):
        del list1[i]
else:
    print('error')
print(list1)
