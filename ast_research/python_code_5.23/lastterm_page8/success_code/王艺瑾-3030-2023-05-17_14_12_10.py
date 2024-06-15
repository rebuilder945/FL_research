a=input.split(",")
b=input.split(',')
c=[eval(i),i in b]
d=[]
for x in range(len(a)):
    d.append([a[x],c[x]])
d.sort(key=lambda x:x[1])
print(d)

            


