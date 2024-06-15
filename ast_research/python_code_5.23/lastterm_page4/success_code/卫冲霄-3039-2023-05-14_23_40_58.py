ls=eval(input())
m=max(ls)
n=min(ls)
for i in range(len(ls)-1,-1,-1):
    if ls[i]==m or ls[i]==n:
        ls.pop(i)
print(ls)
