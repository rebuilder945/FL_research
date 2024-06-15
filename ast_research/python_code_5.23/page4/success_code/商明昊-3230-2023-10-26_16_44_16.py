t=eval(input())
t=list(map(int,t))
t.sort()
t.reverse()
res=""
for i in t:
    res =res+str(i)
res=eval(res)
print(res)
