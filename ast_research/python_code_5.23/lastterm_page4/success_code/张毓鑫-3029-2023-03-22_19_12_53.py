a=[str(eval(input()))]
b=[eval(input())]
c=[([x,y] for x in a[i] for y in b[i]) for i in range(len(a))]
print(c)
