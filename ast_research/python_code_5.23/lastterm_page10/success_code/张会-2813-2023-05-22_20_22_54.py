s1=input()
s=[]
for i in s1:
    s.append(i)
s2=input().split()
for x in s2:
    while x in s:
        s.remove(x)
print(''.join(s))

