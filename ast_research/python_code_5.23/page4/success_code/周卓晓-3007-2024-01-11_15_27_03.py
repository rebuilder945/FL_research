lst=eval(input())
n,m=eval(input())
l=len(lst)
ls=[]
if n>m or n>l or m>l:
    print("error")
else:
    for i in range(n):
        ls.append(lst[i])
    for x in range(m,len(lst)):
        ls.append(lst[x])
    print(ls)
