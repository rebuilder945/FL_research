a=eval(input())
a.sort(reverse=True)
s=""
for x in a:
    s=s+str(s)
s=int(s)
print(s)

