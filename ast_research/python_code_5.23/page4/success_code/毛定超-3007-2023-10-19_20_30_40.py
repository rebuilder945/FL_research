list1=eval(input())
n,m=input().split(",")
n=int(n)
m=int(m)
if m >len (list1) or n >len (list1):
    print("error")
elif n<m:
        del list1[n:m]
        print(list1)
else:
        del list1[m+1:n+1]
        print(list1)


