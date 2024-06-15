ls=eval(input())
ls.sort(reverse=True)
s=""
for i in range(len(ls)):
    s=s+str(ls[i])
print(s)
