name=input().split(",")
grade=input().split(",")

lt=[]
for i in list(range(len(name))):
    ls=[]
    ls.append(name[i])
    ls.append(int(grade[i]))
    lt.append(ls)
lt.sort(key=lambda ls:ls[1])
print(lt)

