gdp = ''
g = {}
while True:
    gdp = input()
    if gdp == 'ok':
        break
    else:
        gdp = gdp.split()
        g[gdp[0]] = int(gdp[1])
c = list(g.keys())
print(sorted(c))
n = list(g.values())
print(sorted(n))
if 'India' in c:
    print('yes')
else:
    print('no')
print(sum(n))
