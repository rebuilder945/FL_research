a=input()
b=eval(input())
c=a.split(",")
c=list(c)

d=[]
for i in range(len(c)):
    m=[c[i],b[i]]
    d.append(m)



print(d)
