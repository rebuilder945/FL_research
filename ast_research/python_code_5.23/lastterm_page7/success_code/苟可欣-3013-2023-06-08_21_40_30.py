g=input().split()
ls=[]
ls1=[]
while g!=["ok"]:
    ls.append(g[0])
    ls1.append(int(g[1]))
print(ls)
print(ls1)
for x in ls:
    if x=='india':
        print("yes")
        break
    print("no")
print(sum(ls1))
