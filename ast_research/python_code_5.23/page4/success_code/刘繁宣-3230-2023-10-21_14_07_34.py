ls=eval(input())
ls.sort(reverse=True)
s=""
for i in range(len(ls)):
    s=s+str(ls[i])
if s[0]==0:
    s=0
print(s)
