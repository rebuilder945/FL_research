lst=list(map(str,input().split(',')))
bst=eval(input())
newlist=[[lst[i],bst[i]]for i in range(len(lst))]
print(newlist)

