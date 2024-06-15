s = eval(input())
m = list (s)
j = 0
for x in m :
    if x == 0:
        j += 1
    else:
        continue
for i in m:
    m.remove(0)
m.remove(0)
print(m)
for h in range(j):
   m.append(0)
print(m)



