s="".join(input())
a=[]
for i in s:
    if s.count(i)==1:
        a.append(i)
if len(a)==0:
    print("None")
else:
    print(a[0])

