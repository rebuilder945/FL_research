lst=[eval(input())]
n,m=eval(input())
if n not in lst:
    print("error")
else:
    lst.remove(lst[n:m])
    print(lst)    
