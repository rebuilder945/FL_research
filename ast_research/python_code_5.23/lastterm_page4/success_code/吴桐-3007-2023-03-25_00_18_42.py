lst1=eval(input())
n,m=eval(input())
if n>len(lst1) or m>len(lst1):
    print("error")
else:
    del lst1[n:m]
    print(lst1)

