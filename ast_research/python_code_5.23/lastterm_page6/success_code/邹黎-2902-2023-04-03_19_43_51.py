lst=[2,1,3,2]
b=0
c=0
for y in range (4,100):
    for x in range(3,y,2):
        b=lst[x-1]+lst[x]
        lst.append(b)
        for x in range(5,y,2):
            c=lst[x-3]
            lst.append(c)
print(lst)
