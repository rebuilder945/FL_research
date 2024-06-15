s1=input()
s2=input()
t=set([])
t1=set([])
for i in s1:
    if i not in t:
        t.add(i)
for j in s2:
    if j not in t1:
        t1.add(j)
if t==t1:
    print("True")
else:
    print("False")



