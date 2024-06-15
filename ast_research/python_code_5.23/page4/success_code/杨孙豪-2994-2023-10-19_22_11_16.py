lst=list(map(int,input().split(',')))

n,m=eval(input())
bst=[]
if n>len(lst)-1:
    print('error')
else:
    bst.append(lst[n])
    
    cst=bst*m
    dst=lst+cst
    print(dst)
