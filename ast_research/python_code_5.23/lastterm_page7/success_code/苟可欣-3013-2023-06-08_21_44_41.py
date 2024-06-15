g=input().split()
ls=[]
ls1=[]
while g!=["ok"]:
    ls.append(g[0])
    ls1.append(int(g[1]))
    g=input().split()
ls.sort()
ls1.sort()
print(ls)
print(ls1)
n=0
for x in ls:
    if x=='India':
        print("yes")
        n=n+1
        break
if n==0:
    print("no")
print(sum(ls1))
