n=input() or "ok"
dic={}
ls,ls1=[],[]
while n != "ok":
    c,g=n.split()
    ls.append(c)
    ls1.append(g)
    n=input() or "ok"
ls2=list(map(int,ls1))
print(ls)
print(ls2)
if "india" not in ls:
    print("no")
else:
    print("yes")
print(sum(ls2))

