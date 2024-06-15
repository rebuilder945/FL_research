a=input().split(',')
b=[eval(input())]
c=[[a[x],b[x]] for x in range(len(a))]
print(c)
