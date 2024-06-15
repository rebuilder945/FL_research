a=input().split(',')
b=eval(input())
d=[]
for i in range(len(b)):
    d+=[[a[i],b[i]]]
print(d)
