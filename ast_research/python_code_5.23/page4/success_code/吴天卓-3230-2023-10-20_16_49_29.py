l=eval(input())
l.sort(reverse=True)
s=""
for i in l:
    s+=str(i)
print(int(s))
