lst=eval(input())
n,m=eval(input())
if -len(lst)<=n<m<=len(lst):
    del lst[n:m]
    print(lst)
#elif -len(lst)<=m<n<len(lst):
    #del lst[m:n]
    #print(lst)
else:
    print("error")
