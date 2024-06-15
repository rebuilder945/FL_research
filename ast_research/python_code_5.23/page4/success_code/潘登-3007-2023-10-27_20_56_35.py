lst=[eval(input())]
n,m=eval(input())
if m>len(lst)-1 and n>=len(lst)-1:
    print("error")
else:
    lst.remove(lst[n:m])
    print(lst)    
