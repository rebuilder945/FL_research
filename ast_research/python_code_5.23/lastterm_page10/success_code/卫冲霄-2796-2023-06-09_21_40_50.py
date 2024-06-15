s=input()
def mmn(s):
    l=0
    for i in s:
        if "0"<=i<="9":
            l+=1
    if l==0:
        return False
    else:
        return True
if mmn(s):
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
else:
    print("No digits")





