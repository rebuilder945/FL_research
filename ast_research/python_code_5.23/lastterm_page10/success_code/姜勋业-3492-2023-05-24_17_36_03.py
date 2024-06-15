a=input()
ls=[]
for i in a:
    if a.count(i)==1:
        print(i)
        ls.append(i)
        break
if ls==[]:
    print(None)

