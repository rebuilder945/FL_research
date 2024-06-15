lst=eval(input())
n,m=eval(input())
lst2=[]
if n>len(lst)-1:
    print("error")
else:
    
    lst2.append(lst[n])
    del lst[n]
    print(lst+lst2*m)
