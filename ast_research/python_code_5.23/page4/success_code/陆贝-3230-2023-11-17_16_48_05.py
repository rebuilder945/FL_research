a=eval(input())
a.sort(reverse=True)
s=""
for i in a:
    i=str(i)
    s=s+i
if s[0]=="0":
    print(0)
else:
    print(s)
