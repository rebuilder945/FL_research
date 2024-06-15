a=eval(input())
i=0
while 0 in a:
    a.remove(0)
    i+=1
for b in range(0,i):
    a.append(0)
print(a)
