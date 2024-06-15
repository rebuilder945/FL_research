lst=eval(input())
a,b=eval(input())
n=min(a,b)
m=max(a,b)
for i in range(n,m):
    if m<len(lst):
       del lst[i]
    else:
        print("error")
print(lst)

