name=input().split(',')
a=input().split(',')
b=[]
for i in range(0,len(a)):
    b.append([name[i],eval(a[i])])
print(b)

