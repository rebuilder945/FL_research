lst=eval(input())
new=[]
ans=[]
for i in lst[::-1]:
    if i not in new:
        new.append(i)
for x in new[::-1]:
    ans.append(x)
print(ans)
