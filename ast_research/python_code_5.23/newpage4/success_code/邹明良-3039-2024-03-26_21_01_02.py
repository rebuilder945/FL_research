ls = list(eval(input()))
max = max(ls)
min = min(ls)
a = ls.count(max)
b = ls.count(min)
for i in range(a):
    ls.remove(max)
if len(ls) !=0:
    for i in range(b):
        ls.remove(min)
print(ls)
