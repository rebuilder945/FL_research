li=eval(input())
li.reverse()
li1=[]
for x in li:
    if not x in li1:
        li1.append(x)
li1.reverse()
print(li1)
