a = input()
b = list(a)
c =[]
d =[]
for i in b:
    m = (int(i)+5)%10
    c.append(m)
d = c[::-1]
print(*d,sep="")



