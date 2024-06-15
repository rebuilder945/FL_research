from audioop import reverse


x=eval(input())
x.sort(reverse=True)
s=""
for i in range(0,len(x)):
    s+=str(x[i])
if s[1]=="0":
    s="0"
print(s)
