s1=set()
s2=set()
x=list(input())
y=list(input())
for m in x:
    s1.add(m)
for n in y:
    s2.add(n)
if s1==s2:
    print("True")
else:
    print("False")
