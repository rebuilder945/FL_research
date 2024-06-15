a = eval(input())
c = [x for x in range(1,a+1)]
b=[]
m=c[0]

for i in range(1,a):
    b.append(c[i])
b.append(m)

print(b)







