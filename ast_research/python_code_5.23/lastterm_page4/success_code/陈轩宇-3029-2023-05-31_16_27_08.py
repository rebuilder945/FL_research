Sname = input().split(",")
Sgrades = eval(input())
c = []
for i in range(0,len(Sname)):
    temp = []
    temp.append(Sname[i])
    temp.append(Sgrades[i])
    c.append(temp)
print(c)


