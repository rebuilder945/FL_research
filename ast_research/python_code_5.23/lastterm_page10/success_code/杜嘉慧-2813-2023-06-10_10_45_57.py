s=input()
ans=input()
la=len(s)
lb=len(ans)
lst=[]
for i in range(la):
    if s[i,i+lb]!=ans:
        lst.append(s[i,i+lb])
print("".join(x for x in lst))
