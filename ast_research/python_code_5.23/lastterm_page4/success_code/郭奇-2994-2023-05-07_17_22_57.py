lst= input().split(',') 
n,m=map(int,input().split(','))
a=len(lst)

if n>=a:
    print("error")
else:
    lst.append(lst[n]*m)
    print(lst)


