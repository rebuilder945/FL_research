li1=eval(input())
li2=[]
for i in li1:
    if li1.count(i)==1:
        li2.append(i)
if li2==[]:
    print("False")
li2.sort()
s=",".join(str(x) for x in li2)
print(s)
