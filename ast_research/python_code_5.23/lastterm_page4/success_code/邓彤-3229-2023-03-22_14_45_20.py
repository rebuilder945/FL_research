a=eval(input())
b=[]
for x in a:
    if a.count(x)==1:
        b.append(x)
if b==[]:
    print("Flase")
else:
    print(b)
