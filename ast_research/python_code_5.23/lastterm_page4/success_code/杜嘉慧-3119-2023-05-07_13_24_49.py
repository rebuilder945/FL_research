lst=eval(input())
new=[]
ans=[]
for x in lst[::-1]:
    if x not in new:
        new.append(x)
for x in new[::-1]:
    ans.append(x)
print(ans)
