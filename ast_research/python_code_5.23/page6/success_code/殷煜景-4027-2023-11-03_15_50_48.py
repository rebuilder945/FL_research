list1=[]
m=1
i=0
while m!="#":
    m=input()
    if m=="#":
        break
    list1.append(eval(m))
    i+=1
print(i,sum(list1),end="")

