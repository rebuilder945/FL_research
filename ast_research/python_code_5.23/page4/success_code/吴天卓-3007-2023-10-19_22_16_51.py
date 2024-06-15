lst=eval(input())
n,m=eval(input())
if -len(lst)<=n<0<=m<=len(lst):
    del lst[n:m:-1]
    print(lst)
elif 0<=n<m<=len(lst):
    del lst[m:n]
    print(lst)
elif -len(lst)<=n<m<0:
    del lst[m:n]
    print(lst)
else:
    print("error")
