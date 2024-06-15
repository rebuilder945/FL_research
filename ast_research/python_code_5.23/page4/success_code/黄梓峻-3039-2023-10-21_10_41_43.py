lst=list(map(int,input().split()))
max_val=max(lst)
min_val=min(lst)
lst=[x for x in lst if x !=max_val and x !=min_val]
print(lst)
