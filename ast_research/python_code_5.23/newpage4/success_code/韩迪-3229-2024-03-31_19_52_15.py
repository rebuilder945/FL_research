a=list(eval(input()))
a.sort()
s=[]
for i in a:
    if a.count(i)==1:
        s.append(i)
    else:
        pass
if s:
    print(s)
else:
    print("False")
