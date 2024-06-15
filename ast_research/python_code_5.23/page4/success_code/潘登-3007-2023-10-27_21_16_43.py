a=eval(input())
lst=list(a)
n,m=eval(input())
if m>len(lst)-1 or n>len(lst)-1:
    print("error")
else:
    b=[]
    c=str(lst)
    b.append(lst[0:n])
    b.append(lst[m:])
    print(b)    
