a=list[eval(input())]
n,m=eval(input())
if n not in a or m not in a:
    print("error")
else:
    a.remove(a[n:m])
    print(a)    
