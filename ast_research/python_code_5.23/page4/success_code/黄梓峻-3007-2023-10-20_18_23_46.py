list1=input().split()
m,n=eval((input()).split())
if n>m or n<1 or m>len(list1):
    print("error")
else:
    del list1[n-1:m-1]
    print(".join(list1)")
