n1=eval(input())
n1.sort()
n2=0
for x in range(len(n1)):
    n2=n1[x]*10**x+n2
print(n2)

