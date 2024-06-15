a=input().split(',')
b=eval(input())
d=[]
for x in range(len(a)):
    d.append([a[x],int(b[x])])
print(d)

