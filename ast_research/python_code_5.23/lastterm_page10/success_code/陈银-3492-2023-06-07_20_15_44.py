a = input()
b=""
for x in a:
    if a.count(x)==1:
        b+=x
if len(b)!=0:
    print(b[0])
else:
    print("None")
