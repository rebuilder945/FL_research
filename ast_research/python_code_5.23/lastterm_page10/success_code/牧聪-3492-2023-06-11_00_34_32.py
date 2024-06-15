a=input()
b=[]
for x in a:
    if a.count(x)==1:
        print(x)
        b.append(x)
        break
if not b:
    print(None)
