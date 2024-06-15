#4
s = input()
nls = []
mls = []
while s != "ok":
    n,m = s.split()
    nls.append(n)
    mls.append(eval(m))
    s = input() or "ok"
mls.sort()
nls.sort()
print(nls)
print(mls)
if "India" in nls:
    print("yes")
else:
    print("no")
print(sum(mls))

