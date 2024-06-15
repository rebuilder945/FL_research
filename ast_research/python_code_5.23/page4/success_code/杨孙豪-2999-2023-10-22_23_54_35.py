lst=list(map(str,input().split(' ')))
bst=list(map(int,input().split(' ')))
lst[bst[0]],lst[bst[1]]=lst[bst[1]],lst[bst[0]]
print(lst)
