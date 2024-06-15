a = eval(input())
b = []
c = ""
for i in a:
    if i not in b:
        b.append(i)
for x in range(len(b)):
    if a.count(b[x])==1:
       c+=str(b[x])+","
if len(c)==0:
    print("False")
else:
    print(c)

