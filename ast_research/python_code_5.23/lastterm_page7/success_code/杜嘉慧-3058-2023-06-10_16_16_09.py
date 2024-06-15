s=input()
ans={}
if s!="q":
    ans[s]=ans.get(s,0)+1
print(max(ans,key=ans.get()),end="")
print(max(ans.values()))

