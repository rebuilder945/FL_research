ls=eval(input())
n,m = input().split(',')
n=int(n)
m=int(m)
n=min(n,m)
m=max(n,m)
lst=list(ls)
for x in range(n,m):
    if x<=len(lst)-1:
        lst.remove(x)
        print(lst)
    else:
        print('Error')    
        
