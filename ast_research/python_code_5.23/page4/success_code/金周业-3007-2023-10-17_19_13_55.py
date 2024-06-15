list1=eval(input())
m,n=eval(input())
if m<n:
    for i in range(n-m):
        del list1[m]
    print(list1)
else:
    print("error")





