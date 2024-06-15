n=eval(input())
a=0
for i in n:
    if i == 0:
        a+=1
        n.remove(0)
for i in range(a):
    n.append(0)
print(n)
