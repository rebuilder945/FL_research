a=eval(input())
lst=list(a)
n,m=eval(input())
if m>len(lst)-1 or n>len(lst)-1:
    print("error")
else:
    b=[]
    b.append(int(str(lst[0:n])))
    b.append(int(str(lst[m:])))
    print(b)    
