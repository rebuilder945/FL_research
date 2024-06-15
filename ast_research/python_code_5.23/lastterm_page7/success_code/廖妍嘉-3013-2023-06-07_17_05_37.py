n=input() or "ok"
dic={}
ls,ls1=[],[]
while n != "ok":
    c,g=n.split()
    ls.append(c)
    ls1.append(g)
    n=input() or "ok"
ls2=list(map(int,ls1))
print(ls.sort())
print(ls2.sort())
if "India" not in ls:
    print("no")
else:
    print("yes")
print(sum(ls2))

