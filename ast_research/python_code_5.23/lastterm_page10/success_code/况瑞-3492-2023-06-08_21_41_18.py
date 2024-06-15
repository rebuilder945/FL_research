b=input()
a=list(b)
b=""
for i in a:
    if a.count(i)==1:
        b=i
        break
    else:
        continue
if b=="":
    print(None)
else:
    print(b)


