s=input()
ans={}
while s!="q":
    ans[s]=ans.get(s,0)+1
    s=input()
print(max(ans,key=ans.get),end="")
print(max(ans.values()))

