a=eval(input())
a.sort()
j=0
for x in a:
    c=x*10**(a.index(x))
    j=j+c
print(j)
#c=lst.index(21)
#print(c)
