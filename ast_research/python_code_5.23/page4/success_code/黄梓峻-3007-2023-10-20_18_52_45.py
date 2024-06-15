A=input()
n,m=input().split('')
lst=list(A)
n=int(n)
m=int(m)
if n<1 or n>m or m>len(lst):
    print("error");
else:
    del lst[n:m]
    print(lst)
