lst=eval(input())
n,m=eval(input())
if n>=len(lst) or m>=len(lst) or n>m:
    print("error")
else:
    for x in range(n,m):
        del lst[x]
print(lst)
    
