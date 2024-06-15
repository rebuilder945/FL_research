lst=[eval(input())]
lst=','.join
n,m=eval(input())
if n not in lst or m not in lst:
    print("error")
else:
    lst.remove(lst[n:m])
    print(lst)    
