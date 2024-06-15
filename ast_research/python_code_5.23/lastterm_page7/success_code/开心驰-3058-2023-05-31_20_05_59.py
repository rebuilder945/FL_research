ans={}
bns=input()
while bns!='q':
    if bns not in ans:
        ans[bns]=1
    else:
        ans[bns]+=1
    bns=input()
b=max(ans.values())
for i in ans:
    if ans[i]==b:
        a=i
    else:
        pass
print('%s %d'%(a,b))

