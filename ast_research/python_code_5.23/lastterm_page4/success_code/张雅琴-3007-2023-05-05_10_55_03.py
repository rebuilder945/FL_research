lst=eval(input())
n,m=eval(input())
a=len(lst)-1
if n<=a and m<=a:
    lst1=[]
    lst2=[]
    lst1.append(lst[0:n])
    lst2.append(lst[m:])
    lst3=lst1+lst2
    print(lst3)
elif n>a or m>a:
    print("error")
