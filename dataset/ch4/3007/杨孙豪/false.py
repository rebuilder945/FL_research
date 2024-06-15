def kong(lst,n,m,a):
    if n in range(a) and m in range(a):
        lst[n:m]=[]
        return lst
    else:
        return str('error')
lst=eval(input())
print(lst[2],lst)
n,m=eval(input())
a=len(lst)-1
yaoyao=(kong(lst,n,m,a))
print(yaoyao)
    
