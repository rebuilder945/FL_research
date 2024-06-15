lst=eval(input())
m,n=eval(input())
lst2=[]
if n>len(lst)-1:
    print("error")
else:
    del lst[n]
    lst2.append(n)
    print(lst+lst2*m)
