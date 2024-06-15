ls = eval(input())
a = max(ls)
b = min(ls)
js = 0
for x in range(len(ls)):
    if ls[x] == a or ls[x]==b:
       ls[x] = 516
       js +=1
while js>0:
    ls.remove(516)
    js-=1
print(ls)
