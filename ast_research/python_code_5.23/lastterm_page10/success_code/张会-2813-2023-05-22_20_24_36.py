s1=input()
s2=input()
s=[]
s3=[]
for i in s1:
    s.append(i)
for i in s2:
    s3.append(i)
for x in s3:
    while x in s:
        s.remove(x)
print(''.join(s))

