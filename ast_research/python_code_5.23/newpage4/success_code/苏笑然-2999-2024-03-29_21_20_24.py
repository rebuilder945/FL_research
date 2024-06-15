a=input()
list=a.split( )
n,m=eval(input())
if n>m:
    list.insert(m,list[n])
    list.insert(n+1,list[m+1])
    del list[m+1]
    del list[n+1]
else:
    list.insert(n,list[m])
    list.insert(m+1,list[n+1])
    del list[n+1]
    del list[m+1]
print(list)
