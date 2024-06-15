import operator
a=input().split(",")
b=list(eval(input()))
c=[]
for i in range(len(a)):
    d=[]
    d.append(a[i])
    d.append(b[i])
    c.append(d)
c.sort(key=operator.itemgetter(1))
print(c)
