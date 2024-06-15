a=input().split()
b=0
for i in a:
    if a.count(i)>b:
        b=a.count(i)
for i in a:
    if a.count(i)==b:
        print(i,a.count(i))
    






