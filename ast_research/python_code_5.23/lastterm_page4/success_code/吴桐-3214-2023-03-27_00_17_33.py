li1=eval(input())
li2=li1.copy()
for i in range(len(li1)):
    if li1[i]==0:
       li2.remove(li1[i])
       li2.append(0)
print(li2)


