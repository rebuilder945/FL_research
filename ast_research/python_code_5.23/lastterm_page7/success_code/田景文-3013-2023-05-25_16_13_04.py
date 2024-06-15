gdp = {}
a = input()
while a != 'ok':
    k,v = map(str,a.split())
    gdp[k] = eval(v)
    a = input()
ls1 = list(gdp.keys())
ls2 = list(gdp.values())
ls1.sort()
ls2.sort()
print(ls1)
print(ls2)
if "India" in gdp:
    print("yes")
else:
    print("no")
print(sum(ls2))
