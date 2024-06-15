a=eval(input())
b=a+1
c=[a for a in range(1,b)]
d=int(c[0])
for d in 1 :
    c.remove(1)
    c.append(1)
    break
print(c)
