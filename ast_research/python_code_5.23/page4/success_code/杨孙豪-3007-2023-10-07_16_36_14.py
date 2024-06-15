lst=list((input()))
n,m=eval(input())
a=len(lst)-1
def kong(lst,n,m,a):
    if n in range(a) and m in range(a):
        del lst[n:m]
        return list(lst)
    else:
        return str('error')
print(kong(lst,n,m,a))
    
