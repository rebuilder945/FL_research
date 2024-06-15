x=input()
l=[]
for i in x:
    if x.count(i)==1:
        l.append(i)
if l==[]:
    print("None")
else:
    print(l[0])
