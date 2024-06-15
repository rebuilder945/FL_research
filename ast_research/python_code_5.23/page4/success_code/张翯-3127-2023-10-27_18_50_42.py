n=eval(input())
lst=[x for x in range(1,n+1)]
for i in range(len(lst)):
    if i+1 < len(lst):
       lst[i]=lst[i+1]
    else:
        lst[i]=1
print(lst) 
