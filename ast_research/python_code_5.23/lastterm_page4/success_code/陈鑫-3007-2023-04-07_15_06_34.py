lst=eval(input())
n,m=eval(input())
if n>len(lst) or m>len(lst):
    print("error")
elif n<m:
    lst.pop(n,m)
elif n==m:
    lst.pop(n)
else:
    lst.pop(m,n)
print(lst)
