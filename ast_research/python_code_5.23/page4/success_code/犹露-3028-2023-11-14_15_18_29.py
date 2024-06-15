a,b,c = eval(input())

d =[]
i = 0
d.append(a)
for i in range(b-1):
    a+=c
    i+=1
    d.append(a)
print(d)



