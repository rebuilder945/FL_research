list1=eval(input())
m,n=eval(input())
if m<len(list1) and n<len(list1):
    if m<n:
        for i in range(n-m):
            del list1[m]
    print(list1)
    if m>n:
        for i in range(m-n):
            del list1[n]
    print(list1)
else:
    print("error")





