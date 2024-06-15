a=eval(input())
lst=list(a)
n,m=eval(input())
if m>len(lst)-1 or n>len(lst)-1:
    print("error")
else:
    del lst[n:m]
    print(lst)

