a=eval(input())
b=0
d=100

for i in a:
    if i>b:
        b=i
        
    if i<d:
        d=i
for i in a:
    if i==b:
        del a[i]
    if i==d:
        del a[i]
print(a)

    


