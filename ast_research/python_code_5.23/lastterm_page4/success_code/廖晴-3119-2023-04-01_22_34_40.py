s=eval(input())
s.reverse()
s2=[]
for x in s:
    if x not in s2:
        s2.append(x)
s2.reverse()
print(s2)
