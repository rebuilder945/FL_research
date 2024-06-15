s=input()
ls=[0 for i in range(len(s)+1)]
for i in range(1,len(s)+1):
    if "0"<=s[i-1]<="9":
        ls[i]=ls[i-1]+1
    mmax=max(ls)
for i in range(len(ls)-1,-1,-1):
    if ls[i]==mmax:
        q=i
        break
print(s[q-mmax:q])






