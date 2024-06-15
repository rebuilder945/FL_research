ls=eval(input())
n,m = input().split(',')
n=int(n)
m=int(m)
ls1=list(ls)
for x in range(n,m):
    if x in ls1:
        ls1.remove(x)
        print(ls1)
    else:
        print('Error')    
        
